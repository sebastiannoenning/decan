import sys, math, re
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QEasingCurve, Slot, QPointF
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy, QStyleOption, QStyle, QCalendarWidget
from PySide6.QtGui import QFont, QPainter

class DateTime(Enum):
    Date = 0
    Time = 1

class DTPushButton(QLabel):
    clicked = Signal()

    def __init__(self, parent, 
                 type = DateTime.Date,
                 dateTime = QDateTime(QDate(0,0,0),QTime(0,0)),
                 format = 'd MMM yyyy'):
        super().__init__(parent)
        self._eventPressed = False # Flag
        self._dateTime = dateTime
        self._format = format
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
        if (color == 'red'): color = 'rgba(245, 90, 40, 1)'
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
        if isinstance(dateTime, QDateTime): self._dateTime = dateTime
        if (self._type == DateTime.Date): string = self._dateTime.date().toString(self._format)
        else: string = self._dateTime.time().toString("HH:mm") #"HH:mm a")
        self.adjustSize()
        super().setText(string)

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

class TDateTimeEdit(QWidget):
    """ Base class for opening QCalendar & TDateTimeEdit
    """
    dateTimeChanged = Signal()
    dateChanged = Signal()
    timeChanged = Signal()

    def __init__(self, parent, 
                 dateTime = QDateTime()):
        super().__init__(parent)
        self._minimumDateTime = QDateTime()
        self._dateTime = dateTime
        self._maximumDateTime = QDateTime()
        self.__setup_ui()
        self.__setup_connections()
    
    def __setup_ui(self):
        self._button_container = QHBoxLayout(self)
        self.setLayout(self._button_container)

        self._dateEdit_pushButton = DTPushButton(self, DateTime.Date, QDateTime(QDate(1920,11,9),QTime(2,3,1,0)))
        self._timeEdit_pushButton = DTPushButton(self, DateTime.Time, QDateTime(QDate(1920,11,9),QTime(2,3,1,0)))

        self.layout().addWidget(self._dateEdit_pushButton)
        self.layout().addWidget(self._timeEdit_pushButton)
        self._button_container.addStretch(1)

        self._timeEdit_editDialog = None
        self._dateEdit_editDialog = None

        self.__set_styles()

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
            lambda: print('date clicked!')
        )
        self._timeEdit_pushButton.clicked.connect(
            lambda: print('time clicked!')
        )

    def _updateMaximumDateTime(self):
        self._timeEdit_editDialog()
        self._dateEdit_editDialog()

    def _updateMinimumDateTime(self):
        self._timeEdit_editDialog()
        self._dateEdit_editDialog()

    # Setters for both minimumDateTime & maximumDateTime
    def setDateRange(self, min: QDate, max: QDate): self._minimumDateTime.setDate(min), self._maximumDateTime.setDate(max)
    def setDateTimeRange(self, min: QDateTime, max: QDateTime): self._minimumDateTime, self._maximumDateTime = min, max

    # Setters for _minimumDateTime
    def setMinimumDateTime(self, datetime: QDateTime): self._minimumDateTime = datetime, self._updateMinimumDateTime()
    def setMinimumDate(self, date: QDate): self._minimumDateTime.setDate(date), self._updateMinimumDateTime()
    def setMinimumTime(self, time: QTime): self._minimumDateTime.setTime(time), self._updateMinimumDateTime()
    # Functions for clearing _minimumDateTime
    def clearMinimumDateTime(self): self._minimumDateTime = QDateTime(), self._updateMinimumDateTime()
    def clearMinimumDate(self): self._minimumDateTime.setDate(QDate()), self._updateMinimumDateTime()
    def clearMinimumTime(self): self._minimumDateTime.setTime(QTime()), self._updateMinimumDateTime()
    # Getters for _minimumDateTime
    def minimumDateTime(self): return self._minimumDateTime
    def minimumDate(self): return self._minimumDateTime.date()
    def minimumTime(self): return self._minimumDateTime.time()

    # Setters for _maximumDateTime
    def setMaximumDateTime(self, datetime: QDateTime): self._maximumDateTime = datetime, self._updateMaximumDateTime()
    def setMaximumDate(self, date: QDate): self._maximumDateTime.setDate(date), self._updateMaximumDateTime()
    def setMaximumTime(self, time: QTime): self._maximumDateTime.setTime(time), self._updateMaximumDateTime()
    # Functions for clearing _maximumDateTime
    def clearMaximumDateTime(self): self._maximumDateTime = QDateTime(), self._updateMaximumDateTime()
    def clearMaximumDate(self): self._maximumDateTime.setDate(QDate()), self._updateMaximumDateTime()
    def clearMaximumTime(self): self._maximumDateTime.setTime(QTime()), self._updateMaximumDateTime()
    # Getters for _maximumDateTime
    def maximumDateTime(self): return self._maximumDateTime()
    def maximumDate(self): return self._maximumDateTime.date()
    def maximumTime(self): return self._maximumDateTime.time()

    # Functions for returning dateTime
    def dateTime(self): return self._dateTime
    def date(self): return self._dateTime.date()
    def time(self): return self._dateTime.time()

    # Reimplemented paintEvent for advanced styling
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
