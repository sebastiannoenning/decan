import sys, math, re
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QEasingCurve, Slot, QPointF, Signal
from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QWidget, QLabel, QCalendarWidget, QSpinBox
from PySide6.QtWidgets import QSizePolicy, QToolButton, QMenu
from PySide6.QtGui import QFont, QIcon

import views.resources.assets.rss 

class DateSelect(QCalendarWidget):
    def __init__(self, parent, 
                 theme='light'):
        super().__init__(parent)
        self.theme=theme
        self.__setup_ui()
        self.__setup_connections()

    def __setup_ui(self):
        self.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setGridVisible(False)

        self._header = self.findChild(QHBoxLayout) # Find _header
        self._nav = self.findChild(QWidget, "qt_calendar_navigationbar")
        self._nav.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self._nav.setContentsMargins(0,0,0,0)
        self._header.setContentsMargins(0,0,0,0)

        self._prevMonth = self._nav.findChild(QToolButton,"qt_calendar_prevmonth")
        self._nextMonth = self._nav.findChild(QToolButton,"qt_calendar_nextmonth")
        self._monthButton = self._nav.findChild(QToolButton, "qt_calendar_monthbutton")
        self._yearButton = self._nav.findChild(QToolButton, "qt_calendar_yearbutton")
        self._yearEdit = self._nav.findChild(QSpinBox, "qt_calendar_yearedit")
        self._monthMenu = self._monthButton.findChild(QMenu)

        # Remove & hide all widgets from layout
        self._header.removeWidget(self._prevMonth), self._prevMonth.hide()
        self._header.removeWidget(self._nextMonth), self._nextMonth.hide()
        self._header.removeWidget(self._monthButton), self._monthButton.hide()
        self._header.removeWidget(self._yearButton), self._yearButton.hide()
        self._header.removeWidget(self._yearEdit), self._yearEdit.hide()
        # Remove excess/unimportant spacers from layout
        for x in range(self._header.count()-1, -1, -1):
            spacer = self._header.takeAt(x)
            del spacer
        
        self._yearLabel = QLabel(self._nav, text=str(self._yearEdit.value()))
        self._yearUpButton = QPushButton(icon=QIcon(f":/icons/arrows/arrow_up_{self.theme}.svg"))
        self._yearDownButton = QPushButton(icon=QIcon(f":/icons/arrows/arrow_down_{self.theme}.svg"))

        self._yearLabel.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self._yearUpButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self._yearDownButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self._monthButton.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)

        fontStyle = QFont('Arial', 13)
        self._yearLabel.setFont(fontStyle)
        self._yearLabel.setContentsMargins(2,0,2,0)
        self._yearLabel.setAutoFillBackground(True)
        self._monthButton.setFont(fontStyle)
        self._monthButton.setContentsMargins(2,0,2,0)

        self._nav.setStyleSheet("background-color: grey;"
                                "border-radius: 4px;")
        self._yearUpButton.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                         "border-radius: 0px;"
                                         "padding-left: 4px;"
                                         "padding-right: 4px;"
                                         "border-top-left-radius: 4px;"
                                         "border-bottom-left-radius: 4px;")
        self._yearDownButton.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                           "border-radius: 0px;"
                                           "padding-left: 4px;"
                                           "padding-right: 4px;"
                                           "border-left: 1px solid rgba(255, 255, 255, 0.5);")
        self._yearLabel.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                      "padding: 2px;"
                                      "border-radius: 0px;"
                                      "border-left: 1px solid rgba(255, 255, 255, 0.5);")
        self._monthButton.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                        "border-radius: 0px;"
                                        "text-align: left;"
                                        "border-left: 1px solid rgba(255, 255, 255, 0.5);")
        self._monthMenu.setStyleSheet("background-color: rgba(125, 125, 125, 0.8);"
                                      "border-left: 0px rgba(0,0,0,0);"
                                      "border-bottom-left-radius: 4px;"
                                      "border-bottom-right-radius: 4px;")
        self._prevMonth.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                      "border-radius: 0px;"
                                      "border-left: 1px solid rgba(255, 255, 255, 0.5);"
                                      "padding-left: 4px;"
                                      "padding-right: 4px;"
                                      f"qproperty-icon: url(:/icons/arrows/arrow_left_{self.theme}.svg);")
        self._nextMonth.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                      "border-radius: 0px;"
                                      "padding-left: 4px;"
                                      "padding-right: 4px;"
                                      "border-top-right-radius: 4px;"
                                      "border-bottom-right-radius: 4px;"
                                      "border-left: 1px solid rgba(255, 255, 255, 0.5);"
                                      f"qproperty-icon: url(:/icons/arrows/arrow_right_{self.theme}.svg);")
                                      

        self._header.addWidget(self._yearUpButton)
        self._header.addWidget(self._yearDownButton)
        self._header.addWidget(self._yearLabel)
        self._monthButton.show(), self._header.addWidget(self._monthButton)
        self._prevMonth.show(), self._header.addWidget(self._prevMonth)
        self._nextMonth.show(), self._header.addWidget(self._nextMonth)

    def __setup_connections(self):
        self._yearUpButton.clicked.connect(lambda: self._stepUpYearEdit())
        self._yearDownButton.clicked.connect(lambda: self._stepDownYearEdit())

    def setMinimumDate(self, date):
        if (self.selectedDate().year() < date.year()): self._yearLabel.setText(date.year())
        super().setMinimumDate(date)
    
    def setMaximumDate(self, date):
        if (self.selectedDate().year() > date.year()): self._yearLabel.setText(date.year())
        super().setMaximumDate(date)

    """ QCalendarWidget has a private model & signal/slot connections it uses to update the view with.
            As these are private/inaccessible & difficult to reimplement, it is preferable to simply re-emit
            the signal connected with the slot '_q_yearEditingFinished()', which is editingFinished.
            
            The original way the QCalendarWidget works is by listening to connections from yearEdit & 
            yearButton and swapping their visibility in the layout. As the '_q__yearEditingFinished'
            slot is being reused & both original buttons are detached/hidden from the nav header,
            addtional handling to hide both widgets is reimplemented.

            Source code visible here:
                https://codebrowser.dev/qt5/qtbase/src/widgets/widgets/qcalendarwidget.cpp.html
    """ 
    def _stepUpYearEdit(self):
        """ Private access function. Manually changes yearEdit spinbox via stepUp, emits a editingFinished
            signal & updates the yearLabel text to match the current yearEdit.value() """
        self._yearEdit.stepUp(), self._yearEdit.editingFinished.emit()
        self._yearLabel.setText(str(self._yearEdit.value()))
        self._yearEdit.hide(), self._yearButton.hide()

    def _stepDownYearEdit(self): 
        """ Private access function. Manually changes yearEdit spinbox via stepDown, emits a editingFinished
            signal & updates the yearLabel text to match the current yearEdit.value() """
        self._yearEdit.stepDown(), self._yearEdit.editingFinished.emit()
        self._yearLabel.setText(str(self._yearEdit.value()))
        self._yearEdit.hide(), self._yearButton.hide()

class TDateEditDialog(QDialog):
    def __init__(self, parent = ..., f = ...):
        super().__init__(parent, f)
        self._dateSelect = DateSelect

    def dateSelect(self): return self._dateSelect