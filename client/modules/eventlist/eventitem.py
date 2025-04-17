import datetime
import json
from enum import Enum
from typing import List, Dict, Tuple, Union

# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, Signal, 
                            QJsonDocument, QJsonValue,
                            QByteArray, QModelIndex, Property)
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, 
                               QWidget, QScrollArea, QLabel, QCheckBox, QSizePolicy, QDataWidgetMapper,
                               QScroller, QScrollerProperties, QStyleOption, QStyle)
from PySide6.QtGui import (QFont, QMouseEvent, QPainter)

from models.event_model import EventModel
from modules.eventlist.event_item_ui import Ui_event_item
from modules.eventlist.eventtype import EventType

class EventItem(QWidget):

    """A "EventItem" widget with an several labels.

    Attributes:
        _layout: The QVBoxLayout containing all the nested labels
        _event: The Event object with the attributes for the labels
        EID : EventID
        ETitle: EventTitle
        ETime: Event Time
        Attributes: Event Attributes 

    Signals:
    """

    mousePressed = Signal(QObject)
    itemChanged = Signal(QObject)
        
    def __init__(self,
                 parent     : QObject       = None, 
                 model      : EventModel    = None, 
                 row        : QModelIndex   = None):
        super().__init__(parent)
        self._Ui = Ui_event_item()
        self._Ui.setupUi(self)
        self._Ui.formatUi(Type=EventType.Simple)

        self._mapper    :QDataWidgetMapper      = QDataWidgetMapper(parent=self)
        if (model is not None): self._mapper.setModel(model)
        self._index     :QModelIndex           = row
        if (row is not None): self._mapper.setRootIndex(row)

        self._setupMappings()

    def setModel(self, model: EventModel): 
        self._mapper.setModel(model)

    def setModelIndex(self, index: QModelIndex): self._mapper.setRootIndex(index)

    def _setupMappings(self): # Sets mappings to each ui object generated via the _setup_Ui
        self._mapper.addMapping(self._Ui.event_title, 1)
        self._mapper.addMapping(self._Ui.event_time, 2)
        self._mapper.addMapping(self._Ui.event_body, 4, "Attributes")
        self._mapper.addMapping(self._Ui.event_location, 6)

        self._mapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy.AutoSubmit)

    def _formatUi(self, Type: EventType=EventType.Simple): pass

    def setModelRow(self, model: EventModel, index: QModelIndex): pass

    def mousePressEvent(self, event):
        # Check if the left mouse button was pressed
        if event.button() == Qt.MouseButton.LeftButton:
            # Change the background color to a new color
            self.mousePressed.emit(self)
            #print('mouse pressed!')

        # Call the base class implementation to ensure the event is handled correctly
        super().mousePressEvent(event)

    def paintEvent(self, pe):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self) 


