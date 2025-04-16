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

from modules.eventlist.eventitem import EventItem, EDescription, EToDo, EBody, EventType
import modules.scrollers_qt as scrollFuncs

class Ui_event_item(object):
    def setupUi(self, event_item: EventItem):
        if not event_item.objectName():
            event_item.setObjectName(u"event_item")
        event_item.resize(0, 0)
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
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
        self.event_body = EBody(self)
        self.event_body.setObjectName("event_body")

        self.footer = QWidget(event_item)
        self.footer.setObjectName(u"footer")

        self.retranslateUi(event_item)

        QMetaObject.connectSlotsByName(event_item)
    # setupUi

    def formatUi(self, Type: EventType):
        if (Type == self.format): return
        self.format = Type
        if (Type == EventType.Simple):
            self.header_layout.addWidget(self.event_title_wrapper)
            self.header_layout.addWidget(self.event_time)
            self.layout.addWidget(self.header)
            self.layout.addWidget(self.event_body)

    def retranslateUi(self, event_item: EventItem):
        event_item.setWindowTitle(QCoreApplication.translate("event_item", u"Form", None))
    # retranslateUi

class Ui_event_body(object):
    def setupUi(self, event_body: EBody):
        if not event_body.objectName():
            event_body.setObjectName(u"event_body")
        event_body.resize(0, 0)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum))
        
        self.container = QVBoxLayout(event_body)
        self.container.setObjectName(u"event_body_container")
        self.container.setSpacing(4)
        self.container.setContentsMargins(0,0,0,0)

        event_body.setLayout(self.container)

        QMetaObject.connectSlotsByName(event_body)
    # setupUi
    
    def retranslateUi(self, event_body: EBody):
        event_body.setWindowTitle(QCoreApplication.translate("event_body", u"Form", None))
    # retranslateUi

class Ui_event_description(object):
    def setupUi(self, event_description: EDescription):
        if not event_description.objectName():
            event_description.setObjectName(u"event_description")
        event_description.resize(0, 0)
        event_description.setMaximumHeight(60)
        
        self.label = QLabel(event_description)
        self.label.setObjectName(u"event_description_label")
        self.label.setWordWrap(True)
        self.label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(20)
        Font.setBold(True)

        self.wrapper = QScrollArea(event_description)
        self.wrapper.setObjectName(u'event_description_wrapper')
        self.wrapper.setSizePolicy(QSizePolicy.Policy.Maximum,      
                                   QSizePolicy.Policy.MinimumExpanding)
        self.wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.wrapper_scroller = scrollFuncs.returnUniScroller(self.wrapper)
        self.wrapper_scroller.setObjectName(u"event_description_wrapper_scroller")

        self.wrapper.setWidget(self.label)

        self.retranslateUi(event_description)

        QMetaObject.connectSlotsByName(event_description)
    # setupUi

    def retranslateUi(self, event_description: EDescription):
        event_description.setWindowTitle(QCoreApplication.translate("event_description", u"event_description", None))
        self.label.setText(QCoreApplication.translate("event_description", u"Description", None))
    # retranslateUi

class Ui_event_todo(object):
    def setupUi(self, event_todo: EToDo):
        if not event_todo.objectName():
            event_todo.setObjectName(u"event_todo")
        event_todo.resize(0, 0)
        event_todo.setMaximumHeight(50)

        self.layout = QHBoxLayout(event_todo)
        self.layout.setSpacing(10)
        self.layout.setObjectName(u"event_todo_layout")
        self.layout.setContentsMargins(0,0,0,0)

        self.label = QLabel(event_todo)
        self.label.setObjectName(u"event_todo_label")
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(30)
        Font.setBold(True)
        self.label.setFont(Font)

        self.label_wrapper = QScrollArea(event_todo)
        self.label_wrapper.setWidget(self.label)
        self.label_wrapper.setMaximumHeight(self.label.height()+2)
        self.label_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_wrapper_scroller = scrollFuncs.returnUniScroller(self.label_wrapper)

        self.layout.addWidget(self.label_wrapper)

        self.checkbox = QCheckBox(event_todo)
        self.checkbox.setObjectName(u"event_todo_checkbox")

        self.layout.addWidget(self.checkbox)

        self.retranslateUi(event_todo)
    # setupUi

    def retranslateUi(self, event_description: EDescription):
        event_description.setWindowTitle(QCoreApplication.translate("event_todo", u"event_todo", None))
        self.label.setText(QCoreApplication.translate("event_todo", u"Task", None))
    # retranslateUi