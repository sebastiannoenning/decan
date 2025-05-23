import sys, math, re
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QEasingCurve, Slot, QPointF, Signal, QEvent, QObject, QSize
from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QWidget, QLabel, QCalendarWidget, QSpinBox, QStyle
from PySide6.QtWidgets import QSizePolicy, QToolButton, QMenu, QVBoxLayout, QStyleOption
from PySide6.QtGui import QFont, QIcon, QColor, QPainter, QTextCharFormat, QPalette, QPixmap

class DateSelect(QCalendarWidget):
    """
        More touch friendly variation of the QCalendarWidget. 'Replaces' year_QSpinBox with Prev & Next Year buttons
    """
    def __init__(self, parent, 
                 theme='light'):
        super().__init__(parent)
        self.theme=theme
        self.__setupUi()
        self.__setStyles()
        self.__setupConnections()

    def __setupUi(self):
        self.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setGridVisible(False)

        self._nav           : QWidget       = self.findChild(QWidget, "qt_calendar_navigationbar")    # Underlying widget
        self._header        : QHBoxLayout   = self.findChild(QHBoxLayout)                          # Header layout

        # All header buttons/subsets
        self._prevMonth     : QToolButton   = self._nav.findChild(QToolButton,"qt_calendar_prevmonth")
        self._nextMonth     : QToolButton   = self._nav.findChild(QToolButton,"qt_calendar_nextmonth")
        self._monthButton   : QToolButton   = self._nav.findChild(QToolButton, "qt_calendar_monthbutton")
        self._yearButton    : QToolButton   = self._nav.findChild(QToolButton, "qt_calendar_yearbutton")
        self._yearEdit      : QSpinBox      = self._nav.findChild(QSpinBox, "qt_calendar_yearedit")
        self._monthMenu     : QMenu         = self._monthButton.findChild(QMenu)
        self._monthMenu.setObjectName("qt_calendar_monthmenu")

        # Remove & hide all widgets from layout
        self._header.removeWidget(self._prevMonth),     self._prevMonth.hide()
        self._header.removeWidget(self._nextMonth),     self._nextMonth.hide()
        self._header.removeWidget(self._monthButton),   self._monthButton.hide()
        self._header.removeWidget(self._yearButton),    self._yearButton.hide()
        self._header.removeWidget(self._yearEdit),      self._yearEdit.hide()

        # Remove excess/unimportant spacers from layout
        for x in range(self._header.count()-1, -1, -1):
            spacer = self._header.takeAt(x)
            del spacer
        
        self._yearLabel                     = QLabel(self._nav, text=str(self._yearEdit.value()))
        self._nextYear                      = QPushButton(icon=QIcon(f":/icons/arrows/arrow_up_{self.theme}.svg"))
        self._prevYear                      = QPushButton(icon=QIcon(f":/icons/arrows/arrow_down_{self.theme}.svg")) 

        # Add new controls
        self._header.addWidget(self._nextYear),     self._nextYear.setObjectName("qt_calendar_nextyear")
        self._header.addWidget(self._prevYear),     self._prevYear.setObjectName("qt_calendar_prevyear")
        self._header.addWidget(self._yearLabel),    self._yearLabel.setObjectName("qt_calendar_yearlabel")
        # Re-add old controls
        self._monthButton.show(),                   self._header.addWidget(self._monthButton)
        self._prevMonth.show(),                     self._header.addWidget(self._prevMonth)
        self._nextMonth.show(),                     self._header.addWidget(self._nextMonth)

    def __setStyles(self):
        self.__setHeaderStyle()
        self.__setupCalendarStyle()

    def __setHeaderStyle(self):
        if (self.theme == 'light'): c, b = 255, 30
        else: c, b = 20, 255
        a = 1

        self._nav.setMaximumHeight(60)
        self._nav.setContentsMargins(0,0,0,0)
        self._header.setContentsMargins(0,0,0,0)

        self._nav.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self._yearLabel.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self._nextYear.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self._prevYear.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self._nextMonth.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self._prevMonth.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self._monthButton.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)

        self._nextYear.setMaximumWidth(50)
        self._prevYear.setMaximumWidth(50)
        self._nextMonth.setMaximumWidth(50)
        self._prevMonth.setMaximumWidth(50)

        date_font, month_font = QFont('Arial', 18), QFont('Arial', 16)
        self._yearLabel.setFont(date_font)
        self._yearLabel.setContentsMargins(2,0,2,0)
        self._yearLabel.setAutoFillBackground(True)
        self._monthButton.setFont(date_font)
        self._monthButton.setContentsMargins(2,0,2,0)
        self._monthMenu.setFont(month_font)

        left_arrow, right_arrow, up_arrow, down_arrow = QIcon(), QIcon(), QIcon(), QIcon()
        left_arrow.addFile(f":/icons/arrows/arrow_left_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        left_arrow.addFile(f":/icons/arrows/arrow_left_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        right_arrow.addFile(f":/icons/arrows/arrow_right_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        right_arrow.addFile(f":/icons/arrows/arrow_right_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        up_arrow.addFile(f":/icons/arrows/arrow_up_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        up_arrow.addFile(f":/icons/arrows/arrow_up_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        down_arrow.addFile(f":/icons/arrows/arrow_down_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        down_arrow.addFile(f":/icons/arrows/arrow_down_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)

        self._nextMonth.setIcon(right_arrow),       self._nextMonth.setIconSize(QSize(23,23))
        self._prevMonth.setIcon(left_arrow),        self._prevMonth.setIconSize(QSize(23,23))
        self._nextYear.setIcon(up_arrow),           self._nextYear.setIconSize(QSize(23,23))
        self._prevYear.setIcon(down_arrow),         self._prevYear.setIconSize(QSize(23,23))

        string = f"""

#qt_calendar_navigationbar {{
    background-color: rgba({c}, {c}, {c}, {a});
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}}                     

#qt_calendar_navigationbar * {{
    border-left: 1px solid rgba({b}, {b}, {b}, {a});
}}

/*#################### YEAR BUTTONS ####################*/

QPushButton#qt_calendar_nextyear {{
    border-top-left-radius: 4px;
    border: none;
}}

QPushButton#qt_calendar_prevyear {{
    border-radius: 0px;
}}
                           
QPushButton:pressed {{
    /* Pressed state */
    background-color: rgba(90, 90, 90, {a});
}}

QLabel#qt_calendar_yearlabel {{
    padding-left: 8px;
    padding-right: 8px;
    color: rgba({b}, {b}, {b}, {a});
    background-color: rgba({c}, {c}, {c}, {a});
    border-right: 1px solid rgba({b}, {b}, {b}, {a});
}}

/*#################### MONTH BUTTONS ####################*/

QToolButton#qt_calendar_monthbutton {{
    padding: 4px;
    background-color: rgba({c}, {c}, {c}, {a});
    color: rgba({b}, {b}, {b}, {a});
    border: none;
}}

#qt_calendar_monthbutton * {{
    border: none;
    color: rgba({b}, {b}, {b}, {a});
}}

QToolButton#qt_calendar_monthbutton::menu-indicator {{
    image: url(":/icons/arrows/arrow_down_{self.theme}.svg");
    subcontrol-origin: padding;
    subcontrol-position: bottom left;
    width: 23px;
    height: 23px;
}}

QToolButton#qt_calendar_monthbutton::menu-indicator:pressed {{
    image: url(":/icons/arrows/arrow_down_red.svg");
}}

QMenu#qt_calendar_monthmenu {{
    background-color: rgba({c}, {c}, {c}, 0.5);
    padding-top: 0px;
    padding-bottom: 0px;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
}}

QMenu#qt_calendar_monthmenu::item {{
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 4px;
    padding-bottom: 4px;
    border-bottom: 1px solid rgba({b}, {b}, {b}, {a});
}}

QMenu#qt_calendar_monthmenu::item:selected {{
    background: rgba(255, 80, 80, 0.7);
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
}}

QMenu#qt_calendar_monthmenu::item:disabled {{
    color: rgba(90, 90, 90, 0.9);
}}

QToolButton#qt_calendar_prevmonth {{
    /* Base state */
    border-radius: 0px;
}}

QToolButton#qt_calendar_nextmonth {{
    /* Base state */
    border-radius: 0px;
    border-top-right-radius: 4px;
}}

QToolButton:pressed {{
    background-color: rgba(90, 90, 90, {a});
}}
"""
        
    def __setupCalendarStyle(self):
        if (self.theme == 'light'): c, b = 255, 30
        else: c, b = 20, 255
        a = 1

        self.setFont(QFont('Arial', 15))

        self.setFirstDayOfWeek(Qt.DayOfWeek.Sunday)
        self.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)

        weekend_text = QTextCharFormat()
        weekend_text.setFont(QFont('Arial',15))
        weekend_text.setFontCapitalization(QFont.Capitalization.AllUppercase)
        weekend_text.setForeground(QColor(255, 80, 80, 255))

        weekday_text = QTextCharFormat(weekend_text)
        weekday_text.setForeground(QColor(c, c, c, 255))
        weekday_text.setBackground(QColor(b, b, b, 255))

        self.setHeaderTextFormat(weekday_text)
        self.setWeekdayTextFormat(Qt.DayOfWeek.Saturday, weekend_text)
        self.setWeekdayTextFormat(Qt.DayOfWeek.Sunday, weekend_text)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor(c, c, c))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(255, 80, 80))

        palette.setColor(QPalette.ColorRole.Text, QColor(b, b, b))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(100, 100, 100))

        self.setPalette(palette)

    def __setupConnections(self):
        self._nextYear.clicked.connect(lambda: self._stepUpYearEdit())
        self._prevYear.clicked.connect(lambda: self._stepDownYearEdit())
        self._yearEdit.valueChanged.connect(lambda value: self._updateYearComponents(value))

    def setMinimumDate(self, date):
        if (self.selectedDate().year() < date.year()): self._yearEdit.valueChanged.emit()
        super().setMinimumDate(date)
    
    def setMaximumDate(self, date):
        if (self.selectedDate().year() > date.year()): self._yearEdit.valueChanged.emit()
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
        self._yearEdit.hide(), self._yearButton.hide()

    def _stepDownYearEdit(self): 
        """ Private access function. Manually changes yearEdit spinbox via stepDown, emits a editingFinished
            signal & updates the yearLabel text to match the current yearEdit.value() """
        self._yearEdit.stepDown(), self._yearEdit.editingFinished.emit()
        self._yearEdit.hide(), self._yearButton.hide()

    def _updateYearComponents(self, value):
        """ Private access function. As _yearLabel is dependent on changes passed to the internal spinbox, 
            and the _prev & _next year buttons need to not exceed date bounds, this function is ran everytime
            the value is changed."""
        self._yearLabel.setText(str(value))
        if (value == self.minimumDate().year()): self._prevYear.setDisabled(True)
        elif (value == self.maximumDate().year()): self._nextYear.setDisabled(True)
        else:
            if (self._prevYear.isEnabled() != True): self._prevYear.setDisabled(False)
            if (self._nextYear.isEnabled() != True): self._nextYear.setDisabled(False)

class TDateEditDialog(QDialog):

    dateSelected = Signal(QDate)

    def __init__(self, parent, 
                 cur_Date: QDate):
        super().__init__(parent)
        self._Date = cur_Date
        self.__setupUi()
        self.__setupStyles()
        self.__setupConnections()

    def __setupUi(self):
        self.setObjectName("datetime_dialog")
        self._layer_base = QVBoxLayout(self)          
        self._dateSelect = DateSelect(self, theme='dark')
        self._dateSelect.setSelectedDate(self._Date)
        self._layer_base.addWidget(self._dateSelect)

        self._footer_container = QWidget(self)
        self._layer1_footer = QHBoxLayout(self._footer_container)                            
        
        
        self.confirmPushButton = QPushButton(parent=self, text='Confirm')
        self.cancelPushButton = QPushButton(parent=self, text='Cancel')
        self._layer1_footer.addWidget(self.confirmPushButton)
        self._layer1_footer.addWidget(self.cancelPushButton)

        self._layer_base.addWidget(self._footer_container)

        self._layer_base.setObjectName("datetime_dialog_layout_base")
        self._dateSelect.setObjectName("datetime_dialog_dateselect")
        self._layer1_footer.setObjectName("datetime_dialog_layout_footer")
        self.confirmPushButton.setObjectName("datetime_dialog_confirm_pushbutton")
        self.cancelPushButton.setObjectName("datetime_dialog_cancel_pushbutton")

    def __setupStyles(self):
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)
        self.setMinimumSize(500, 400)

        self.layout().setContentsMargins(0,0,0,0)
        self._layer1_footer.setContentsMargins(0,0,0,0)
    
        self.layout().setSpacing(0)
        self._layer1_footer.setSpacing(0)

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.confirmPushButton.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.cancelPushButton.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        
        self.confirmPushButton.setMaximumHeight(40)
        self.cancelPushButton.setMaximumHeight(40)
        self._footer_container.setMaximumHeight(40)

        self.confirmPushButton.setFont(QFont("Arial", 18))
        self.cancelPushButton.setFont(QFont("Arial", 18))

        self._footer_container.setStyleSheet(f"""

#datetime_dialog {{
    border-radius: 4px
}}  

/*#################### DIALOG BUTTONS ####################*/
                           
QPushButton#datetime_dialog_confirm_pushbutton, QPushButton#datetime_dialog_cancel_pushbutton {{
    background-color: rgba(30, 30, 30, 1);
    border: none;
    border-radius: 0px;
}}

QPushButton#datetime_dialog_confirm_pushbutton {{
    border-bottom-left-radius: 4px;
    border: none;
}}

QPushButton#datetime_dialog_cancel_pushbutton {{
    border-bottom-right-radius: 4px;
    border-left: 1px solid rgba(100,100,100,1)
}}
                           
QPushButton#datetime_dialog_confirm_pushbutton:pressed {{
    /* Pressed state */
    background: rgba(140, 255, 140, 1);
}}
                           
QPushButton#datetime_dialog_cancel_pushbutton:pressed {{
    /* Pressed state */
    background: rgba(255, 80, 80, 1);
}}
""")
        
    def __setupConnections(self):
        self.confirmPushButton.clicked.connect(lambda: self.dialogueAccepted())
        self.cancelPushButton.clicked.connect(lambda: self.dialogueRejected())

    def dialogueAccepted(self): self.dateSelected.emit(self._dateSelect.selectedDate()), self.accept()
    def dialogueRejected(self): self.reject(), self.rejected.emit()

    # Setters for DateSelect Object values
    def setMinimumDate(self, date: QDate):      self._dateSelect.setMinimumDate(date)
    def setMaximumDate(self, date: QDate):      self._dateSelect.setMaximumDate(date)
    def setSelectedDate(self, date: QDate):     self._dateSelect.setSelectedDate(date)
    def clearMinimumDate(self):                 self._dateSelect.clearMinimumDate()
    def clearMaximumDate(self):                 self._dateSelect.clearMaximumDate()
    # Getters for DateSelect Object values
    def minimumDate(self):                      return self._dateSelect.minimumDate()
    def maximumDate(self):                      return self._dateSelect.maximumDate()
    def selectedDate(self):                     return self._dateSelect.selectedDate()
    def yearShown(self):                        return self._dateSelect.yearShown()
    def dateSelect(self):                       return self._dateSelect
