import sys, math, re
from enum import Enum
from typing import Dict, Tuple
from shiboken6 import Shiboken

from PySide6 import QtCore
from PySide6.QtCore import (Qt, 
                            QDateTime, QDate, QTime, 
                            QEasingCurve, 
                            Slot, Signal,
                            QPointF)
from PySide6.QtWidgets import (QWidget, QScrollArea, QLabel, QPushButton, 
                               QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, 
                               QDialog, QDialogButtonBox)
from PySide6.QtWidgets import (QSizePolicy, 
                               QScroller, QScrollerProperties)
from PySide6.QtGui import QFont, QPalette, QColor

import modules.scrollers_qt as s

class TimeType(Enum):
    Hours = 0
    SimpleMinutes = 1
    DetailedMinutes = 2

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
    def __init__(self, parent, 
                 type: TimeType, 
                 min_val=0, 
                 labelStyle=QFont("Arial",20)):
        super().__init__(parent)
        self.type, self.labelStyle              = type, labelStyle

        #Adjust variables based on changes to TimeType
        if  (self.type == TimeType.Hours):
            self.labelAlignment                 = Qt.AlignmentFlag.AlignRight
            self._entries, self._mult           = 24, 1
        elif(self.type == TimeType.SimpleMinutes):
            self.labelAlignment                 = Qt.AlignmentFlag.AlignLeft
            self._entries, self._mult           = 12, 5
        elif(self.type == TimeType.DetailedMinutes):
            self.labelAlignment                 = Qt.AlignmentFlag.AlignLeft
            self._entries, self._mult           = 60, 1
        
        self._locked                                = math.ceil(min_val / self._mult)
        if (self._locked == self._entries): self._locked -= 1    #Shouldn't happen, but just in case
        self._period                                = (self._entries - self._locked)
        self._repeats                               = self.__determineRepeats(self._entries, self._locked)

        self.labels: Dict[int, Tuple[QLabel, bool]] = []
        self.labelContainer                         = QVBoxLayout(self)

        self._selected: bool                        = None

        self.setObjectName(f"TimeSelect_{hex(id(self))}")

        self.__setup_ui()

    def __determineRepeats(self, A, O):
        """ Internal function for determining the number of sets needed on generation
            #   C is a value for deciding a 'central' value for the repeats to centre around
            #   C can be a constant, which could be an arbitrary number so long as it exceeds the maximum possible A.
            #   However, _infiniteScroll struggles with values under ~48, & setting C to 60 (max A) causes unnecessary
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
        """ A function for calculating the current _stateHandler/entry of the infinite scroll area
            #   Based on function 'f(x) = (x mod P) ÷ (P ÷ A)' 
            #   Where P is Period, & A is Amplitude
            #   O is optional for removing early values from approximation (for instance, setting minimum time)

            Example use in code: 
                return __approxFunc(x, self.period, self._entries)
        """
        return ((x % P) / ( P / (A - O) )) + O
    
    def Type(self):
        return self.type
    
    def returnCurrentVal(self, offset):
        """ Public access function for calculating the current value based on the position of the QScrollBar/QScroller
            #   Re-uses the __approxFunc function, with the period being substituted as the actual size of the container.
            #   ↪   'offset' is named as such, since the given value will typically add the final position of the scrollbar
                        and the offset (the middle of the visible scrollArea portion) together.
                ↪   truncated so that the lowest possible representer of an area is selected
        """
        self._clearSelected()
        self._setSelected(math.trunc(offset / self.returnInterval()))
        return self._mult * math.trunc(self.__approxFunc(offset, self.period, self._entries, self._locked))
    
    def _setSelected(self, val):
        self._selected  = val
        palette, font   = (QPalette(self.labels[self._selected][0].palette()), 
                           QFont(self.labels[self._selected][0].font())
                           )
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255,80,80))
        font.setBold(True)
        self.labels[self._selected][1] = True
        self.labels[self._selected][0].setPalette(palette)
        self.labels[self._selected][0].setFont(font)

    def _clearSelected(self):
        # Should be outside of scroll range, so serves as a default palette value
        palette, font = QPalette(self.labels[0][0].palette()), QFont(self.labels[0][0].font())
        # Clear any selected labels (excluding the selected)
        for label in self.labels.items():
            if self.labels[label][1] == True:
                self.labels[label][0].setPalette(palette)
                self.labels[label][0].setFont(font)
                self.labels[self._selected][1] = False
        if (self._selected != None):
            self.labels[self._selected][0].setPalette(palette)
            self.labels[self._selected][0].setFont(font)
            self.labels[self._selected][1] = False
            self._selected = None

    def clearSelected(self):
        """ Public access for clearSelected """
        self._clearSelected()
    
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
            #                   ↪   Labels are stored via a dictionary 'self.labels[][0]', so can be passed along knowing the first
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
            (self.labels[f_label][0].pos().y()) 
            + (self.labels[f_label][0].sizeHint().height() / 2)
            - (offset)
        )
        return st_val, interval
    
    def returnCentralValue(self, pagestep):
        """
            Public access function, returns exact middle label from the offset
        """
        self._clearSelected()
        m_label, offset = (round(len(self.labels) / 2)), (pagestep / 2) # Middle Label & Offset
        return (
            self.labels[m_label][0].pos().y()
            + (self.labels[m_label][0].sizeHint().height() / 2)
            - (offset)
            )
    
    def returnUpperLowerBounds(self, pagestep):
        """
            Public access function, returns exact labels from 1/4 & 3/4 of the size of the widget
        """
        b_label, t_label, offset = (round(len(self.labels) / 4)), 3*(round(len(self.labels) / 4)), (pagestep/2)
        return (
            self.labels[b_label][0].pos().y()
            + (self.labels[b_label][0].sizeHint().height() / 2)
            - (offset)
            ),(
            self.labels[t_label][0].pos().y()
            + (self.labels[t_label][0].sizeHint().height() / 2)
            - (offset)
            )
    
    def returnInterval(self):
        """
            Public access function, returns approximate distance between labels/_entries. 
                Rounded as pixels do not sit at float values.
        """
        return round(self.sizeHint().height() / len(self.labels))
    
    def changeMinVal(self, min_val, test_en=False):
        if (math.ceil(min_val / self._mult) != self._locked):
            self._locked        = math.ceil(min_val / self._mult)
            if (self._locked == self._entries): self._locked -= 1    #Shouldn't happen, but just in case
            self._period        = self._entries - self._locked
            self._repeats       = self.__determineRepeats(self._entries, self._locked)
            self._clearSelected()
            self.__reconstruct_ui()
        elif (test_en==True): print("Could not change min_val: Same as previous")

    def __setup_ui(self, test_en=False):
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
            self.labels[x][0] = QLabel(f"{val:02}", parent=self)
            self.labels[x][1] = False
            self.labels[x][0].setObjectName(f"{self.objectName()}_TSLabel_{x}_{val:02}")
            self.labels[x][0].setFont(self.labelStyle)
            self.labels[x][0].setAlignment(Qt.AlignmentFlag.AlignRight)
            self.labelContainer.addWidget(self.labels[x][0],
                                          40,
                                          self.labelAlignment)
        if (test_en): print(f"Total values: {self._period} Repeated: {self._repeats} \nTotal in list: {len(self.labels)}")
        self.setLayout(self.labelContainer)
        self.period = round(self.sizeHint().height()/self._repeats)

    def __reconstruct_ui(self, test_en=False):
        """ Internal function for that deletes the active labels in the TimeSelect object & reconstructs the new ui
            on the assumption that the values present are no longer enforceable in the TimeSelect. Should only be
            used when reusing TimeSelects.
        """
        try:
            for x in range(len(self.labels)):
                t_label: QLabel = self.findChild(QLabel, (self.labels[x][0]).objectName())
                if (test_en): print(t_label.objectName())
                self.labelContainer.removeWidget(t_label)
                t_label.deleteLater()
                if (test_en): print(Shiboken.isValid(self.labels[x][0]))
            
            if (test_en): print(len(self.labels))
            self.labels.clear() # Delete all key references (otherwise will break functions reliant on len(labels))
            self.__setup_ui()
        except Exception as e:
            print(f"### Reconstruction of ui for object {str(self.objectName())} failed:",e)

class  TTimeEditDialog(QDialog):
    """ A T(ouch)TimeEditDialog QDialog that implements seamless touch scrolling functionality in a base QDialogue,
        based on design implementations that currently exist (for instance, via iPhone Time SpinBoxes).
    """
    timeSelected = Signal(QTime)

    def __init__(self, parent, 
                 cur_QDT    :   QDateTime, 
                 min_QDT    =   QDateTime(QDate(0000,0,0),QTime(0,0,0,0)), 
                 minuteType =   TimeType.SimpleMinutes,
                 theme='light'):
        super().__init__(parent)
        self._minimumDateTime = min_QDT
        self._dateTime = cur_QDT
        self._minuteType = minuteType

        self._hours, self._minutes = 0, 0
        self._function_lock = False         # Flag for locking infinite scroll
        self._l1t_mins_TimeSelect_ACTIVE = dict()
        self._active = 'default'

        self.__setup_ui()
        self.__set_styles()
        self.__setup_connections()

    def __setup_ui(self):
        self.setWindowTitle("TTimeEditDialog")

        self._layer0_base       = QVBoxLayout(self)

        self._layer1_times      = QHBoxLayout()   #   Horizontal box layout for time selects
        self._layer1_buttons    = QHBoxLayout()

        self._layer0_base.addLayout(self._layer1_times)
        self._layer0_base.addLayout(self._layer1_buttons)
            
        self._l1t_hours_scrollArea = QScrollArea(self)
        if ((self._minimumDateTime.date() == self._dateTime.date()) 
            and (self._minimumDateTime.time().hour() > 0)): 
            self._l1t_hours_TimeSelect = TimeSelect(self, TimeType.Hours, self._minimumDateTime.time().hour())
            self._active = 'alternate'
        else: self._l1t_hours_TimeSelect = TimeSelect(self, TimeType.Hours)
        self._l1t_hours_scrollArea.setWidget(self._l1t_hours_TimeSelect)
        self._l1t_hours_timeScroller = s.returnDragScroller(self._l1t_hours_scrollArea)

        self._l1t_mins_scrollArea = QScrollArea(self)

        self._l1t_mins_TimeSelect_ACTIVE['default'] = TimeSelect(self, self._minuteType)  
        self._l1t_mins_TimeSelect_ACTIVE['alternate'] = TimeSelect(self, self._minuteType, self._minimumDateTime.time().minute())
        self._l1t_mins_scrollArea.setWidget(self._l1t_mins_TimeSelect_ACTIVE[self._active])
        self._l1t_mins_timeScroller = s.returnDragScroller(self._l1t_mins_scrollArea)

        self._layer1_times.addWidget(self._l1t_hours_scrollArea)
        self._layer1_times.addWidget(self._l1t_mins_scrollArea)
        
        self._l1b_confirm_pushButton = QPushButton(text="Confirm", parent=self)
        self._l1b_cancel_pushButton = QPushButton(text="Cancel", parent=self)
        self._layer1_buttons.addWidget(self._l1b_confirm_pushButton)
        self._layer1_buttons.addWidget(self._l1b_cancel_pushButton)

        self._l1b_confirm_pushButton.setObjectName("datetime_dialog_confirm_pushbutton")
        self._l1b_cancel_pushButton.setObjectName("datetime_dialog_cancel_pushbutton")

    def __set_styles(self):
        """self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint) #sets Window to clear"""
        self.setWindowModality(Qt.WindowModality.ApplicationModal) #sets Dialog to override background application until closed
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowOpacity(0.9)

        self._l1t_hours_scrollArea.setWidgetResizable(True)
        self._l1t_mins_scrollArea.setWidgetResizable(True) 

        self.setStyleSheet(f"""
QScrollArea {{
    background: transparent;
    border: 0px;
}}
QScrollBar {{
    width: 0px;
    height: 0px;
}}          
    
#datetime_dialog {{
    border-radius: 4px
}}  

/*#################### DIALOG BUTTONS ####################*/
                           
QPushButton#datetime_dialog_confirm_pushbutton, QPushButton#datetime_dialog_cancel_pushbutton {{
    background-color: rgba(30, 30, 30, 1);
    border: none;
    border-radius: 0px;
    padding: 8px;
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
        
        self._l1b_confirm_pushButton.setFont(QFont("Arial",18))
        self._l1b_cancel_pushButton.setFont(QFont("Arial",18))

        self._l1b_confirm_pushButton.setMaximumHeight(40)
        self._l1b_cancel_pushButton.setMaximumHeight(40)

        self._l1b_confirm_pushButton.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self._l1b_cancel_pushButton.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.layout().setSpacing(0)
        self._layer0_base.setSpacing(0)
        self._layer1_times.setSpacing(0)
        self._layer1_buttons.setSpacing(0)

        self.setContentsMargins(
            0,          #Left
            0,          #Top
            0,          #Right
            0           #Bottom
            )
        self._layer1_times.setContentsMargins(
            0,          #Left
            0,          #Top
            0,          #Right
            0           #Bottom
            )
        self._layer0_base.setContentsMargins(
            0,          #Left
            0,          #Top
            0,          #Right
            0           #Bottom
            )
        
        pref_height = (
            (5 * self._l1t_hours_TimeSelect.returnInterval())
            + self._l1b_confirm_pushButton.sizeHint().height()
            - 20
            )

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)

        self.setBaseSize(200,pref_height)
        self.setMinimumHeight(pref_height)
        self.setMaximumHeight(pref_height)

        self.adjustSize()
        self._l1b_confirm_pushButton.adjustSize()

    def __setup_connections(self):
        self._l1b_confirm_pushButton.clicked.connect(lambda: self.dialogueAccepted())
        self._l1b_cancel_pushButton.clicked.connect(lambda: self.dialogueRejected())

        self._l1t_hours_timeScroller.stateChanged.connect(
            lambda state: 
            self._stateHandler(
                state,
                self._l1t_hours_TimeSelect,
                int(
                    self._l1t_hours_timeScroller.finalPosition().y() + 
                    (self._l1t_hours_scrollArea.verticalScrollBar().pageStep()/2)
                )
                ))
        self._l1t_mins_timeScroller.stateChanged.connect(
            lambda state: 
            self._stateHandler(
                state,
                self._l1t_mins_TimeSelect_ACTIVE[self._active],
                int(
                    self._l1t_mins_timeScroller.finalPosition().y() +
                    (self._l1t_mins_scrollArea.verticalScrollBar().pageStep()/2)
                )
                ))
        
        self._l1t_hours_scrollArea.verticalScrollBar().valueChanged.connect(
            lambda value: 
            self._infiniteScroll(
                value,
                self._l1t_hours_scrollArea,
                self._l1t_hours_timeScroller,
                self._l1t_hours_TimeSelect
                ))
        self._l1t_mins_scrollArea.verticalScrollBar().valueChanged.connect(
            lambda value: 
            self._infiniteScroll(
                value,
                self._l1t_mins_scrollArea,
                self._l1t_mins_timeScroller,
                self._l1t_mins_TimeSelect_ACTIVE[self._active]
                ))

    @Slot(QScroller.State)
    #Handle stateChanges triggered by TimeSelect
    def _stateHandler(self, state, TimeSelect: TimeSelect, pagestep):
        if (state == QScroller.State.Inactive):
            final_val = TimeSelect.returnCurrentVal(pagestep)
            self._updateCurrentVarsAndQTime(final_val, TimeSelect)
            self._l1b_confirm_pushButton.setEnabled(True)
        else:
            if (self._l1b_confirm_pushButton.isEnabled()): self._l1b_confirm_pushButton.setDisabled(True)
            TimeSelect.clearSelected()
        
    def _updateCurrentVarsAndQTime(self, f_val: int, TimeSelect: TimeSelect):
        if (TimeSelect.Type() == TimeType.Hours):
            self._hours = f_val
            if ((self._hours == TimeSelect.returnMinimumVal()) 
                and (0 < self._hours)):
                self._setActiveTimeSelect('alternate')
            elif (self._hours > TimeSelect.returnMinimumVal()):
                self._setActiveTimeSelect('default')
            else:
                self._updateCurrentQTime(test_en=True)
        else:
            self._minutes = f_val
            self._updateCurrentQTime(test_en=True)
        
    def _updateCurrentQTime(self, test_en=False):
        self._dateTime.setTime(QTime(self._hours, self._minutes, 0, 0))
        if (test_en == True): print(f"Current time: {self._dateTime.time()}")

    def _setActiveTimeSelect(self, new: str):
        if (new == self._active):
            self._updateCurrentQTime(test_en=True)
        else: 
            self._swapActiveTimeSelect()

    def _swapActiveTimeSelect(self):
        if (self._active == 'default'):
            self._active = 'alternate'
            self._updateMinutesActiveTimeSelect()
        elif (self._active == 'alternate'):
            self._active = 'default'
            self._updateMinutesActiveTimeSelect()
        else: 
            self._active = 'default'
            self._updateMinutesActiveTimeSelect()

    def _updateMinutesActiveTimeSelect(self):
        self._l1t_mins_scrollArea.takeWidget()
        self._l1t_mins_scrollArea.setWidget(self._l1t_mins_TimeSelect_ACTIVE[self._active])
        self._updateMinutesPositions()
        self._updateCurrentQTime(test_en=True)

    #Shift scrollArea().verticalScrollBar() to a new value if exceeding a bound
    def _infiniteScroll(self, value, qScrollArea: QScrollArea, qScroller: QScroller, TimeSelect: TimeSelect):
        l_bound, u_bound = TimeSelect.returnUpperLowerBounds(qScrollArea.verticalScrollBar().pageStep())
        interval = TimeSelect.returnInterval()
        #Prevent repeated calls --> for instance, if Dragging hits a bound, it repeatedly calls which causes undesired behaviour
        if ((l_bound - (2 * interval)) <= value) & (value <= (u_bound + (2 * interval))): self._function_lock = False

        if (value < (l_bound - (2 * interval))) & (self._function_lock == False):
            self._function_lock = True
            try:
                shift = u_bound - (2 * interval)
                self._shiftScroll(shift, value, qScroller, qScrollArea, "lower")
                self._function_lock = False
            except Exception as e:
                print("###Infinite Scroll Error: ",e)
                self._function_lock = False

        if (value > (u_bound + (2 * interval))) & (self._function_lock == False):
            self._function_lock = True
            try:
                shift = l_bound + (2 * interval)
                self._shiftScroll(shift, value, qScroller, qScrollArea, "upper")
                self._function_lock = False
            except Exception as e:
                print("### Shift Scroll Error: ",e)
                self._function_lock = False

    def _shiftScroll(self, shift, value, qScroller: QScroller, qScrollArea: QScrollArea, bound="undef", test_en=False):
        """ Private access function for use with self._infiniteScroll()
            ↪   Takes all values passed to the valueChanged Slot & shifts it via the amount specified by the caller.
                Additionally, handles all types of QScroller.States at the moment of shifting, ensuring continuation
                of Dragging movements & seamless animations for those in motion/scrolling

                Additional notes: Was initially packaged in self._infiniteScroll(), but migrated to a secondary func-
                -tion as both upper and lower bounds functioned identically outside of the value passed to the shift.

            Variable outline:
                'shift':    Shift is the new verticalScrollBar position that'll be set post call. Shift is generally
                            an upper or lower bound, inclined inwards (towards the central value) so that it doesn't
                            overlap with the 'real bound'. Bounds edges are 2 _entries outwards, and shifted values
                            are the opposite bound 2 _entries inwards.

                'value':    The function calling this (_infiniteScroll()) is linked to a signal slot connection for
                            verticalScrollBar listed 'valueChanged'. The value in this instance is the value passed
                            from aforementioned signal slot connection. Despite this, this function is only called
                            when the scrollbar has exceeded acceptible bounds (due to the _function_lock variable and
                            general design of _infiniteScroll())

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

    def _updatePositions(self, TimeSelect: TimeSelect, scrollArea: QScrollArea, timeScroller: QScroller):
        """ Private function for use with '_updateHoursPositions' & '_updateMinutesPositions' """
        n_s, n_i = TimeSelect.returnStartValue(scrollArea.verticalScrollBar().pageStep())
        n_c = TimeSelect.returnCentralValue(scrollArea.verticalScrollBar().pageStep())
        timeScroller.setSnapPositionsY(n_s, n_i)
        scrollArea.verticalScrollBar().setValue(n_c)

        return TimeSelect.returnCurrentVal(
            scrollArea.verticalScrollBar().value() 
            + (scrollArea.verticalScrollBar().pageStep() / 2)
        )

    def _updateHoursPositions(self):
        self._hours = self._updatePositions(TimeSelect    =self._l1t_hours_TimeSelect,
                                            scrollArea    =self._l1t_hours_scrollArea,
                                            timeScroller  =self._l1t_hours_timeScroller)
    
    def _updateMinutesPositions(self):
        self._minutes = self._updatePositions(TimeSelect    =self._l1t_mins_TimeSelect_ACTIVE[self._active],
                                              scrollArea    =self._l1t_mins_scrollArea,
                                              timeScroller  =self._l1t_mins_timeScroller)

    def _setPositions(self):
        self._updateHoursPositions()
        self._updateMinutesPositions()

    def changeDates(self, new_M_QDT: QDateTime, new_C_QDT: QDateTime):
        """ Public access function for changing/updating the values in the TTimeEditDialog
            #   Requires both new values for reuse.
            #   Uses 'changeMinVal' in TimeSelect to change ui features
        """
        self._minimumDateTime = new_M_QDT
        self._dateTime = new_C_QDT

        print(self._minimumDateTime)
        print(self._dateTime)

        if ((self._minimumDateTime.date() == self._dateTime.date()) 
            and (self._minimumDateTime.time() > QTime(0,0,0,0))):
            self._l1t_hours_TimeSelect.changeMinVal(self._minimumDateTime.time().hour())
            self._l1t_mins_TimeSelect_ACTIVE['alternate'].changeMinVal(self._minimumDateTime.time().minute())
            self._setActiveTimeSelect('alternate')
        else:
            self._l1t_hours_TimeSelect.changeMinVal(QTime(0,0,0,0).hour())
    
    def setMinimumDateTime(self, new_min: QDateTime): self.changeDates(new_min, self._dateTime)
    def setCurrentDateTime(self, new_cur: QDateTime): self.changeDates(self._minimumDateTime, new_cur)

    def resizeEvent(self, event):
        self._setPositions()
        super().resizeEvent(event)

    def showEvent(self, event):
        self._setPositions()
        return super().showEvent(event)
    
    def dialogueAccepted(self): self.timeSelected.emit(self._dateTime.time()), self.accept()
    def dialogueRejected(self): self.reject(), self.rejected.emit()