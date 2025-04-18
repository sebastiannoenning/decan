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
from modules.eventlist.eventattributes import EBody
import modules.scrollers_qt as scrollFuncs

class Ui_event_item(object):
    def setupUi(self, event_item):
        if not event_item.objectName():
            event_item.setObjectName(u"event_item")
        event_item.resize(0, 0)
        event_item.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.format = EventType.Simple

        # Central Container
        self.layout = QVBoxLayout(event_item)
        self.layout.setSpacing(4)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Header
        self.header = QWidget(event_item)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0) #etc
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(0,0))
        self.header.setStyleSheet(u"")
        # Header_layout
        self.header_layout = QVBoxLayout(self.header)
        self.header_layout.setSpacing(10)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(0, 0, 0, 0)

        # Event Title
        self.event_title = QLabel(event_item)
        self.event_title.setObjectName(u"event_title")
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(24)
        self.event_title.setFont(Font)
        self.event_title_wrapper = QScrollArea(event_item)
        self.event_title_wrapper.setObjectName(u"event_title_wrapper")
        self.event_title_wrapper.setWidget(self.event_title)
        self.event_title_wrapper.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.event_title_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.event_title_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.event_title_wrapper.setWidgetResizable(True)
        self.event_title_wrapper_scroller = scrollFuncs.returnUniScroller(self.event_title_wrapper)
        self.event_title_wrapper_scroller.setObjectName(u"event_title_wrapper_scroller")
        # Event Time
        self.event_time = QLabel(event_item)
        self.event_time.setObjectName(u"event_time")
        Font1 = QFont()
        Font1.setFamilies([u"Arial"])
        Font1.setPointSize(24)
        self.event_time.setFont(Font1)
        # Event Location
        self.event_location = QLabel(event_item)
        self.event_location.setObjectName(u"event_location")
        Font2 = QFont()
        Font2.setFamilies([u"Arial"])
        Font2.setPointSize(24)
        self.event_location.setFont(Font2)
        # Event Body
        self.event_body = EBody(event_item)
        self.event_body.setObjectName("event_body")

        self.footer = QWidget(event_item)
        self.footer.setObjectName(u"footer")

        self.retranslateUi(event_item)

        QMetaObject.connectSlotsByName(event_item)
    # setupUi

    def formatUi(self, Type: EventType = EventType.Simple):
        if (Type == self.format): return
        self.format = Type
        if (Type == EventType.Simple):
            self.header_layout.addWidget(self.event_title_wrapper)
            self.header_layout.addWidget(self.event_time)
            self.layout.addWidget(self.header)
            self.layout.addWidget(self.event_body)

    def retranslateUi(self, event_item):
        event_item.setWindowTitle(QCoreApplication.translate("event_item", u"Form", None))
    # retranslateUi