import sys, math, re
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QEasingCurve, Slot, QPointF
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy, QStyleOption, QStyle, QCalendarWidget
from PySide6.QtGui import QFont, QPainter

from modules.touchdatetime.tdateedit import TDateEditDialog
from modules.touchdatetime.ttimeedit import TTimeEditDialog

from modules import datetime_qt as dt_qt

class DTPushButton(QLabel):
    clicked = Signal()

    def __init__(self, parent, 
                 type: dt_qt.EDateTime=None,
                 dateTime = QDateTime(QDate(0,0,0),QTime(0,0))):
        super().__init__(parent)
        self._eventPressed = False # Flag
        self._dateTime = dateTime
        if (type == None): type = dt_qt.EDateTime.Date # Reject Edt_qt.EDateTime.DateTime
        self._type = type
        self._opacity = 0.3

        self.__setup_ui()

    def __setup_ui(self):
        self.setText(self._dateTime)
        self.setFont(QFont('Arial',15))
        self.setInactiveStyle()

    def __set_styles(self, 
                 color: str, 
                 opacity=float(0.5),
                 bg_color=0, 
                 test_en=False):
        if (color == 'red'): color = 'rgba(255, 80, 80, 0.9)'
        else: color = 'white'
        opacity %= 1
        bg_color %= 255
        padding = 6
        self.setStyleSheet("border-radius: 4px;"
                           f"background-color: rgba({bg_color}, {bg_color}, {bg_color}, {opacity});"
                           f"color: {color};"
                           f"padding: {padding}px;"
        )
        pref_height = (self.font().pointSize()
                       + (2 * padding) + 2)
        if(test_en): print(pref_height)
        #self.setMinimumHeight(pref_height)
        self.adjustSize()

    def setText(self, dateTime: QDateTime):
        self._dateTime = dateTime
        super().setText(dt_qt.dateTimeToFS(self._dateTime, self._type))
        self.adjustSize()       # CHECK FOR ERROR LATER; DOES ADJUST SIZE CALL AFTER THE SET TEXT CALL?

    def setFont(self, arg):
        self.__set_styles('white')
        super().setFont(arg)

    def setInactiveStyle(self):
        self.__set_styles(color='white', opacity=self._opacity)

    def setActiveStyle(self):
        self.__set_styles(color='red', opacity=self._opacity)

    def mousePressEvent(self, event):
        self._eventPressed = True
        self.setActiveStyle()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if (self._eventPressed):
            self._eventPressed = False
            self.clicked.emit()
        super().mouseReleaseEvent(event)

    def date(self):
        return self._dateTime

class TDateTimeEdit(QWidget):
    """ Base class for opening QCalendar & TDateTimeEdit
    """
    dateTimeChanged = Signal(QDateTime)

    def __init__(self, parent, 
                 dateTime = QDateTime.currentDateTime()):
        super().__init__(parent)
        self._minimumDateTime = QDateTime()
        self._dateTime = dateTime
        self._maximumDateTime = QDateTime()
        self.__setup_ui()
        self.__set_styles()
        self.__setup_connections()
    
    def __setup_ui(self):
        self._button_container = QHBoxLayout(self)
        self._button_container.addStretch(1)

        self._dateEdit_pushButton = DTPushButton(self, dt_qt.EDateTime.Date, self._dateTime)
        self._timeEdit_pushButton = DTPushButton(self, dt_qt.EDateTime.Time, self._dateTime)

        self.layout().addWidget(self._dateEdit_pushButton)
        self.layout().addWidget(self._timeEdit_pushButton)

        self._timeEdit_editDialog = TTimeEditDialog(self, self._dateTime)
        self._dateEdit_editDialog = TDateEditDialog(self, self._dateTime)

    def __set_styles(self):
        self.layout().setContentsMargins(
            0,          #Left
            0,          #Top
            0,          #Right
            0           #Bottom
            )
        self.setMinimumHeight(self._dateEdit_pushButton.sizeHint().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        #self.setStyleSheet(
        """TDateTimeEdit{
                border: 1px solid black;
                border-radius: 5px;
            }"""#)

    def __setup_connections(self):
        self._dateEdit_pushButton.clicked.connect(
            lambda: self._openDialogue(self._dateEdit_editDialog)
        )
        self._timeEdit_pushButton.clicked.connect(
            lambda: self._openDialogue(self._timeEdit_editDialog)
        )
        self._dateEdit_editDialog.dateSelected.connect(
            lambda date: self._closeDialogue(
                new_date=date)
        )
        self._timeEdit_editDialog.timeSelected.connect(
            lambda time: self._closeDialogue(
                new_time=time)
        )
        self._dateEdit_editDialog.rejected.connect(
            lambda: self._dateEdit_pushButton.setInactiveStyle()
        )
        self._timeEdit_editDialog.rejected.connect(
            lambda: self._timeEdit_pushButton.setInactiveStyle()
        )

    def _openDialogue(self, dialog: QDialog):
        dialog.show()

    def _closeDialogue(self,
                       new_date = QDate(), 
                       new_time = QTime(),
                       test_en=True):
        if (new_date != QDate()):
            if (new_date > self._dt_qt.EdateTime.date()): self._dateTime = QDateTime(self._dt_qt.EdateTime.date(),(QTime(0,0,0,0)))
            self._dateTime = QDateTime(new_date, self._dt_qt.EdateTime.time())
        if (new_time != QTime()):   self._dateTime = QDateTime(self._dateTime, (new_time))

        if (test_en): print(f"TDE_:{hex(id(self))}############\nCLOSED DIA; NEW DTE {self._dateTime}")

        self._updateButton(self._dateEdit_pushButton)
        self._updateButton(self._timeEdit_pushButton)
        
        self.dateTimeChanged.emit(self._dateTime)

    def _updateButton(self,
                      button: DTPushButton):
        button.setText(self._dateTime)
        button.setInactiveStyle()
        button.update()

    
    def _autoUpdateButton(self, test_en=True):
        if (test_en): print(self._dateEdit_pushButton.date())

        if (self._dateEdit_pushButton.date() < self._dateTime): self._updateButton(self._dateEdit_pushButton)
        if (self._timeEdit_pushButton.date() < self._dateTime): self._updateButton(self._timeEdit_pushButton)  

    def _updateMaximumDateTime(self):
        #self._timeEdit_editDialog
        self._dateEdit_editDialog.setMaximumDate(self._maximumDateTime)

    def _updateMinimumDateTime(self, test_en=True):
        self._timeEdit_editDialog.setMinimumDateTime(self._minimumDateTime)
        self._dateEdit_editDialog.setMinimumDate(self._minimumDateTime.date())

        if (test_en): print(f"TDE_:{hex(id(self))}############\nUPDATE MIN DT; NEW MIN DT {self._minimumDateTime}\nCUR DT: {self._dateTime}")
        self._autoUpdateButton()

    def _updateDateTime(self, test_en=True):
        self._timeEdit_editDialog.setCurrentDateTime(self._dateTime);           self._updateButton(self._timeEdit_pushButton)
        self._dateEdit_editDialog.setSelectedDate(self._dateTime.date());       self._updateButton(self._dateEdit_pushButton)

        if (test_en): print(f"TDE_:{hex(id(self))}############\nUPDATE CUR DT; NEW CUR DT {self._dateTime}")

    # Setters for both minimumDateTime & maximumDateTime
    def setDateRange(self, min: QDate, max: QDate):             self._minimumDateTime.setDate(min); self._maximumDateTime.setDate(max)
    def setDateTimeRange(self, min: QDateTime, max: QDateTime): self._minimumDateTime, self._maximumDateTime = min, max

    # Setters for _minimumDateTime
    def setMinimumDateTime(self, datetime: QDateTime):  self._minimumDateTime = datetime;       self._updateMinimumDateTime()
    def setMinimumDate(self, date: QDate):              self._minimumDateTime.setDate(date);    self._updateMinimumDateTime()
    def setMinimumTime(self, time: QTime):              self._minimumDateTime.setTime(time);    self._updateMinimumDateTime()
    # Functions for clearing _minimumDateTime
    def clearMinimumDateTime(self): self._minimumDateTime = QDateTime();                        self._updateMinimumDateTime()
    def clearMinimumDate(self):     self._minimumDateTime.setDate(QDate());                     self._updateMinimumDateTime()
    def clearMinimumTime(self):     self._minimumDateTime.setTime(QTime());                     self._updateMinimumDateTime()
    # Getters for _minimumDateTime
    def minimumDateTime(self):      return self._minimumDateTime
    def minimumDate(self):          return self._minimumDateTime.date()
    def minimumTime(self):          return self._minimumDateTime.time()

    # Setters for _maximumDateTime
    def setMaximumDateTime(self, datetime: QDateTime):  self._maximumDateTime = datetime;       self._updateMaximumDateTime()
    def setMaximumDate(self, date: QDate):              self._maximumDateTime.setDate(date);    self._updateMaximumDateTime()
    def setMaximumTime(self, time: QTime):              self._maximumDateTime.setTime(time);    self._updateMaximumDateTime()
    # Functions for clearing _maximumDateTime
    def clearMaximumDateTime(self): self._maximumDateTime = QDateTime();                        self._updateMaximumDateTime()
    def clearMaximumDate(self):     self._maximumDateTime.setDate(QDate());                     self._updateMaximumDateTime()
    def clearMaximumTime(self):     self._maximumDateTime.setTime(QTime());                     self._updateMaximumDateTime()
    # Getters for _maximumDateTime
    def maximumDateTime(self):      return self._maximumDateTime()
    def maximumDate(self):          return self._maximumDateTime.date()
    def maximumTime(self):          return self._maximumDateTime.time()

    # Functions for returning dateTime
    def dateTime(self):             return self._dateTime

    # Reimplemented paintEvent for advanced styling
    def paintEvent(self, pe):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
