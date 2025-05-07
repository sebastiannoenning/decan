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

from modules.eventlist.eventtype import EventType

class ObjectType(Enum):
    EDescription    = 0, 'EDescription'
    EToDo           = 1, 'EToDo'
    Invalid         = 2, 'Invalid'

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]

class EventJsonParser(QWidget):
    """ Object for connecting a json file to, & then """
    objectsAdded = Signal(list)
    objectsUpdated = Signal(list)
    objectsRemoved = Signal(list)
    objectsMoved = Signal(list)

    typeChanged = Signal(EventType)

    finishedEditing = Signal()

    def __init__(self, /, 
                 parent):
        super().__init__(parent=parent)
        self.resize(0,0)
        self.setMaximumSize(0,0)
        self.hide()

        self._attributes:   Optional[Union[QByteArray, str]]= None

        self._info:         Dict[str, int]                  = {}  
        self._positions:    List[str]                       = []
        self._objects:      Dict[str, Union[
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

        self._info.update({"types": ["Simple", "Complex", "Note", "Task"]})

    def _update(self, test_en: bool = False):
        """ Updates the internal dicts & converts them into internal objects """
        new_json:       dict                = json.loads(self._attributes)
        if new_json is None: raise Exception('Attributes loaded empty file')

        new_info:       Dict[str, int]      = new_json.get('info', {})
        new_positions:  List[str]           = new_json.get('positions')
        new_objects:    Dict[str, Any]      = new_json.get('objects', {})

        if test_en: print('Info: ', new_info)
        if test_en: print('Objects: ',new_objects)
        if test_en: print('Positions: ', new_positions)

        description_count, todo_count = 0, 0

        # Lists for tracking all changes made to the items
        added:      List[str]           = []
        updated:    List[str]           = []
        unchanged:  List[str]           = []
        removed:    List[str]           = []
        moved:      List[str]           = []

        largest_val = 0

        if isinstance(new_positions, str):
            try:
                new_positions = json.loads(new_positions)
            except json.JSONDecodeError:
                print("Error parsing positions JSON:", new_positions)
                new_positions = []
        # Parse objects if it's a string
        if isinstance(new_objects, str):
            try:
                new_objects = json.loads(new_objects)
            except json.JSONDecodeError:
                print("Error parsing objects JSON:", new_objects)
                new_objects = {}

        if new_objects is not None:
            for key, value in new_objects.items():
                # Check formatting
                obj_text, index       = key.rsplit('_', 1)
                obj_format: ObjectType  = self.strToObjectType(obj_text)
                index:  int         = int(index)
                largest_val = max(index, largest_val)

                if obj_format == ObjectType.EDescription:
                    value = self.formatEDescription(value)
                    description_count += 1
                elif obj_format == ObjectType.EToDo:
                    value = self.formatEToDo(value)
                    description_count += 1

                # Pull the previous/old value (if it exists)
                old_value: Union[str, dict] = self._objects.get(key)

                if old_value is None:    # Key doesn't exist
                    self._objects.update({key : value})
                    added.append(key)
                elif old_value != value:   # Key exists but the value mismatches
                    self._objects.update({key : value})
                    updated.append(key)
                elif old_value == value:   # Key exists & the value matches
                    unchanged.append(key)

        # Append any keys not in new_objects to removed & subsequently pop them from self._objects
        for key in self._objects.keys():
            if (key in added) or (key in updated) or (key in unchanged): pass
            else:
                removed.append(key)
        for key in removed:
            self._objects.pop(key)
            self._positions.remove(key)

        if new_positions is not None:
            # Check if new_positions is a string and convert it to a list if necessary
            if isinstance(new_positions, str):
                # If it's a string, we can't use pop() on it, so we'll create a new list
                new_positions = []

            # I.e, if new_objects is empty & thus self._objects will be as well
            if not new_objects: self._positions.clear() # Pre-emptively clear self._positions(), as it won't have any objects to track regardless
            else:
                # Find all the invalid indices
                invalid_indices = (tuple(index 
                                         for index, key in enumerate(new_positions) 
                                         if (key in removed) or (key not in new_objects)
                                         )
                                         )[::-1] # Flip backwards to iterate through
                for index in invalid_indices: new_positions.pop(index) # & then remove the invalid indices

                # P(reserved) O(bjects) positions are accumulated in two seperate dictionaries for comparison
                PO_new_pos = {key: index for index, key in enumerate(new_positions) if key in updated}
                PO_old_pos = {key: index for index, key in enumerate(self._positions) if key in updated}

                # Record all moved keys
                moved = [key for key in PO_old_pos if (key in PO_new_pos) and PO_old_pos[key] != PO_new_pos[key]]

                self._positions.clear()
                self._positions = new_positions.copy()

        # Add any new keys that haven't been added to the position board (just in case)
        for key in self._objects.keys():
            if key not in new_positions:
                self._positions.append(key)

        if added:
            if test_en: print('Added: ',added)
            self.objectsAdded.emit(added)           # Call linked widgets to add the new objects
        if updated:
            if test_en: print('Updated: ', updated)
            self.objectsUpdated.emit(updated)       # Call linked widgets to update the changed objects
        if unchanged:
            if test_en: print('Unchanged: ', unchanged)
        if removed:
            if test_en: print('Removed: ', removed)
            self.objectsRemoved.emit(removed)       # Call linked widgets to remove the deleted objects
        if moved:
            if test_en: print('Moved: ', moved)
            self.objectsMoved.emit(moved)           # Call linked widgets to check their layouts & move any linked widgets

        if new_info is not None and isinstance(new_info, dict):
            new_index = new_info.get('index')
            new_increment = new_info.get('increment')
            new_type = new_info.get('type')

            if len(new_objects) != new_index:
                new_index = len(new_objects)
            new_increment = max(largest_val, new_increment)

            self._info.update({'index':      new_index})
            self._info.update({'increment':  new_increment})
            self._info.update({'type':       new_type})

        if test_en: print('Info: ', self._info)
        if test_en: print('Positions: ', self._positions)
        if test_en: print('Objects: ', self._objects)
        self.finishedEditing.emit()

    def formatEDescription(self, value: Union[str, dict]):
        if isinstance(value, str):   return value
        elif(isinstance(value, dict)):
            n_value = self._searchForKey(value, 'EDescription')
            if (n_value is not None):   return n_value
        return ''

    def formatEToDo(self, value: Union[str, dict]):
        new_taskdescription:   str     = ''
        new_bool:              bool    = False
        if  (isinstance(value, str)):   new_taskdescription = value
        elif(isinstance(value, dict)):
            temp_taskdesc:    str    = str(self._searchForKey(value, 'ETaskDescription'))
            temp_bool:        bool   = bool(self._searchForKey(value, 'EBool'))
            if (temp_taskdesc is not None):   new_taskdescription    = temp_taskdesc
            if (temp_bool is not None):       new_bool               = temp_bool
        new_todo: Dict[str, Union[str, bool]] = {}
        new_todo.update({'ETaskDescription': new_taskdescription})
        new_todo.update({'EBool': new_bool})
        return new_todo

    def intToEventType(self, format: int):
        EventTypeLookup : List[EventType] = [EventType.Simple, EventType.Complex, EventType.Note, EventType.Task]
        return EventTypeLookup[format]

    def strToObjectType(self, format: str):
        if  (format == 'EDescription'): return ObjectType.EDescription
        elif(format == 'EToDo'):        return ObjectType.EToDo
        else:                           return ObjectType.Invalid

    def setObjectProperty(self, key: str, value: Union[str, Dict[str, bool]]):
        format, index = key.split('_',1)
        format = self.strToObjectType(format)
        if (format == ObjectType.EDescription): value = self.formatEDescription(value)
        elif (format == ObjectType.EToDo):      value = self.formatEToDo(value)
        self._objects.update({key: value})

        self.exportChanges()

    def _searchForKey(self, s_dict: dict, key: str):
        """ Recursive dict search function that searches for a field in a dictionary & if found the value associated """
        if key in s_dict: return s_dict[key]

        for val in s_dict.values():             
            if isinstance(val, dict):
                value = self._searchForKey(val, key)
                if (value is not None):
                    return value
                else:
                    return None

    def exportChanges(self):
        export = {
                'info'      : self._info,
                'positions' : self._positions,
                'objects'   : self._objects
            }
        json_text = json.dumps(export, ensure_ascii=False, indent=2)
        if      isinstance(self._attributes, QByteArray): self._attributes = QByteArray(json_text.encode("utf-8"))
        elif    isinstance(self._attributes, str):        self._attributes = json_text

    # Getters for Objects
    def Objects(self): return self._objects
    def Object(self, key: str): return self._objects[key]

    # Getters for Info
    def Info(self): return self._info
    def InfoAt(self, key: str): return self._info[key]

    # Getters for Positions 
    def Positions(self): return self._positions
    def Position(self, key: str): return self._positions.index(key)

    # Property Attributes
    @Property(str)
    def Attributes(self): return self._attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        if self._attributes != Attributes:
            self._attributes = Attributes
            self._update()
