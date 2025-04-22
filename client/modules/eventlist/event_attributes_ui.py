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

import modules.scrollers_qt as scrQt

class Ui_event_body(object):
    def setupUi(self, event_body):
        if not event_body.objectName():
            event_body.setObjectName(u"event_body")
        event_body.resize(0, 0)
        event_body.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum))
        
        self.container = QVBoxLayout(event_body)
        self.container.setObjectName(u"event_body_container")
        self.container.setSpacing(4)
        self.container.setContentsMargins(0,0,0,0)

        event_body.setLayout(self.container)

        QMetaObject.connectSlotsByName(event_body)
    # setupUi
    
    def retranslateUi(self, event_body):
        event_body.setWindowTitle(QCoreApplication.translate("event_body", u"Form", None))
    # retranslateUi

class Ui_event_description(object):
    def setupUi(self, event_description):
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
        self.wrapper_scroller = scrQt.returnUniScroller(self.wrapper)
        self.wrapper_scroller.setObjectName(u"event_description_wrapper_scroller")

        self.wrapper.setWidget(self.label)

        self.retranslateUi(event_description)

        QMetaObject.connectSlotsByName(event_description)
    # setupUi

    def retranslateUi(self, event_description):
        event_description.setWindowTitle(QCoreApplication.translate("event_description", u"event_description", None))
        self.label.setText(QCoreApplication.translate("event_description", u"Description", None))
    # retranslateUi

class Ui_event_todo(object):
    def setupUi(self, event_todo):
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
        self.label_wrapper_scroller = scrQt.returnUniScroller(self.label_wrapper)

        self.layout.addWidget(self.label_wrapper)

        self.checkbox = QCheckBox(event_todo)
        self.checkbox.setObjectName(u"event_todo_checkbox")

        self.layout.addWidget(self.checkbox)

        self.retranslateUi(event_todo)
    # setupUi

    def retranslateUi(self, event_description):
        event_description.setWindowTitle(QCoreApplication.translate("event_todo", u"event_todo", None))
        self.label.setText(QCoreApplication.translate("event_todo", u"Task", None))
    # retranslateUi