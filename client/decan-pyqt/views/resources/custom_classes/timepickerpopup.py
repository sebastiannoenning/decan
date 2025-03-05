import sys, math
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QEasingCurve, Slot, QPointF
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QLayout, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties, QDialogButtonBox, QFrame
from PySide6.QtGui import QFont, QMouseEvent, QPainter

class TimeType(Enum):
    Hours = 1
    SimpleMinutes = 2
    DetailedMinutes = 3

class TimeSelect(QWidget):
    """A "TimeSelect" widget with a predetermined number of labels, signifying time.

    Variables:
        type:       TimeType, custom Enum which will influence _entries, _repeats, _mult, and consequently _period
        labels:     Python Dictionary storing references to labels, can refer to specific values via labels[n]
        _locked:     Adds omitting options for __approxFunc
        _entries:   Number of options (i.e, 0-23, 0-55, 0-59) or Amplitude
        _repeats:   Amount of times the number of _entries are repeated during generation
        _mult:      Multiplier for conversion to SimpleMinutes/5 minute intervals
        _period:    Total size of widget divided by number of repeated values inside of it. On initiation, the _entries minus the locked.

    Functions:

    """
    def __init__(self, parent, Type: TimeType, min_val=0, labelStyle=QFont("Arial",18)):
        super().__init__(parent)
        self.type = Type

        #Adjust variables based on changes to TimeType
        if  (self.type == TimeType.Hours):
            self.labelAlignment = Qt.AlignmentFlag.AlignRight
            self._entries, self._mult = 24, 1
        elif(self.type == TimeType.SimpleMinutes):
            self.labelAlignment = Qt.AlignmentFlag.AlignLeft
            self._entries, self._mult = 12, 5
        elif(self.type == TimeType.DetailedMinutes):
            self.labelAlignment = Qt.AlignmentFlag.AlignLeft
            self._entries, self._mult = 60, 1
        
        self._locked = math.ceil(min_val / self._mult)
        if (self._locked == self._entries): self._locked -= 1    #Shouldn't happen, but just in case
        self._period = (self._entries - self._locked)
        self._repeats = self.__determineRepeats(self._entries, self._locked)

        self.labels = dict()
        self.labelContainer = QVBoxLayout(self)

        self.labelStyle = labelStyle

        self.__setup_ui()

    def __determineRepeats(self, A, O):
        """ Internal function for determining the number of sets needed on generation
            #   C is a value for deciding a 'central' value for the repeats to centre around
            #   C can be a constant, which could be an arbitrary number so long as it exceeds the maximum possible A.
            #   However, infiniteScroll struggles with values under ~48, & setting C to 60 (max A) causes unnecessary
            #   labels to be created on both SimpleMinutes & Hours. Accounting for perfomance issues, C can now only
            #   be 48 or 60 with the following calculation & possible values for A.

            #   R will calculate an appropriate amount of repeats for labels to be added to 
        """
        C = (48 + (round(
                    (48 / A)
                    % 2)
                    * 12 )
            )
        
        R = (2 * round(
                    ( C / ( A - O ))
                    / 2 )
            )
        return R

    def __approxFunc(self, x, P, A, O=0):
        """ A function for calculating the current finalTimeValue/entry of the infinite scroll area
            #   Based on function 'f(x) = (x mod P) ÷ (P ÷ A)' 
            #   Where P is Period, & A is Amplitude
            #   O is optional for removing early values from approximation (for instance, setting minimum time)

            Example use in code: 
                return __approxFunc(x, self.period, self._entries)
        """
        return ((x % P) / ( P / (A - O) )) + O
    
    def returnCurrentVal(self, offset):
        """ Public access function for calculating the current value based on the position of the QScrollBar/QScroller
            #   Re-uses the __approxFunc function, with the period being substituted as the actual size of the container.
            #   ↪   'offset' is named as such, since the given value will typically add the final position of the scrollbar
                        and the offset (the middle of the visible scrollArea portion) together.
                ↪   truncated so that the lowest possible representer of an area is selected
        """
        return self._mult * math.trunc(self.__approxFunc(offset, self.period, self._entries, self._locked))
    
    def Type(self):
        return self.type
    
    def returnMinimumVal(self):
        return self._locked * self._mult
    
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
            #       'interval': The distance between it & succeeding _entries. Assumes uniform snapping distance (valid here)
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
        """
            Public access function, returns exact middle label from the offset
        """
        m_label, offset = (round(len(self.labels) / 2)), (pagestep / 2) # Middle Label & Offset
        return (
            self.labels[m_label].pos().y()
            + (self.labels[m_label].sizeHint().height() / 2)
            - (offset)
            )
    
    def returnUpperLowerBounds(self, pagestep):
        """
            Public access function, returns exact labels from 1/4 & 3/4 of the size of the widget
        """
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
        """
            Public access function, returns approximate distance between labels/_entries. 
                Rounded as pixels do not sit at float values.
        """
        return round(self.sizeHint().height() / len(self.labels))

    def __setup_ui(self):
        """ Adds all labels to the interface.
            #   Uses __approxFunc to fill list with 2 sets of the value range
            #   ↪   i.e, for Hours: fills labelContainer with 0-23 twice
            #       i.e, for SimpleMinutes: fills labelContainer with 0-55 four times (i.e, 12*4 vals)
            #       i.e, for DetailedMinutes: fills labelContainer with 0-59 twice 
        """
        for x in range(round((self._period)*self._repeats)):
            val = round(self.__approxFunc(x,
                                          P=(self._period), 
                                          A=(self._entries),
                                          O=(self._locked)
                                          ) * self._mult
                                          )
            self.labels[x] = QLabel(f"{val:02}", parent=self)
            self.labels[x].setObjectName(f"TM_{self.objectName}_Type_{self.type}_Pos_{x}_Val_{val:02}")
            self.labels[x].setFont(self.labelStyle)
            self.labels[x].setAlignment(Qt.AlignmentFlag.AlignRight)
            self.labelContainer.addWidget(self.labels[x],40,self.labelAlignment)
        print(f"Total values: {self._period} Repeated: {self._repeats} \nTotal in list: {len(self.labels)}")
        self.setLayout(self.labelContainer)
        self.period = round(self.sizeHint().height()/self._repeats)

    def resizeEvent(self, event):
        return super().resizeEvent(event)

class TimePickerPopup(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.minimumDateTime = QDateTime()
        self.currentDateTime = QDateTime()

        self.hours = 0
        self.minutes = 0

        self.function_lock = False

        self.__setup_ui()
        self.__set_styles()
        self.__setup_connections()

    def __setup_ui(self):
        self.setWindowTitle("timePickerPopup")

        self.layer0_base = QVBoxLayout()
        self.setLayout(self.layer0_base)

        self.layer1_times = QHBoxLayout()   #   Horizontal box layout for time selects

        self.hours_scrollArea = QScrollArea(self)
        self.hours_timeSelect = TimeSelect(self, TimeType.Hours)
        self.hours_scrollArea.setWidget(self.hours_timeSelect)
        self.hours_timeScroller = self.__create_drag_scroller(self.hours_scrollArea)

        """if (self.minimumDateTime == None):"""
        self.mins_scrollArea = QScrollArea(self)
        self.mins_timeSelect = TimeSelect(self, TimeType.SimpleMinutes)
        self.mins_scrollArea.setWidget(self.mins_timeSelect)
        self.mins_timeScroller = self.__create_drag_scroller(self.mins_scrollArea)
        """else:
            self.mins_timeSelect_open = TimeSelect(self, TimeType.SimpleMinutes)
            self.mins_timeSelect_min = TimeSelect(self, TimeType.SimpleMinutes)"""

        self.layer1_times.addWidget(self.hours_scrollArea)
        self.layer1_times.addWidget(self.mins_scrollArea)
        
        self.confirm_pushButton = QPushButton(text="Confirm", parent=self)
        self.cancel_pushButton = QPushButton(text="Cancel",parent=self)

        self.footer_button_box = QDialogButtonBox(self, orientation=Qt.Orientation.Horizontal)
        self.footer_button_box.setCenterButtons(True)
        self.footer_button_box.addButton(self.cancel_pushButton, QDialogButtonBox.ButtonRole.DestructiveRole)
        self.footer_button_box.addButton(self.confirm_pushButton, QDialogButtonBox.ButtonRole.AcceptRole)

        self.layer0_base.addLayout(self.layer1_times)
        self.layer0_base.addWidget(self.footer_button_box)

    def __set_styles(self):
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint) #sets Window to clear
        self.setWindowModality(Qt.WindowModality.ApplicationModal) #sets Dialog to override background application until closed

        self.hours_scrollArea.setWidgetResizable(True)
        self.mins_scrollArea.setWidgetResizable(True) 

        self.setStyleSheet(""" 
            QDialog {
                border: 1px;
                border-radius: 5px;
                padding: 0px;
                margin: 0px;
            }""" """
            QScrollArea {
                background : transparent;
                border: 0px;
            }""" """
            QScrollBar {
                width: 0px;
                height: 0px;
            }""" """
            QPushButton {
                height: 25px;
            }""" """ 
            QDialogButtonBox {
                padding: 0px:
                margin: 0px;
            }
            """
        )

        self.confirm_pushButton.setFont(QFont("Arial",21))
        self.confirm_pushButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.cancel_pushButton.setFont(QFont("Arial",21))
        self.cancel_pushButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.layout().setSpacing(0)
        self.layer0_base.setSpacing(0)
        self.layer1_times.setSpacing(0)
        self.footer_button_box.layout().setSpacing(0)

        self.layout().setSpacing(0)
        self.layer1_times.setContentsMargins(0,0,0,0)
        self.layer0_base.setContentsMargins(0,30,0,0)
        self.footer_button_box.layout().setContentsMargins(0,0,0,0)

        pref_height = (5 * self.hours_timeSelect.returnInterval()) + self.confirm_pushButton.sizeHint().height()

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)

        self.setBaseSize(200,pref_height)
        self.setMinimumHeight(pref_height)
        self.setMaximumHeight(pref_height)

        self.adjustSize()
        self.confirm_pushButton.adjustSize()
        self.cancel_pushButton.adjustSize()

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
            QScrollerProperties.ScrollMetric.ScrollingCurve, QEasingCurve(QEasingCurve.Type.OutExpo))
        new_properties.setScrollMetric( #DecelerationFactor is a percentage decrease of velocity every frame
            QScrollerProperties.ScrollMetric.DecelerationFactor, 0.01) #I.e, around 1% each frame
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
        if (state == QScroller.State.Inactive):
            final_val = timeSelect.returnCurrentVal(offset)
            #print("Calculated central value: ", final_val)
            #self.swapCheck(timeSelect, final_val)
            return timeSelect.returnCurrentVal(offset)
        else: 
            return None
        
    def swapCheck(self, timeSelect: TimeSelect, f_val):
        if (timeSelect.Type() == TimeType.Hours):
            print()


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
                            overlap with the 'real bound'. Bounds edges are 2 _entries outwards, and shifted values
                            are the opposite bound 2 _entries inwards.

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
                position and previous calculated velocity.
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

    def setPositions(self):
        h_s, h_i = self.hours_timeSelect.returnStartValue(self.hours_scrollArea.verticalScrollBar().pageStep())
        h_c = self.hours_timeSelect.returnCentralValue(self.hours_scrollArea.verticalScrollBar().pageStep())
        self.hours_timeScroller.setSnapPositionsY(h_s, h_i)
        self.hours_scrollArea.verticalScrollBar().setValue(h_c)

        m_s, m_i = self.mins_timeSelect.returnStartValue(self.mins_scrollArea.verticalScrollBar().pageStep()) 
        m_c = self.mins_timeSelect.returnCentralValue(self.mins_scrollArea.verticalScrollBar().pageStep())
        self.mins_timeScroller.setSnapPositionsY(m_s, m_i)
        self.mins_scrollArea.verticalScrollBar().setValue(m_c)

    def resizeEvent(self, event):
        self.setPositions()
        super().resizeEvent(event)

    def showEvent(self, event):
        self.setPositions()
        return super().showEvent(event)