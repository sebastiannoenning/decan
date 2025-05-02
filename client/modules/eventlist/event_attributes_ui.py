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
                               QWidget, QTextEdit, QScrollArea, QLabel, QCheckBox, QSizePolicy, QDataWidgetMapper, QFrame,
                               QScrollArea, QAbstractScrollArea, QScroller, QScrollerProperties, QStyleOption, QStyle)
from PySide6.QtGui import (QFont, QMouseEvent, QPainter)

import modules.scrollers_qt as scrQt

class Ui_event_body(object):
    def setupUi(self, event_body):
        if not event_body.objectName():
            event_body.setObjectName(u"event_body")
        event_body.resize(0,0)
        event_body.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred))
        
        self.container = QVBoxLayout(event_body)
        self.container.setObjectName(u"event_body_container")
        self.container.setSpacing(10)
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
        event_description.setMinimumHeight(30)
        event_description.setMaximumHeight(200)
        event_description.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))

        self.container = QVBoxLayout(event_description)
        self.container.setObjectName(u"event_description_container")
        self.container.setSpacing(0)
        self.container.setContentsMargins(0,0,0,0)

        event_description.setLayout(self.container)

        self.text = QTextEdit(event_description)
        self.text.setObjectName(u"event_description_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.text.setSizePolicy(sizePolicy)
        self.text.setSizeAdjustPolicy(QScrollArea.SizeAdjustPolicy.AdjustToContents)
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(18)
        Font.setBold(False)
        self.text.setFont(Font)
        self.text.setReadOnly(True)
        self.text.setFrameShape(QFrame.Shape.NoFrame)
        self.text.setFrameShadow(QFrame.Shadow.Plain)
        self.text.setLineWidth(0)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text.horizontalScrollBar().setEnabled(False)
        self.text.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.text.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoBulletList)
        self.text_scroller = scrQt.returnUniScroller(self.text)
        self.text_scroller.setObjectName(u"event_description_text_scroller")
        self.text.setStyleSheet(
"""
QTextEdit{
	border-radius: 5px;
	background-color: rgba(20,20,20,1);
	border: 2px solid rgba(75,150,255,1);
}

QScrollBar:vertical {
	border-left: 2px solid rgba(70,150,255,1);
    background: rgba(40,40,40,0.9);
    width:  24px;
    padding: 25px 0;
}

QScrollBar::groove:vertical {
    background: transparent;
    width: 20px;
}
QScrollBar::handle:vertical {
    	background: rgba(120,120,120,1);
    	min-height: 50px;
	min-width: 20px;
	max-width: 20px;
    	border-radius: 4px;
}

QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {
    	background: rgba(40,40,40,1);
}

QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
    	width: 20px;
    	height: 25px;             
    	background: rgba(20,20,20,1);
}

QScrollBar::sub-line:vertical {
    	subcontrol-origin: margin;
    	subcontrol-position: top;
    	border-top-left-radius: 4px;
    	border-top-right-radius: 4px;
}

QScrollBar::add-line:vertical {
    subcontrol-origin: margin;
    subcontrol-position: bottom;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
}

QScrollBar::up-arrow:vertical {
    image: url(":/icons/arrows/arrow_up_dark.svg");
    width:  20px;   height: 20px;
}
QScrollBar::up-arrow:vertical:pressed {
    image: url(":/icons/arrows/arrow_up_blue.svg");
}
QScrollBar::down-arrow:vertical {
    image: url(":/icons/arrows/arrow_down_dark.svg");
    width:  20px;   height: 20px;
}
QScrollBar::down-arrow:vertical:pressed {
    image: url(":/icons/arrows/arrow_down_blue.svg");
}
""")
        self.container.addWidget(self.text)

        self.retranslateUi(event_description)

        QMetaObject.connectSlotsByName(event_description)
    # setupUi

    def retranslateUi(self, event_description):
        event_description.setWindowTitle(QCoreApplication.translate("event_description", u"event_description", None))
        self.text.setText(QCoreApplication.translate("event_description", u"Description", None))
    # retranslateUi

class Ui_event_todo(object):
    def setupUi(self, event_todo):
        if not event_todo.objectName():
            event_todo.setObjectName(u"event_todo")
        event_todo.resize(0, 0)
        event_todo.setMinimumHeight(56)
        event_todo.setMaximumHeight(56)
        event_todo.setSizePolicy(QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum))
        event_todo.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        event_todo.setStyleSheet(
f"""
background-color: rgba(20,20,20,1);  
border-radius: 4px;
border: 2px solid rgba(80,160,100,1);""")

        self.layout = QHBoxLayout(event_todo)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"event_todo_layout")
        self.layout.setContentsMargins(2,2,2,2)

        self.task_label = QLabel(event_todo)
        self.task_label.setObjectName(u"event_task_label")
        self.task_label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(30)
        self.task_label.setFont(Font)
        self.task_label.setText(('Task'))
        self.task_label.setStyleSheet(
"""
background-color: transparent;
border: none;
padding-top: 14px;""")

        self.task_label_wrapper = QScrollArea(event_todo)
        self.task_label_wrapper_container = QWidget()
        self.task_label_wrapper_container.setObjectName(u"task_label_wrapper_container")
        self.task_label_wrapper_container.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.task_label_wrapper_container.setMaximumHeight(50)
        self.task_label_wrapper_container_layout = QVBoxLayout(self.task_label_wrapper_container)
        self.task_label_wrapper_container_layout.setObjectName(u"task_label_wrapper_container_layout")
        self.task_label_wrapper_container_layout.setSpacing(0)
        self.task_label_wrapper_container_layout.setContentsMargins(0,0,0,2)
        self.task_label_wrapper_container_layout.addWidget(self.task_label)
        self.task_label_wrapper.setWidget(self.task_label_wrapper_container)
        self.task_label_wrapper.setMaximumHeight(self.task_label_wrapper_container.height()+4)
        self.task_label_wrapper.setWidgetResizable(True)
        self.task_label_wrapper.verticalScrollBar().setEnabled(False)
        self.task_label_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.task_label_wrapper.setStyleSheet(
"""
* {
    background-color: rgba(20, 20, 20, 1);
    border: none;
    border-radius: 4px
} QScrollBar {
    height: 0px;
    width: 0px;
}""")

        self.layout.addWidget(self.task_label_wrapper)

        self.checkbox = QCheckBox(event_todo)
        self.checkbox.setText('')
        self.checkbox.setObjectName(u"event_todo_checkbox")
        self.checkbox.setMinimumHeight(48)
        self.checkbox.setMinimumWidth(48)
        self.checkbox.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.checkbox.resize(48,48)
        self.checkbox.adjustSize()
        self.checkbox.setStyleSheet(
""" * {
    background-color: transparent;
    border: none;
    margin: 0px;
    padding: 0px;
}
QCheckBox::indicator {
    margin: 0px;
    padding: 0px;
	height: 48px; width: 48px;
}""")
        self.layout.addWidget(self.checkbox)

        self.todo_label = QLabel(event_todo)
        self.todo_label.setObjectName(u"event_todo_label")
        Font2 = QFont()
        Font2.setPointSize(13)
        Font2.setBold(True)
        self.todo_label.setFont(Font2)
        self.todo_label.setText('To-do:')
        self.todo_label.setGeometry(0,0,50,19)
        self.todo_label.resize(50,19)
        self.todo_label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.todo_label.setStyleSheet(
"""
background-color: transparent;
border: none;
padding: 0px;
padding-left: 5px;
padding-top: 5px;
""")

        self.retranslateUi(event_todo)
    # setupUi

    def retranslateUi(self, event_todo):
        event_todo.setWindowTitle(QCoreApplication.translate("event_todo", u"event_todo", None))
        self.task_label.setText(QCoreApplication.translate("event_todo", u"Task", None))
        self.todo_label.setText(QCoreApplication.translate("event_todo", u"To-do:", None))
    # retranslateUi