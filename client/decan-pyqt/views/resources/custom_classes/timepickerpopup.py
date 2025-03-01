import sys, math
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QEasingCurve, Slot
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties
from PySide6.QtGui import QFont, QMouseEvent, QPainter

class TimeType(Enum):
    Hours = 1
    SimpleMinutes = 2
    DetailedMinutes = 3

class TimeSelect(QWidget):
    "WidgetContents"
    def __init__(self, parent, Type: TimeType, entries=24, locked=0):
        super().__init__(parent)
        self.entries = entries      #Number of options
        self.locked = locked        #Used to 
        self._period = 0            #Size of total widget
        self._mult = 1              #Conversion value for SimpleMinutes → only used in conj. with __approxFunc to convert to interval values
        
        if Type != None: self.type = Type

        self.labels = dict()

        if (Type == TimeType.SimpleMinutes): 
            self.entries /= 2
            self._mult *= 5
        elif (Type == TimeType.DetailedMinutes):
            self.entries = (self.entries*2)+1
        self.__setup_ui()

    def __approxFunc(self, x, P, A, O=0):
        """ A function for calculating the current scrollerStateChanged/entry of the infinite scroll area
            #   Based on function 'f(x) = (x mod P) ÷ (P ÷ A)' 
            #   Where P is Period, & A is Amplitude
            #   O is optional for removing early values from approximation (for instance, setting minimum time)

            Example use in code: 
                return __approxFunc(x, self.period, self.entries)
        """
        return ((x % P) / ( P /(A - O))) + O
    
    def returnCurrentVal(self, offset):
        """ Public access function for calculating the current value based on the position of the QScrollBar/QScroller
            #   Re-uses the __approxFunc function, with the period being substituted as the actual size of the container.
            #   ↪   'offset' is named as such, since the given value will typically add the final position of the scrollbar
                        and the offset (the middle of the visible scrollArea portion) together.
        """
        return self._mult * math.trunc(self.__approxFunc(offset, self.period, self.entries, self.locked))
    
    def returnStartValue(self, pagestep):
        offset = pagestep/2
        interval = (self.sizeHint().height()-pagestep)/(len(self.labels)-math.ceil())
        st_val = (
            ((round(offset / interval)      # Find central-most label
            * interval)                     # Subsequently find starting x for label
            + (interval / 2))               # Add 0.5 * label's calculated area to find center
            - offset                        # Subtract by the center/offset of the visible container
        )                                   # This will return the minute offset starting value for 'setSnapPositionY'
        alt_func = (

        )
        print("StartValue: ",st_val,"\nAltFunc: ",alt_func,"\nInterval: ",interval,"\nLabels no.: ",len(self.labels))
        return alt_func, interval 

    def __setup_ui(self):
        labelContainer = QVBoxLayout(self)
        """ Adds all labels to the interface.
            #   Uses __approxFunc to fill list with 2 sets of the value range
            #   ↪   i.e, for Hours: fills labelContainer with 0-23 twice
            #       i.e, for SimpleMinutes: fills labelContainer with 0-55 twice
            #       i.e, for DetailedMinutes: fills labelContainer with 0-59 twice 
        """
        for x in range(round((self.entries-self.locked)*2)):
            val = round(self.__approxFunc(x, self.entries, self.entries, self.locked)*self._mult)
            self.labels[x] = QLabel(f"{val:02}", self)
            self.labels[x].setObjectName(f"TM_{self.objectName}_Type_{self.type}_Pos_{x}_Val_{val:02}")
            labelContainer.addWidget(self.labels[x])
        
        self.period = round(self.sizeHint().height()/2)

class TimePickerPopup(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.minimumDateTime = QDateTime()
        self.currentDateTime = QDateTime()

        self.hours = 0
        self.minutes = 0

        self.__setup_ui()
        self.__setup_connections()

    def __setup_ui(self):
        self.setWindowTitle("timePickerPopup")
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint) #sets Window to clear
        #self.setWindowModality(Qt.WindowModality.ApplicationModal) #sets Dialog to override other 

        self.layer1_times = QHBoxLayout(self)   #   Horizontal box layout for time selects

        self.hours_scrollArea = QScrollArea(self)
        self.hours_scrollArea.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        self.hours_scrollArea.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}")
        self.hours_timeSelect = TimeSelect(self, TimeType.Hours)
        self.hours_scrollArea.setWidget(self.hours_timeSelect)
        self.hours_timeScroller = QScroller.scroller(self.hours_scrollArea.viewport())
        self.hours_timeScroller.grabGesture(
            self.hours_scrollArea.viewport(),
            QScroller.ScrollerGestureType.LeftMouseButtonGesture
        )

        self.mins_scrollArea = QScrollArea(self)
        self.mins_scrollArea.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        self.mins_scrollArea.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}")
        self.mins_timeSelect = TimeSelect(self, TimeType.SimpleMinutes)
        self.mins_scrollArea.setWidget(self.mins_timeSelect)
        self.mins_timeScroller = QScroller.scroller(self.mins_scrollArea.viewport())
        self.mins_timeScroller.grabGesture(
            self.mins_scrollArea.viewport(),
            QScroller.ScrollerGestureType.LeftMouseButtonGesture
        )

        self.layer1_times.addWidget(self.hours_scrollArea)
        self.layer1_times.addWidget(self.mins_scrollArea)

    def __setup_connections(self):
        self.hours = self.hours_timeScroller.stateChanged.connect(
            lambda state: 
            self.scrollerStateChanged(
                state,
                self.hours_timeSelect,
                int(
                    self.hours_timeScroller.finalPosition().y() + 
                    (self.hours_scrollArea.verticalScrollBar().pageStep()/2)
                )
                ))
        self.mins = self.mins_timeScroller.stateChanged.connect(
            lambda state: 
            self.scrollerStateChanged(
                state,
                self.mins_timeSelect,
                int(
                    self.mins_timeScroller.finalPosition().y() +
                    (self.mins_scrollArea.verticalScrollBar().pageStep()/2)
                )
                ))
        
        self.hours_scrollArea.verticalScrollBar().valueChanged.connect(
            lambda value: 
            self.scrollBarPosition(
                value,
                self.hours_scrollArea,
                self.hours_timeScroller.finalPosition()
                ))
        self.mins_scrollArea.verticalScrollBar().valueChanged.connect(
            lambda value: 
            self.scrollBarPosition(
                value,
                self.mins_scrollArea,
                self.mins_timeScroller.finalPosition()
                ))

    @Slot(QScroller.State)
    #Calculate end-value of the timepicker
    def scrollerStateChanged(self, state, timeSelect: TimeSelect, offset):
        if (state == QScroller.State.Inactive):
            print("Calculated central value: ", timeSelect.returnCurrentVal(offset))
            return timeSelect.returnCurrentVal(offset)
        else: 
            return None

    #Teleport scroller to center if it reaches a low value
    def scrollBarPosition(self, value, scrollArea: QScrollArea, finalPosition):
        print(value)
        print(scrollArea.verticalScrollBar().maximum(),
              "/",
              (scrollArea.verticalScrollBar().maximum()+scrollArea.verticalScrollBar().pageStep()))
    
    def resizeEvent(self, event):
        """h_s, h_i = self.hours_timeSelect.returnStartValue(self.hours_scrollArea.verticalScrollBar().pageStep())
        self.hours_timeScroller.setSnapPositionsY(h_s, h_i)
        self.hours_scrollArea.verticalScrollBar().setValue(h_s)
        m_s, m_i = self.mins_timeSelect.returnStartValue(self.mins_scrollArea.verticalScrollBar().pageStep())
        self.mins_timeScroller.setSnapPositionsY(m_s, m_i)
        self.mins_scrollArea.verticalScrollBar().setValue(m_s)"""
        super().resizeEvent(event)
        
    
"""#Abandoned; Cant subclass QScroller
class TimeScroller(QScroller): 
    def __init__(self, parent, connect: TimePickerPopup):
        super().__init__(parent)
        self.grabGesture(parent.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture())
        self._setup_properties()

    def _setup_properties(self):
        properties = self.scrollerProperties()

        properties.setScrollMetric(                                   
            QScrollerProperties.ScrollMetric.VerticalOvershootPolicy, 1)  
        properties.setScrollMetric(                                
            QScrollerProperties.ScrollMetric.HorizontalOvershootPolicy, 1)
        properties.setScrollMetric(                                      
            QScrollerProperties.ScrollMetric.AxisLockThreshold, 1)
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.ScrollingCurve, QEasingCurve(QEasingCurve.Type.OutExpo))
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.DecelerationFactor, 0.05)
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.MaximumVelocity, 0.635)
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.OvershootDragResistanceFactor, 0.33)
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.OvershootScrollDistanceFactor, 0.33)
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.SnapscrollerStateChangedRatio, 0.93)
        properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.DragStartDistance, 0.001)

        self.setScrollerProperties(properties)
                 
    
    def InputRelease():
        print("hello")""" #Not intended to be subclassed, will use the signal slots instead