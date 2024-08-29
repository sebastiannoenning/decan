import datetime
import json

# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties, QCheckBox
from PySide6.QtGui import QFont

class EventItem(QWidget):

    """A "EventItem" widget with an several labels.

    Attributes:
        _layout: The QVBoxLayout containing all the nested labels
        _event: The Event object with the attributes for the labels
        EID : EventID
        ETitle: EventTitle
        ETime: Event Time
        EAttributes: Event Attributes 

    Signals:
    """
        
    def __init__(self, parent: QWidget, EID: int, ETitle: str, EStartTime, EAttributes: json):
        super().__init__(parent)

        self.EID = EID
        self.ETitle = ETitle
        self.EStart_Time, EEnd_Time = EStartTime, None
        self.EAttributes = EAttributes 

        self.setup_ui()


    def mousePressEvent(self, event):
        # Check if the left mouse button was pressed
        if event.button() == Qt.LeftButton:
            # Change the background color to a new color
            print(self.EID)

        # Call the base class implementation to ensure the event is handled correctly
        super().mousePressEvent(event)

    #   For use with all scrollers where uni-directional scrolling is key.
    #       ↪ Properties are not expected to be changed, so internal is fine. 
    #       ↪ This can be enforced with high-axis lock, removal of overshooting and slight padding (1-2px) on the scrollable objects.
    def uni_scroller(self, viewport: QScrollArea):
        #   Create properties profile
        side_scroll = QScroller.scroller(viewport.viewport())
        side_scroll.grabGesture(viewport.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)
        #   Create properties profile
        side_scroll_props = side_scroll.scrollerProperties()    # Copy default properties
        side_scroll_props.setScrollMetric(                                      #      Remove vertical overshoot
            QScrollerProperties.ScrollMetric.VerticalOvershootPolicy, 1)        #       ↪ 1 is enum for the 'OvershootAlwaysOff' setting --> couldn't refer to it directly
        side_scroll_props.setScrollMetric(                                      #      Remove horizontal overshoot
            QScrollerProperties.ScrollMetric.HorizontalOvershootPolicy, 1)      #       ↪ 1 is enum for the 'OvershootAlwaysOff' setting --> couldn't refer to it directly
        side_scroll_props.setScrollMetric(                                      #      Implement strong AxisLock (prevents bi-directional scroll movements)
            QScrollerProperties.ScrollMetric.AxisLockThreshold, 1)              #       ↪ Value can be set between 0 & 1, with 1 indicating strong lock.
        side_scroll.setScrollerProperties(side_scroll_props)    #set scroller properties to profile
        return side_scroll

    def setup_ui(self):
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        # create vertical box layout to hold all the items
        self._layout = QVBoxLayout()
        self._layout.setSpacing(4)
        self.setLayout(self._layout)

        # Create 3 main parts for place in layout -- will add later
        self._header = QHBoxLayout()         #Top row       Features two labels - one at fixed width (for EventTitle), and another nested in a scroll-area
        #self._midsection = QScrollArea()     #Mid row       Features one label, nested inside a scroll-area
        self._footer = QLabel("Estimated travel time:")       #Bottom row

        # Header Components
        self._header.setSpacing(10)
        self._header1_wrapper = QScrollArea()               #Scroll Area
        self._header1_title = QLabel('EventTitle'*10)       # ↪ For nested QLabel, displaying ETITLE
        self._header2_time = QLabel('00:00')                #QLabel, displaying ESTARTTIME

        #self._header2_time.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        #   Header_1 wrapper settings 
        self._header1_wrapper.setWidget(self._header1_title)
        self._header1_wrapper.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self._header1_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._header1_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._header1_wrapperscroll = self.uni_scroller(self._header1_wrapper)

        #   Header font styling for components
        self._headerfont = QFont()
        self._headerfont.setFamilies([u"Arial"])
        self._headerfont.setPointSize(24)
        self._header1_title.setFont(self._headerfont)
        self._header2_time.setFont(self._headerfont)

        self._header1_title.adjustSize()
        self._header1_wrapper.setMaximumHeight(self._header1_title.height()+2)
        self._header2_time.adjustSize()
        self._header2_time.setMaximumWidth(self._header2_time.width())

        self._header.addWidget(self._header1_wrapper, 0)
        self._header.addWidget(self._header2_time, 0)

        """self._midsection.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        self._midsection.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._midsection.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self._midsection_text = QLabel('brown dog, '*10)
        self._midsection_text.setWordWrap(True)
        self._midsection.setWidget(self._midsection_text)
        self._midsectionscroll = self.uni_scroller(self._midsection)"""

        self._additional = QVBoxLayout()
        self._additional.setSpacing(4)
        
        if self.EAttributes is not None: 
            for key, value in self.EAttributes.items():
                try:
                    object_type, index_number = key.rsplit('_', 1)
                except:
                    print("Not of type index")
                if object_type == 'EDescription':
                    self.object = self.EDescription(self, value)
                    self.object.setObjectName(key)
                    #self.object.setup_scroll(self.uni_scroller(self.object))
                    self._additional.addWidget(self.object)
                elif object_type == 'EToDo' :
                    self.object = self.EToDo(self, value, value)
                    self.object.setObjectName(key)
                    #self.object.setup_scroll(self.uni_scroller(self.object._wrapper))
                    self._additional.addWidget(self.object)
                elif object_type == 'object_index':
                    print(key,value)


        # add rows to layout
        print('header size:',self._header2_time.sizeHint())
        print('midsection size:',self._additional.sizeHint())
        print('footer size:',self._footer.sizeHint())#"""

        self._layout.addLayout(self._header, 0)         # add header row
        self._layout.addLayout(self._additional, 1)     # add midsection row
        self._layout.addWidget(self._footer, 0)         # add footer row
    
    class EDescription(QScrollArea):
        def __init__(self, parent, text: str):
            super().__init__(parent)
            self._parent = parent
            self.text = text
            self.__setup_ui()
            
        def __setup_ui(self):
            #setup scroll settings
            self.setMaximumHeight(60)
            self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            self._scroll = self._parent.uni_scroller(self)
            self._label = QLabel(self)
            self._label.setText(self.text)
            self._label.setWordWrap(True)
            self.setWidget(self._label)

        """def setup_scroll(self, scroll: QScroller):
            self._scroll = scroll"""

        def setText(self, new_text: str):
            self._label.setText(new_text)

    class EToDo(QWidget):
        def __init__(self, parent, text: str, box: bool):
            super().__init__(parent)
            self._parent = parent
            self.text = text
            self.box = box
            self.__setup_ui()
        
        def __setup_ui(self):
            self.setMaximumHeight(50)
            self._layout = QHBoxLayout(self)
            self._layout.setContentsMargins(1,1,1,1)

            self._checkbox = QCheckBox(self)
            self._checkbox.setChecked(self.box)

            self._label = QLabel(self)
            self._label.setText(self.text)
            self._font = QFont(self)
            self._font.setFamilies([u"Arial"])
            self._font.setPointSize(30)
            self._font.setBold(True)
            self._label.setFont(self._font)
            self._label.adjustSize()

            self._wrapper = QScrollArea(self)
            self._wrapper.setWidget(self._label)
            self._wrapper.setMaximumHeight(self._label.height()+2)
            self._scroll = self._parent.uni_scroller(self._wrapper)

            self._layout.addWidget(self._checkbox)
            self._layout.addWidget(self._label)

        def setText(self, new_text: str):
            self._label.setText(new_text)
            self._label.adjustSize()
            self._wrapper.setMaximumHeight(self._label.height()+2)

        """def setup_scroll(self, scroll: QScroller):
            self._scroll = scroll"""
        


