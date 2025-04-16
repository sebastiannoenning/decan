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

from modules.eventlist.eventlist import EventList
import modules.scrollers_qt as scrollFuncs

class Ui_event_list(object):
    def setupUi(self, event_list: EventList):
        if not event_list.objectName():
            event_list.setObjectName(u"event_list")
        event_list.resize(0, 0)
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        # Central Container
        self.container = QVBoxLayout(event_list)
        self.container.setSpacing(0)
        self.container.setObjectName(u"container")
        self.container.setContentsMargins(0, 0, 0, 0)
        event_list.setLayout(self.container)

        self.retranslateUi(event_list)

        QMetaObject.connectSlotsByName(event_list)
    # setupUi

    def retranslateUi(self, event_list: EventList):
        event_list.setWindowTitle(QCoreApplication.translate("event_list", u"Form", None))
    # retranslateUi