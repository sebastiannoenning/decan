import sys, math
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QEasingCurve, Slot, QPointF
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties
from PySide6.QtGui import QFont, QMouseEvent, QPainter

class TimeType(Enum):
    Hours = 1
    SimpleMinutes = 2
    DetailedMinutes = 3

class TimeSelect(QWidget):

    """A "TimeSelect" widget with a predetermined number of labels, signifying time.

    Variables:
        type:       TimeType, custom Enum which will influence entries, _repeats, _mult, and consequently _period
        entries:    Number of options (i.e, 0-23, 0-55, 0-59) 
        locked:     Adds omitting options for __approxFunc
        labels:     Python Dictionary storing references to labels, can refer to specific values via labels[n]
        _repeats:   Amount of times the number of entries are repeated during generation
        _mult:      Multiplier for conversion to SimpleMinutes/5 minute intervals
        _period:    Total size of widget divided by number of repeated values inside of it

    Functions:

    """
    def __init__(self, parent, Type: TimeType, entries=24, locked=0):
        super().__init__(parent)
        self.entries = entries  
        self.locked = locked       
        self._period = 0         
        self._mult = 1          
        self._repeats = 2 
        
        try: self.type = Type
        except: self.type = TimeType.Hours

        self.labels = dict()

        #Adjust variables based on chanegs to TimeType
        if (Type == TimeType.SimpleMinutes): 
            self.entries /= 2
            self._repeats = 4
            self._mult *= 5
        elif (Type == TimeType.DetailedMinutes):
            self.entries = (self.entries*2)+1
        
        self.__setup_ui()

    def __approxFunc(self, x, P, A, O=0):
        """ A function for calculating the current finalTimeValue/entry of the infinite scroll area
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
        """ Public access function for use with QScroller.setSnapPositionsY()
            ↪   In the context of TimePopupDialog, will be called in a overrode resizeEvent(), as the pagestep (i.e, visible
                area of the QScrollArea) will shift with alternating sizes to the overarching window. Thus the quantity of
                visible labels will change & so will the leading values associated with them. The function is wrote in a way
                that it accounts for all possible variables when calculating the labels, their distance, and quantity of them
                in a TimeSelect.

            ### QScroller.setSnapPositionsY(first: qreal, interval: qreal)
            #   Using the above form for the initialisation, rather than passing a list of all known valid snappable locations
            #       'first':    The starting position
            #       'interval': The distance between it & succeeding entries. Assumes uniform snapping distance (valid here)
            #       qreal:      PyQt Typedef equivalent for doubles/floats 

            ### Variables outline:
            #       'offset':   Value indicating 'central-y'.
            #                   ↪   pagestep indicates the visible containers size, so halving it will indicate central-y value
            #                       Not rounded as setSnapPositions is compatible with float datatype.
            #       'interval': Value for use with setSnapPositionsY()
            #                   ↪   Takes the overall size of the container & divides it by the no. of labels present to assume
            #                       distance between labels. Rounded as pixels are absolute values and decimals cause misalign-
            #                       -ment between values if kept in the interval
            #       'f_label':  Value for dictating the initial snappable label in the container. 
            #                   ↪   Labels are stored via a dictionary 'self.labels[]', so can be passed along knowing the first
            #                       valid label without manually calculating it via a while-loop. Rounds upwards.
            #       'st_val':   Value for use with setSnapPositionsY()
            #                   ↪   Uses the y position of the f_label (in relation to the TimeSelect QWidget's own space),
            #                       adds the label's height divided by half (to offset it more centrally), and then subtracts
            #                       the float offset to determine the starting location.
        """
        offset = pagestep / 2
        interval = math.floor(self.sizeHint().height() / len(self.labels))
        f_label = math.ceil(offset / interval) #No. for self.labels[n] indicating first snappable label in container
        st_val = (
            (self.labels[f_label].pos().y()) 
            + (self.labels[f_label].sizeHint().height() / 2)
            - (offset)
        )
        return st_val, interval
    
    def returnCentralValue(self, pagestep):
        m_label, offset = (round(len(self.labels) / 2)), (pagestep / 2) # Middle Label & Offset
        return (
            self.labels[m_label].pos().y()
            + (self.labels[m_label].sizeHint().height() / 2)
            - (offset)
            )
    
    def returnUpperLowerBounds(self, pagestep):
        b_label, t_label, offset = (round(len(self.labels) / 4)), 3*(round(len(self.labels) / 4)), (pagestep/2)
        return (
            self.labels[b_label].pos().y()
            + (self.labels[b_label].sizeHint().height() / 2)
            - (offset)
            ),(
            self.labels[t_label].pos().y()
            + (self.labels[t_label].sizeHint().height() / 2)
            - (offset)
            )
    
    def returnInterval(self):
        return round(self.sizeHint().height() / len(self.labels))

    def __setup_ui(self):
        labelContainer = QVBoxLayout(self)
        """ Adds all labels to the interface.
            #   Uses __approxFunc to fill list with 2 sets of the value range
            #   ↪   i.e, for Hours: fills labelContainer with 0-23 twice
            #       i.e, for SimpleMinutes: fills labelContainer with 0-55 four times (i.e, 12*4 vals)
            #       i.e, for DetailedMinutes: fills labelContainer with 0-59 twice 
        """
        for x in range(round((self.entries-self.locked)*self._repeats)):
            val = round(self.__approxFunc(x, self.entries, self.entries, self.locked)*self._mult)
            self.labels[x] = QLabel(f"{val:02}", self)
            self.labels[x].setObjectName(f"TM_{self.objectName}_Type_{self.type}_Pos_{x}_Val_{val:02}")
            labelContainer.addWidget(self.labels[x])
        
        self.period = round(self.sizeHint().height()/self._repeats)

class TimePickerPopup(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.minimumDateTime = QDateTime()
        self.currentDateTime = QDateTime()

        self.hours = 0
        self.minutes = 0

        self.function_lock = False
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
        self.hours_timeScroller = self.__create_drag_scroller(self.hours_scrollArea)

        self.mins_scrollArea = QScrollArea(self)
        self.mins_scrollArea.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        self.mins_scrollArea.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}")
        self.mins_timeSelect = TimeSelect(self, TimeType.SimpleMinutes)
        self.mins_scrollArea.setWidget(self.mins_timeSelect)
        self.mins_timeScroller = self.__create_drag_scroller(self.mins_scrollArea)

        self.layer1_times.addWidget(self.hours_scrollArea)
        self.layer1_times.addWidget(self.mins_scrollArea)

    def __setup_connections(self):
        self.hours = self.hours_timeScroller.stateChanged.connect(
            lambda state: 
            self.finalTimeValue(
                state,
                self.hours_timeSelect,
                int(
                    self.hours_timeScroller.finalPosition().y() + 
                    (self.hours_scrollArea.verticalScrollBar().pageStep()/2)
                )
                ))
        self.mins = self.mins_timeScroller.stateChanged.connect(
            lambda state: 
            self.finalTimeValue(
                state,
                self.mins_timeSelect,
                int(
                    self.mins_timeScroller.finalPosition().y() +
                    (self.mins_scrollArea.verticalScrollBar().pageStep()/2)
                )
                ))
        
        self.hours_scrollArea.verticalScrollBar().valueChanged.connect(
            lambda value: 
            self.infiniteScroll(
                value,
                self.hours_scrollArea,
                self.hours_timeScroller,
                self.hours_timeSelect
                ))
        self.mins_scrollArea.verticalScrollBar().valueChanged.connect(
            lambda value: 
            self.infiniteScroll(
                value,
                self.mins_scrollArea,
                self.mins_timeScroller,
                self.mins_timeSelect
                ))
        
    def __create_drag_scroller(self, viewport: QScrollArea):
        #   Create properties profile
        new_scroll = QScroller.scroller(viewport.viewport())
        new_scroll.grabGesture(
            viewport.viewport(), 
            QScroller.ScrollerGestureType.LeftMouseButtonGesture
            )

        #   Set alternate properties profile to default
        new_properties = new_scroll.scrollerProperties()    # Copy default properties

        new_properties.setScrollMetric(                                   
            QScrollerProperties.ScrollMetric.VerticalOvershootPolicy, 1)  
        new_properties.setScrollMetric(                                
            QScrollerProperties.ScrollMetric.HorizontalOvershootPolicy, 1)
        new_properties.setScrollMetric(                                      
            QScrollerProperties.ScrollMetric.AxisLockThreshold, 1)
        
        new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.ScrollingCurve, QEasingCurve(QEasingCurve.Type.Linear))
        new_properties.setScrollMetric( #DecelerationFactor is a percentage decrease of velocity every frame
            QScrollerProperties.ScrollMetric.DecelerationFactor, 0.05) #I.e, around 5% each frame
        new_properties.setScrollMetric( # at 60 frames per second
            QScrollerProperties.ScrollMetric.FrameRate, QScrollerProperties.FrameRates.Fps60)
        new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.MaximumVelocity, 0.635)
        
        new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.SnapPositionRatio,0.33)
        """new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.SnapTime())"""

        new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.OvershootDragResistanceFactor, 0.33)
        new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.OvershootScrollDistanceFactor, 0.33)
        
        new_properties.setScrollMetric(
            QScrollerProperties.ScrollMetric.DragStartDistance, 0.001)
        
        new_scroll.setScrollerProperties(new_properties)    #Set scroller properties to profile
        return new_scroll

    @Slot(QScroller.State)
    #Calculate end-value of the timepicker
    def finalTimeValue(self, state, timeSelect: TimeSelect, offset):
        #print("State: ",state)
        if (state == QScroller.State.Inactive):
            print("Calculated central value: ", timeSelect.returnCurrentVal(offset))
            return timeSelect.returnCurrentVal(offset)
        else: 
            return None

    #Shift scrollArea().verticalScrollBar() to a new value if exceeding a bound
    def infiniteScroll(self, value, qScrollArea: QScrollArea, qScroller: QScroller, timeSelect: TimeSelect):
        l_bound, u_bound = timeSelect.returnUpperLowerBounds(qScrollArea.verticalScrollBar().pageStep())
        interval = timeSelect.returnInterval()
        #Prevent repeated calls --> for instance, if Dragging hits a bound, it repeatedly calls which causes undesired behaviour
        if ((l_bound - (2 * interval)) <= value) & (value <= (u_bound + (2 * interval))): self.function_lock = False

        if (value < (l_bound - (2 * interval))) & (self.function_lock == False):
            self.function_lock = True
            try:
                shift = u_bound - (2 * interval)
                self._shiftScroll(shift, value, qScroller, qScrollArea, "lower")
                self.function_lock = False
            except Exception as e:
                print("###Infinite Scroll Error: ",e)
                self.function_lock = False

        if (value > (u_bound + (2 * interval))) & (self.function_lock == False):
            self.function_lock = True
            try:
                shift = l_bound + (2 * interval)
                self._shiftScroll(shift, value, qScroller, qScrollArea, "upper")
                self.function_lock = False
            except Exception as e:
                print("### Shift Scroll Error: ",e)
                self.function_lock = False

    def _shiftScroll(self, shift, value, qScroller: QScroller, qScrollArea: QScrollArea, bound="undef", test_en=False):
        """ Private access function for use with self.infiniteScroll()
            ↪   Takes all values passed to the valueChanged Slot & shifts it via the amount specified by the caller.
                Additionally, handles all types of QScroller.States at the moment of shifting, ensuring continuation
                of Dragging movements & seamless animations for those in motion/scrolling

                Additional notes: Was initially packaged in self.infiniteScroll(), but migrated to a secondary func-
                -tion as both upper and lower bounds functioned identically outside of the value passed to the shift.

            Variable outline:
                'shift':    Shift is the new verticalScrollBar position that'll be set post call. Shift is generally
                            an upper or lower bound, inclined inwards (towards the central value) so that it doesn't
                            overlap with the 'real bound'. Bounds edges are 2 entries outwards, and shifted values
                            are the opposite bound 2 entries inwards.

                'value':    The function calling this (infiniteScroll()) is linked to a signal slot connection for
                            verticalScrollBar listed 'valueChanged'. The value in this instance is the value passed
                            from aforementioned signal slot connection. Despite this, this function is only called
                            when the scrollbar has exceeded acceptible bounds (due to the function_lock variable and
                            general design of infiniteScroll())

                'bound':    Str value containing a name for which bound called the function. 
                            Purely for testing purposes, and this function can be called without it.

                'test_en':  Shorthand for "testing enabled", enables printing to the terminal for testing purposes.
                            Used this mostly to check maths for deltas' and see if scrollTo was functioning.

            Object outline:
                'qScroller':    qScroller passes a reference to the connected QScroller. Necessary for reading
                                qScroller.state and using that information to handle the shift. 

                'qScrollArea':  qScrollArea passes a reference to the connected QScrollArea. Used in lieu of a more
                                complicated & visibly rough qScroller.scrollTo() movement of the QScrollArea. 
        """
        state = qScroller.state()
        if test_en==True: print(f'Exceeds {bound} bound | Mode: ',state)
        if (state == QScroller.State.Dragging):
            """
                When in the dragging motion, the finalPosition() is preset and unchangable. This is because the
                distance between the starting position of the gesture and it's current determined immediately the
                time, distance, and velocity at which the QScroller will travel, and the deceleration curve is then
                executed over frames to bring the animation. Shifting the scrollBar value with setValue() won't
                automatically reset the finalPosition(), as it is considered override from an external/user function.
                Thus, resendPrepareEvent() is called after the shift, which creates a new QScrollEvent with the new
                position and details.
            """
            if test_en==True: print("# 1 | Dragging Pathway")
            qScrollArea.verticalScrollBar().setValue(shift)
            qScroller.resendPrepareEvent()
        if (state == QScroller.State.Scrolling):
            """
                When in the Scrolling motion, snapping to the shift value w/ setValue eliminates all velocity
                on the resendPrepareEvent, and the result is losing all scroll momentum. Thus an additional step
                calculating how much further the scroller would've travelled, and then applying that to the shift
                is required, and subsequently executed via scrollTo(), which triggers post-resendPrepareEvent().
            """
            if test_en==True: print("# 2 | Scrolling Pathway")
            delta = round(qScroller.finalPosition().y() - value)
            if test_en==True:
                print("## Delta: ",delta,"\n## Predicted: ", shift + delta)
                print("## Shift: ",shift)
            qScrollArea.verticalScrollBar().setValue(shift)
            qScroller.resendPrepareEvent()
            qScroller.scrollTo(QPointF(
                0,
                shift + delta)
            )
        else:
            """
                When in the Inactive state, no additional motion is required and it can settle on the bound without
                issue. Additionally, this functions as a catchall for any non-scroller triggered behaviour (i.e, from
                mouse-wheels or scrollbars; this is unlikely to ever happen as this is a touch screen application, but
                it is nice for testing & caution nonetheless.)
            """
            if test_en==True: print("# 3 | Inactive/Catch-all Pathway")
            qScrollArea.verticalScrollBar().setValue(shift)

    def resizeEvent(self, event):
        h_s, h_i = self.hours_timeSelect.returnStartValue(self.hours_scrollArea.verticalScrollBar().pageStep())
        h_c = self.hours_timeSelect.returnCentralValue(self.hours_scrollArea.verticalScrollBar().pageStep())
        self.hours_timeScroller.setSnapPositionsY(h_s, h_i)
        self.hours_scrollArea.verticalScrollBar().setValue(h_c)
        m_s, m_i = self.mins_timeSelect.returnStartValue(self.mins_scrollArea.verticalScrollBar().pageStep()) 
        m_c = self.mins_timeSelect.returnCentralValue(self.mins_scrollArea.verticalScrollBar().pageStep())
        self.mins_timeScroller.setSnapPositionsY(m_s, m_i)
        self.mins_scrollArea.verticalScrollBar().setValue(m_c)
        super().resizeEvent(event)
