from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QSizePolicy, QWidget, 
                               QVBoxLayout, QHBoxLayout, QLabel)

from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, Signal, QJsonDocument, QByteArray, QModelIndex, Property)
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, 
                               QWidget, QScrollArea, QLabel, QCheckBox, QSizePolicy, QDataWidgetMapper,
                               QScrollArea, QAbstractScrollArea, QScroller, QScrollerProperties, QStyleOption, QStyle)
from PySide6.QtGui import (QFont, QMouseEvent, QPainter)

from modules.eventlist.eventtype import EventType
from modules.eventlist.eventattributes import EBody, ETime
import modules.scrollers_qt as scrQt

class Ui_event_item(object):
    def setupUi(self, event_item: QWidget):
        if not event_item.objectName():
            event_item.setObjectName(u"event_item")
        event_item.resize(0, 0)
        event_item.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        event_item.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self._eventType = EventType.Simple

        # Central Container
        self.layout = QVBoxLayout(event_item)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(4, 4, 4, 4)

        event_item.setStyleSheet(""" * { border: 0px; }""")

        # Header
        self.header = QWidget(event_item)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0) #etc
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(0,0))
        self.header.setStyleSheet(u"")
        # Header_layout
        self.header_layout = QVBoxLayout(self.header)
        self.header_layout.setSpacing(0)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(0, 0, 0, 0)

        # Event Title
        self.event_title = QLabel(event_item)
        self.event_title.setObjectName(u"event_title")
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(24)
        self.event_title.setFont(Font)
        self.event_title.setMaximumHeight(44)
        self.event_title_wrapper = QScrollArea(event_item)
        self.event_title_wrapper.setMinimumSize(QSize(312, 46))
        self.event_title_wrapper.setMaximumSize(QSize(350, 46))
        self.event_title_wrapper.setObjectName(u"event_title_wrapper")
        self.event_title_wrapper.setWidget(self.event_title)
        self.event_title_wrapper.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.event_title_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.event_title_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.event_title_wrapper.setWidgetResizable(True)
        self.event_title_wrapper_scroller = scrQt.returnUniScroller(self.event_title_wrapper)
        self.event_title_wrapper_scroller.setObjectName(u"event_title_wrapper_scroller")
        self.event_title_wrapper.setStyleSheet("""* { 
        background-color: None; 
        border-radius: 0px;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        }""")
        self.event_title_wrapper.widget().setStyleSheet('background-color: rgba(30,30,30,1)')

        # Event Time
        self.event_time = ETime(event_item)
        self.event_time.setObjectName(u"event_time")
        Font1 = QFont()
        Font1.setFamilies([u"Arial"])
        Font1.setPointSize(18)
        self.event_time.setFont(Font1)
        self.event_time.setMaximumHeight(68)
        self.event_time.setMinimumHeight(68)
        self.event_time.setStyleSheet("""* { background-color: None; }""")

        self.header_layout.addWidget(self.event_title_wrapper)
        self.header_layout.addWidget(self.event_time)

        self.layout.addWidget(self.header)

        # Event Location
        self.event_location = QLabel(event_item)
        self.event_location.setObjectName(u"event_location")
        Font2 = QFont()
        Font2.setFamilies([u"Arial"])
        Font2.setPointSize(18)
        self.event_location.setFont(Font2)
        # Event Body
        self.event_body = EBody(event_item)
        self.event_body.setObjectName("event_body")
        self.event_body.layout().setContentsMargins(0,0,0,0)
        self.event_body.layout().setSpacing(0)

        self.layout.addWidget(self.event_body)

        self.footer = QWidget(event_item)
        self.footer.setObjectName(u"footer")

        self.layout.addWidget(self.footer)

        self.event_location.hide()

        self.retranslateUi(event_item)

        QMetaObject.connectSlotsByName(event_item)
    # setupUi

    """def formatUi(self, event_item, event_type: EventType = EventType.Simple):
        if event_type == self._eventType: return
        self._eventType = event_type

        event_item.setMinimumSize(QSize(312, 300))

        if self._eventType == EventType.Simple:
            pass"""

    def retranslateUi(self, event_item):
        event_item.setWindowTitle(QCoreApplication.translate("event_item", u"Form", None))
    # retranslateUi