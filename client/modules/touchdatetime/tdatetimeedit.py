import sys, math, re
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QEasingCurve, Slot, QPointF, Property
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
        padding = 6
        self.setStyleSheet( "border-radius: 4px;"
                            "border: none;"
                            "background-color: rgba(40,40,40,1);"
                            "color: white;"
                            "padding: 6px;"
        )
        pref_height = (self.font().pointSize()
                       + (2 * padding) + 2)
        if(test_en): print(pref_height)
        #self.setMinimumHeight(pref_height)
        self.adjustSize()

    def setText(self, dateTime: QDateTime):
        self._dateTime = dateTime
        super().setText(dt_qt.date_time_to_fs(self._dateTime, self._type))
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
    
    def resizeEvent(self, event):
        
        return super().resizeEvent(event)

class TDateTimeSelect(QWidget):
    """ Base class for opening QCalendar & TDateTimeEdit
    """
    dateTimeChanged = Signal(QDateTime)

    def __init__(self, parent, 
                 dateTime = QDateTime.currentDateTime()):
        super().__init__(parent)
        self._minimumDateTime       = QDateTime()
        self._DateTime  :QDateTime  = dateTime
        self._maximumDateTime       = QDateTime()

        self._allday    :bool       = False

        self.__setup_ui()
        self.__set_styles()
        self.__setup_connections()
    
    def __setup_ui(self):
        self._button_container = QHBoxLayout(self)
        self._button_container.addStretch(1)

        self.dateEditButton = DTPushButton(self, dt_qt.EDateTime.Date, self._DateTime)
        self.timeEditButton = DTPushButton(self, dt_qt.EDateTime.Time, self._DateTime)

        self.layout().addWidget(self.dateEditButton)
        self.layout().addWidget(self.timeEditButton)

        self._TE_Dialogue = TTimeEditDialog(self, self._DateTime.time())
        self._DE_Dialogue = TDateEditDialog(self, self._DateTime.date())

    def __set_styles(self):
        self.layout().setContentsMargins(
            0,          #Left
            0,          #Top
            0,          #Right
            0           #Bottom
            )
        self.setMinimumHeight(self.dateEditButton.sizeHint().height())
        self.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        #self.setStyleSheet(
        """TDateTimeEdit{
                border: 1px solid black;
                border-radius: 5px;
            }"""#)

    def __setup_connections(self):
        self.dateEditButton.clicked.connect(
            lambda: self._openDialogue(self._DE_Dialogue)
        )
        self.timeEditButton.clicked.connect(
            lambda: self._openDialogue(self._TE_Dialogue)
        )
        self._DE_Dialogue.dateSelected.connect(
            lambda date: self._closeDialogue(
                new_date=date)
        )
        self._TE_Dialogue.timeSelected.connect(
            lambda time: self._closeDialogue(
                new_time=time)
        )
        self._DE_Dialogue.rejected.connect(
            lambda: self.dateEditButton.setInactiveStyle()
        )
        self._TE_Dialogue.rejected.connect(
            lambda: self.timeEditButton.setInactiveStyle()
        )

    def _openDialogue(self, dialog: QDialog):
        dialog.show()

    def _closeDialogue(self,
                       new_date = QDate(), 
                       new_time = QTime(),
                       test_en=True):
        if (new_date != QDate()):
            if new_date < self._minimumDateTime.date():
                new_date = self._minimumDateTime.date()
            self._DateTime = QDateTime(new_date, self._DateTime.time())
        if (new_time != QTime()):   self._DateTime = QDateTime(self._DateTime.date(), (new_time))

        if (test_en): print(f"TDE_:{hex(id(self))}############\nCLOSED DIA; NEW DTE {self._DateTime}")

        self._updateButton(self.dateEditButton)
        self._updateButton(self.timeEditButton)
        
        self.dateTimeChanged.emit(self._DateTime)

    def _updateButton(self,
                      button: DTPushButton):
        button.setText(self._DateTime)
        button.setInactiveStyle()
        button.update()
    
    def _autoUpdateButton(self, test_en=False):
        if (test_en): print(self.dateEditButton.date())

        if (self.dateEditButton.date() < self._DateTime): self._updateButton(self.dateEditButton)
        if (self.timeEditButton.date() < self._DateTime): self._updateButton(self.timeEditButton)

    def _updateMaximumDateTime(self):
        #self._TE_Dialogue
        self._DE_Dialogue.setMaximumDate(self._maximumDateTime)

    def _updateMinimumDateTime(self, test_en=True):
        self._minimumDateTime = self._minimumDateTime.addSecs(10*60)

        if self._DateTime < self._minimumDateTime:
            self._DateTime = self._minimumDateTime.addSecs(10*60)

        self._TE_Dialogue.setMinimumTime(self._minimumDateTime.time())
        self._DE_Dialogue.setMinimumDate(self._minimumDateTime.date())

        if (test_en): print(f"TDE_:{hex(id(self))}############\nUPDATE MIN DT; NEW MIN DT {self._minimumDateTime}\nCUR DT: {self._DateTime}")
        self._autoUpdateButton()

    def _updateDateTime(self, test_en=True):
        self._TE_Dialogue.setCurrentTime(self._DateTime.time());           self._updateButton(self.timeEditButton)
        self._DE_Dialogue.setSelectedDate(self._DateTime.date());       self._updateButton(self.dateEditButton)

        if (test_en): print(f"TDE_:{hex(id(self))}############\nUPDATE CUR DT; NEW CUR DT {self._DateTime}")

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
    def maximumDateTime(self):      return self._maximumDateTime
    def maximumDate(self):          return self._maximumDateTime.date()
    def maximumTime(self):          return self._maximumDateTime.time()

    # Functions for returning dateTime
    @Property(QDateTime)
    def DateTime(self): return self._DateTime
        
    @DateTime.setter
    def DateTime(self, DateTime: QDate):
            if (self._DateTime != DateTime):
                self._DateTime = DateTime
                self._autoUpdateButton()
                self.dateTimeChanged.emit(self._DateTime)

    # Reimplemented paintEvent for advanced styling
    def paintEvent(self, pe):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
