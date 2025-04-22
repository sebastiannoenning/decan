import datetime
import json
from enum import Enum
from typing import List, Dict, Tuple, Union, Optional, Any

# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, Signal, 
                            QJsonDocument, QJsonValue,
                            QByteArray, QModelIndex, Property,
                            QDateTime, QDate, QTime, 
                            QSize)
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, 
                               QWidget, QScrollArea, QLabel, QCheckBox, 
                               QSizePolicy,
                               QDataWidgetMapper,
                               QScroller, QScrollerProperties, QStyleOption, QStyle)
from PySide6.QtGui import (QFont, QMouseEvent, QPainter)

class EventJsonParser(QObject):
    attributesChanged = Signal()

    def __init__(self, /, 
                 parent = ..., 
                 *, 
                 objectName = ...):
        super().__init__(parent, 
                         objectName=objectName)
        self.info:          Dict[str, Union[int, str]]      = {}  
        self.positions:     Dict[int, str]                  = {}
        self.objects:       Dict[str, Union[
                                            str,                        # Either of type string
                                            Dict[                       # Or Subdictionary;
                                                str,                    # Key
                                                Union[                  # Value:
                                                    str,                    # string
                                                    bool                    # boolean
                                                ]
                                            ]
                                        ]
                                    ]                       = {}

    def setSubProperty(self, key: str, value: Union[str, Dict[str, bool]]):
        self.objects.update()
        pass

    def Objects(self): return self.objects
    def Object(self, key: str): return self.objects[key]

    def Info(self): return self.info
    def Info(self, key: str): return self.info[key]

    def Positions(self): return self.positions
    def Position(self, key: int): return self.positions[key]
        
    @Property(QByteArray)
    def Attributes(self): return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes: QByteArray):
        if (self._Attributes != Attributes):
            self._Attributes = Attributes
            if (QJsonDocument.fromJson(self._Attributes).object() != self._Json): self._updateJson()
            self.attributesChanged.emit()