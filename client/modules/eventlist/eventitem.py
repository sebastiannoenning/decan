import datetime
import json
from enum import Enum
from typing import List, Dict, Tuple, Union

# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, Signal, 
                            QJsonDocument, QJsonValue,
                            QByteArray, QModelIndex, Property, QPersistentModelIndex,
                            QSize)
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, 
                               QWidget, QScrollArea, QLabel, QCheckBox, QSizePolicy, QDataWidgetMapper,
                               QScroller, QScrollerProperties, QStyleOption, QStyle)
from PySide6.QtGui import (QFont, QMouseEvent, QPainter)

from models.event_model import EventModel

from modules.eventlist.event_item_ui import Ui_event_item

from modules.eventlist.eventattributes import EBody
from modules.eventlist.eventtype import EventType
from modules.eventlist.eventjsonparser import EventJsonParser

class EventItem(QWidget):
    mousePressed = Signal(QWidget)

    def __init__(self, parent=None, model=None, index=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        self._Ui = Ui_event_item()
        self._Ui.setupUi(self)
        #self._Ui.formatUi(self, event_type=EventType.Simple)

        self._mapper    :QDataWidgetMapper      = QDataWidgetMapper(parent=self)
        if model is not None: self._mapper.setModel(model)

        self._jsonParser = EventJsonParser(self)

        self._Ui.event_body.setJsonParser(self._jsonParser)

        self._setupMappings()

        self._index     :QModelIndex           = index
        if index is not None:
            self._mapper.setCurrentModelIndex(index)


    def setModel(self, model: EventModel):              self._mapper.setModel(model)
    def setCurrentModelIndex(self, index: QModelIndex): self._mapper.setCurrentModelIndex(index)
    def setCurrentIndex(self, row: int):                self._mapper.setCurrentIndex(row)
    def currentIndex(self):                             self._mapper.currentIndex()

    def _setupMappings(self): # Sets mappings to each ui object generated via the _setup_Ui
        self._mapper.addMapping(self._Ui.event_title, 1, QByteArray("text"))
        print(f'{self.objectName()}_{hex(id(self))} added mapping to _eventTitle')
        self._Ui.event_time.addMappings(self._mapper, 2, 3)
        print(f'{self.objectName()}_{hex(id(self))} added mapping to _eventTime')
        self._mapper.addMapping(self._jsonParser, 4, QByteArray("Attributes"))
        print(f'{self.objectName()}_{hex(id(self))} added mapping to _jsonParser/_eventBody')
        self._mapper.addMapping(self._Ui.event_location, 6)

        self._mapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy.AutoSubmit)

    def mousePressEvent(self, event):
        # Check if the left mouse button was pressed
        if event.button() == Qt.MouseButton.LeftButton:
            # Change the background color to a new color
            self.mousePressed.emit(self)
            #print('mouse pressed!')

        # Call the base class implementation to ensure the event is handled correctly
        super().mousePressEvent(event)

    def setObjectName(self, name, /):
        self.setStyleSheet(f"""
        QWidget#{name} {{
            border-radius: 4px;
            background-color: rgba(30,30,30,1);
        }}""")
        return super().setObjectName(name)

    def paintEvent(self, pe):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)