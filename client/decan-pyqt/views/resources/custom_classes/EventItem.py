# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties
from PySide6.QtGui import QFont

class EventItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        _layout = QVBoxLayout()
        self.setLayout(_layout)

        _header = QHBoxLayout()
        _midsection = QScrollArea()
        _footer = QLabel('Hello')

        _header1 = QScrollArea()
        _header1text = QLabel('EventTitle, EventTitle, EventTitle, EventTitle')
        _header1.setWidget(_header1text)
        _header1.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        _header1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        _header1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        _header1scroll = QScroller.scroller(_header1.viewport())
        _header1scroll.grabGesture(_header1.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)

        _header2 = QLabel('00:00')

        _headerfont = QFont()
        _headerfont.setFamilies([u"Arial"])
        _headerfont.setPointSize(20)
        _header1text.setFont(_headerfont)
        _header2.setFont(_headerfont)

        _header1text.adjustSize()
        _header1.setMaximumHeight(_header1text.height())
        _header2.adjustSize()
        _header2.setMaximumWidth(_header2.width())

        _header.addWidget(_header1, 0)
        _header.addWidget(_header2, 0)

        _midsection.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        _midsection.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        _midsectiontext = QLabel('Brown dog, brown dog, brown dog, brown dog, brown dog, brown dog, brown dog, brown dog, brown dog')
        _midsectiontext.setWordWrap(True)
        _midsection.setWidget(_midsectiontext)

        _midsectionscroll = QScroller.scroller(_midsection.viewport())
        _midsectionscroll.grabGesture(_midsection.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)

        _layout.addLayout(_header, 0)
        _layout.addWidget(_midsection, 1)
        _layout.addWidget(_footer, 0)


        pass

    #def setup_details(self):
        #nothing