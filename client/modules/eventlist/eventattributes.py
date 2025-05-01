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

from client.modules.eventlist.event_attributes_ui import Ui_event_description, Ui_event_todo, Ui_event_body

from client.modules.datetime_qt import date_to_fs_long, time_to_fs

from client.modules.eventlist.eventjsonparser import EventJsonParser, ObjectType
 
import client.modules.scrollers_qt as scr_qt

class EBody(QWidget):
    """ Provides a UI representation of an associated 
    """
    sizeChanged = Signal(QSize)
    itemsChanged = Signal()
    hasItems = Signal(bool)

    def __init__(self, parent, 
                 jsonParser: EventJsonParser = None):
        super().__init__(parent)
        self._jsonParser: Optional[EventJsonParser] = None
        if jsonParser is not None: self._jsonParser = jsonParser
        if self._jsonParser is not None: self.setConnections()

        self._Ui = Ui_event_body()
        self._Ui.setupUi(self)

        # Internal data list for pulling key associated with object, to provide ease of use on moving or changing the values inside.
        self._Items         : Dict[str, Union[EToDo, EDescription]] = {}

    def setJsonParser(self, jsonParser: EventJsonParser):
        # Calling will clear all existing items in the EBody & import all the items directly from the new jsonParser
        if self._Items: self.clearAll()
        self.removeConnections()
        self._jsonParser = jsonParser
        self.setConnections()
        self.importAll()
        self.checkState()

    def removeConnections(self, test_en: bool=False):
        try: self._jsonParser.objectsAdded.disconnect(self.addItems)
        except Exception as e: 
            if test_en: print('removeConnections()->objectsAdded.disconnect()  error: Was not connected,',e)
        try: self._jsonParser.objectsUpdated.disconnect(self.updateItems)
        except Exception as e: 
            if test_en: print('removeConnections()->objectsUpdateddisconnect()  error: Was not connected,',e)
        try: self._jsonParser.objectsRemoved.disconnect(self.removeItems)
        except Exception as e: 
            if test_en: print('removeConnections()->objectsRemoved.disconnect() error: Was not connected,',e)
        try: self._jsonParser.objectsMoved.disconnect(self.moveItems)
        except Exception as e: 
            if test_en: print('removeConnections()->objectsMoved.disconnect() error: Was not connected,',e)

    def setConnections(self):
        if self._jsonParser:
            self._jsonParser.objectsAdded.connect(lambda added: self.addItems(new_items=added))
            self._jsonParser.objectsUpdated.connect(lambda updated: self.updateItems(updated_items=updated))
            self._jsonParser.objectsRemoved.connect(lambda removed: self.removeItems(removed_items=removed))
            self._jsonParser.objectsMoved.connect(lambda moved: self.moveItems(moved_items=moved))

            self._jsonParser.finishedEditing.connect(lambda: self.checkState())

    def importAll(self):
        new_objects: List[str] = self._jsonParser.Positions()
        if new_objects: self.addItems(new_objects)

    def clearAll(self):
        all_objects: List[str] = list(self._Items.keys())
        if all_objects: self.removeItems(all_objects)

    def checkState(self):
        if self._Items: self.hasItems.emit(True)
        else: self.hasItems.emit(False)

    def updateStatus(self):
        self.setMinimumHeight(self._Ui.container.minimumSize().height())
        self.adjustSize()

    def addItems(self, new_items: List[str]):
        for key in new_items:
            new_widget: Union[EToDo, EDescription, None] = None
            obj_name, index = key.split('_',1)
            obj_type: ObjectType = self._jsonParser.strToObjectType(obj_name)
            value = self._jsonParser.Object(key)

            if obj_type == ObjectType.EDescription: 
                new_widget: EDescription    = EDescription(self, key)
                value: str                          = self._jsonParser.formatEDescription(value)

                new_widget.setText(value)
            if obj_type == ObjectType.EToDo:
                new_widget:     EToDo               = EToDo(self, key)
                value:  Dict[str, Union[str, bool]] = self._jsonParser.formatEToDo(value)
                value_bool:     bool                = value.get('EBool')
                value_string:   str                 = value.get('ETaskDescription')

                new_widget.setText(value_string)
                new_widget.setChecked(value_bool)

                new_widget.checkStateChanged.connect(lambda: self._jsonParser.setObjectProperty(key, {'ETaskDescription':new_widget.text(),'EBool':new_widget.isChecked()}))

            index = self._jsonParser.Positions().index(key)

            self._Ui.container.insertWidget(index, new_widget)

            self._Items.update({key: new_widget})

        self.updateStatus()
    
    def removeItems(self, removed_items: List[str]):
        for key in removed_items:
            removed_widget  = self._Items[key]
            index           = self._Ui.container.indexOf(removed_widget)
            removed_item    = self._Ui.container.takeAt(index)
            removed_widget  = removed_item.widget()

            del removed_item
            removed_widget.deleteLater()

            self._Items.pop(key)
        
        self.updateStatus()

    def moveItems(self, moved_items: List[str]):
        for key in moved_items:
            moved_widget    = self._Items[key]
            index           = self._Ui.container.indexOf(moved_widget)
            moved_item      = self._Ui.container.takeAt(index)
            moved_widget    = moved_item.widget()
            del moved_item

            new_index = self._jsonParser.Position(key)

            self._Ui.container.insertWidget(new_index, moved_widget)

        self.updateStatus()
    
    def updateItems(self, updated_items: List[str]):
        for key in updated_items:
            update_widget: Union[EToDo, EDescription]   = self._Items[key]

            obj_name, index = key.split('_',1)
            obj_type: ObjectType = self._jsonParser.strToObjectType(obj_name)
            value = self._jsonParser.Object(key)

            if obj_type == ObjectType.EDescription:
                value: str                          = self._jsonParser.formatEDescription(value)
                update_widget.setText(value)
            elif obj_type == ObjectType.EToDo:
                update_widget.checkStateChanged.disconnect(self._jsonParser.setObjectProperty)

                value:  Dict[str, Union[str, bool]] = self._jsonParser.formatEToDo(value)
                value_bool:     bool                = value.get('EBool')
                value_string:   str                 = value.get('ETaskDescription')

                update_widget.setText(value_string)
                update_widget.setChecked(value_bool)

                update_widget.checkStateChanged.connect(lambda: self._jsonParser.setObjectProperty(key, {'ETaskDescription':update_widget.text(),'EBool':update_widget.isChecked()}))

            update_widget.adjustSize()

        self.updateStatus()


# noinspection PyTypeChecker,PyAttributeOutsideInit
class ETime(QWidget):        # Time Label that provides multiple formatting/preset-styles & real-time time updating,
    def __init__(self, parent):
        super().__init__(parent)
        self._startColumn   :int        = 0
        self._endColumn     :int        = 0

        self._allDay        :bool       = False
        self._multiDay      :bool       = False

        if not self.objectName():
            self.setObjectName(u"event_time")

        self.setupUi()

        self._startLabel.dateTimeChanged.connect(self.updateFormat())
        self._endLabel.dateTimeChanged.connect(self.updateFormat())

    def setMinimumHeight(self, minw):
        minw : int = max(minw, self._b_height)
        return super().setMinimumWidth(minw)

    def sizeHint(self):
        return QSize(self._b_height, self._b_width)

    def setupUi(self):
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self._b_height       :int        = 50    # Base height
        self._b_width        :int        = 150   # Base width

        self.label_container = QVBoxLayout()
        self.label_container.setContentsMargins(2,2,2,2)
        self.label_container.setSpacing(4)
        self.setLayout(self.label_container)

        self._startLabel                = self.ELabel(self)
        self._endLabel                  = self.ELabel(self)
        Font = QFont()
        Font.setFamilies([u"Arial"])
        Font.setPointSize(18)
        Font.setBold(False)
        self._startLabel.setObjectName("event_time_label")
        self._endLabel.setObjectName("event_time_label")

        self._startLabel.setText('Not connected')
        self._endLabel.setText('Not connected')

        self.label_container.addWidget(self._startLabel)
        self.label_container.addWidget(self._endLabel)

        self.setStyleSheet("""
ETime{
                           background-color: rgba(20,20,20,1);
                           border-radius: 5px;
                           padding: 5px;
                           
} ELabel {
                           background-color: None;
                           border-radius: 0px;
                           padding-left: 5px;
                           border: 0px solid transparent;
}""")

    def setFont(self, font: QFont):
        self._startLabel.setFont(font)
        self._endLabel.setFont(font)

        self.resize(self.label_container.minimumSize())

    def updateFormat(self):
        alldaytxt: str = '<span style="color: #ff5050; font-weight: bold;">All day</span>'

        if (self._startLabel.Time() <= QTime(0, 0, 59)) and (self._endLabel.Time() >= QTime(23, 59, 0)): 
            self._allDay = True
        else: self._allDay = False

        if self._startLabel.Date() != self._endLabel.Date():
            self._multiDay = True
        else: self._multiDay = False

        if self._allDay and self._multiDay:
            self._startLabel.setText(f'{alldaytxt}, from {date_to_fs_long(self._startLabel.Date())}')
            self._endLabel.setText(f'to {date_to_fs_long(self._endLabel.Date())}')
        elif self._allDay:
            self._startLabel.setText(self._startLabel.Date().toString('dddd d MMM yyyy'))
            self._endLabel.setText(alldaytxt)
        elif self._multiDay:
            self._startLabel.setText(f'from {date_to_fs_long(self._startLabel.Date())}')
            self._endLabel.setText(f'to {date_to_fs_long(self._endLabel.Date())}')
        else:
            self._startLabel.setText(self._startLabel.Date().toString('dddd d MMM yyyy'))
            self._endLabel.setText(f'from {time_to_fs(self._startLabel.Time())} to {time_to_fs(self._endLabel.Time())}')

    def addMappings(self, mapper: QDataWidgetMapper, col_start: int, col_end: int):
        self._startColumn = col_start
        self._endColumn = col_end
        mapper.addMapping(self._startLabel, self._startColumn, QByteArray('DateTime'))
        mapper.addMapping(self._endLabel, self._endColumn, QByteArray('DateTime'))

    def removeMappings(self, mapper: QDataWidgetMapper):
        mapper.removeMapping(self._startLabel)
        mapper.removeMapping(self._endLabel)

    def connectToWidgets(self):
        pass

    class ELabel(QLabel):
        dateTimeChanged = Signal()

        def __init__(self, parent):
            super().__init__(parent)
            self._DateTime: Optional[QDateTime] = QDateTime().currentDateTime()
            pass

        def Time(self): return self._DateTime.time()

        def Date(self): return self._DateTime.date()

        @Property(QDateTime)
        def DateTime(self): return self._DateTime
        
        @DateTime.setter
        def DateTime(self, date_time: QDateTime):
            if self._DateTime != date_time:
                self._DateTime = DateTime
                self.dateTimeChanged.emit()


class ELocation(QLabel):    # Location Label that provides travel-time recommendations 
    def __init__(self, parent):
        super().__init__(parent)
        pass

    def setModel(self, LocModel): pass

class EDescription(QWidget):    # Description addition that provides a larger, scrollable box with horizontal word-wrapping
    def __init__(self, parent, key: str = ''):
        super().__init__(parent)
        self.setObjectName(key)

        self._Ui = Ui_event_description()
        self._Ui.setupUi(self)

    def sizeHint(self): return QSize(100, 30)

    def setText(self, new_txt: str):        self._Ui.text.setText(new_txt)

    def text(self):                         return self._Ui.text.toMarkdown()

class EToDo(QWidget):           # ToDo Add-on that provides a checkable box & a specially formatted title
    checkStateChanged = Signal()

    def __init__(self, parent, key: str = ''):
        super().__init__(parent)
        self.setObjectName(key)

        self._Ui = Ui_event_todo()
        self._Ui.setupUi(self)

        self._Ui.checkbox.checkStateChanged.connect(lambda: self.checkStateChanged.emit())

        self.form_wrapper_scroller : QScroller = scr_qt.returnUniScroller(self._Ui.task_label_wrapper)

    def sizeHint(self): return QSize(200, 50)

    def setText(self, new_txt: str):        self._Ui.task_label.setText(new_txt)
    def setChecked(self, new_bool: bool):   self._Ui.checkbox.setChecked(new_bool)

    def text(self):                         return self._Ui.task_label.text()
    def isChecked(self):                    return self._Ui.checkbox.isChecked()