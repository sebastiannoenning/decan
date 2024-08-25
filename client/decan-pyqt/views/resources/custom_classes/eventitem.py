# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties
from PySide6.QtGui import QFont

"""class Event(QObject):"""

"""Event.

    Attributes:
        ETitle: EventTitle
        EDescription: Event Description
        ETime: Event Time
        ELocation: 

    Signals:
        updated: Emitted when one of the entry values has been changed
        deleted: Emitted/called on deletion of the object
"""

"""    updated_text = QtCore.Signal()
    deleted_object = QtCore.Signal()

    def __init__(self, ETitle = 'ETitle'*10, EDescription = 'EDescription'*30, ETime = '00:00'):
        super().__init__()
        self.ETitle = ETitle
        self.EDescription = EDescription
        self.ETime = ETime

    def set_data(self, NETitle = None, NEDescription = None, NETime = None):
        updated = False

        if (NETitle is not None) and (NETitle != self.ETitle): 
            self.ETitle = NETitle
            updated = True
        if (NEDescription is not None) and (NEDescription!= self.EDescription): 
            self.EDescription = NEDescription
            updated = True
        if (NETime is not None) and (NETime != self.ETime): 
            self.ETime = NETime
            updated = True

        if updated: self.updated_text.emit()


    def get_data(self):
        return {
            'ETitle': self.ETitle,
            'EDescription': self.EDescription,
            'ETime': self.ETime
        }
    
    def __del__(self): self.deleted_object.emit()"""

class EventItem(QWidget):

    """A "EventItem" widget with an several labels.

    Attributes:
        _layout: The QVBoxLayout containing all the nested labels
        _event: The Event object with the attributes for the labels
        EID : EventID
        ETitle: EventTitle
        EDescription: Event Description
        ETime: Event Time
        ELocation: 

    Signals:
    """
        
    def __init__(self, parent=None):
        super().__init__(parent)

        self.EID = None
        self.ETitle = None
        self.EDescription = None
        self.ETime = None

        self.setup_ui()

    def setup_ui(self):
        # create vertical box layout to hold all the items
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        # Create 3 main parts for place in layout -- will add later
        self._header = QHBoxLayout()         #Top row       Features two labels - one at fixed width (for EventTitle), and another nested in a scroll-area
        self._midsection = QScrollArea()     #Mid row       Features one label, nested inside a scroll-area
        self._footer = QLabel()       #Bottom row

        # Header Components
        self._header1_wrapper = QScrollArea()               #Scroll Area
        self._header1_title = QLabel('EventTitle'*10)          # ↪ For nested QLabel, displaying ETITLE
        self._header2_time = QLabel('00:00')                #QLabel, displaying ESTARTTIME

        #   Header_1 wrapper settings 
        self._header1_wrapper.setWidget(self._header1_title)
        self._header1_wrapper.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self._header1_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._header1_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        #   Create scroller & input type
        self._header1scroll = QScroller.scroller(self._header1_wrapper.viewport())
        self._header1scroll.grabGesture(self._header1_wrapper.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)
        #   Create properties profile
        self._header1scroll_props = self._header1scroll.scrollerProperties()    # Copy default properties
        self._header1scroll_props.setScrollMetric(                              #      Remove vertical overshoot
            QScrollerProperties.ScrollMetric.VerticalOvershootPolicy, 1)        #       ↪ 1 is enum for the 'OvershootAlwaysOff' setting --> couldn't refer to it directly
        self._header1scroll_props.setScrollMetric(                              #      Remove horizontal overshoot
            QScrollerProperties.ScrollMetric.HorizontalOvershootPolicy, 1)      #       ↪ 1 is enum for the 'OvershootAlwaysOff' setting --> couldn't refer to it directly
        self._header1scroll_props.setScrollMetric(                              #      Implement strong AxisLock (prevents bi-directional scroll movements)
            QScrollerProperties.ScrollMetric.AxisLockThreshold, 1)              #       ↪ Value can be set between 0 & 1, with 1 indicating strong lock.
        self._header1scroll.setScrollerProperties(self._header1scroll_props)  #set scroller properties to profile

        #   Header font styling for components
        self._headerfont = QFont()
        self._headerfont.setFamilies([u"Arial"])
        self._headerfont.setPointSize(20)
        self._header1_title.setFont(self._headerfont)
        self._header2_time.setFont(self._headerfont)

        self._header1_title.adjustSize()
        self._header1_wrapper.setMaximumHeight(self._header1_title.height())
        self._header2_time.adjustSize()
        self._header2_time.setMaximumWidth(self._header2_time.width())

        self._header.addWidget(self._header1_wrapper, 0)
        self._header.addWidget(self._header2_time, 0)

        self._midsection.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self._midsection.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._midsection_text = QLabel('brown dog, '*10)
        self._midsection_text.setWordWrap(True)
        self._midsection.setWidget(self._midsection_text)

        self._midsectionscroll = QScroller.scroller(self._midsection.viewport())
        self._midsectionscroll.grabGesture(self._midsection.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)


        # add rows to layout
        self._layout.addLayout(self._header, 0)         # add header row
        self._layout.addWidget(self._midsection, 1)     # add midsection row
        self._layout.addWidget(self._footer, 0)         # add footer row

    def set_data(self, EID = None, ETitle = None, EDescription = None, ETime = None):

        if (self.EID is None): # EID can only be set once, on the objects creation. subsequent calls to change the EID are ignored.
            self.EID = EID
        if (ETitle is not None) and (ETitle != self.ETitle): 
            self.ETitle = ETitle
            self._header1_title.setText(self.ETitle)
            self._header1_title.adjustSize()
        if (EDescription is not None) and (EDescription!= self.EDescription): 
            self.EDescription = EDescription
            self._midsection_text.setText(self.EDescription)
            self._midsection_text.adjustSize()
        if (ETime is not None) and (ETime != self.ETime): 
            self.ETime = ETime
            self._header2_time.setText(self.ETime)
            self._header2_time.adjustSize()

        self._midsection_text.adjustSize()

    def get_data(self):
        return {
            'EID' : self.EID,
            'ETitle': self.ETitle,
            'EDescription': self.EDescription,
            'ETime': self.ETime
        }
