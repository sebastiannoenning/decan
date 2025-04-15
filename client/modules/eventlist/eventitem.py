import datetime
import json
from enum import Enum
from typing import List, Dict, Tuple

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
from modules.eventlist.event_item_ui import Ui_event_item, Ui_event_description, Ui_event_todo

class EventType(Enum):
    Complex = 0
    Simple = 1
    Description = 2
    ToDo = 3

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
                 parent: QObject=None, 
                 model: EventModel=None, 
                 row: QModelIndex=None):
        super().__init__(parent)

        self._mapper = QDataWidgetMapper(parent=self)
        if (model is not None): self._mapper.setModel(model)
        self._index = row

        self._ui = Ui_event_item()
        self._ui.setupUi(self)

    def setModel(self, model: EventModel): self._mapper.setModel(model)

    def setRow(self, index: QModelIndex): self._mapper.setRootIndex(index)

    def _setupMappings(self): # Sets mappings to each ui object generated via the _setup_ui
        self._mapper(self._ui.event_title, 1)
        self._mapper(self._ui.event_time, 2)
        self._mapper(self._ui.event_body, 4)
        self._mapper(self._ui.event_location, 8)

    def _formatUi(self, Type: EventType=EventType.Simple):
        pass

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
    
    def _update_EAttribute(self, key, value):
        self._EJSON[key] = value
        self.Attributes = QJsonDocument(self._EJSON).toJson(QJsonDocument.JsonFormat.Compact)
        self.itemChanged.emit(self)
    
    def __setup_ui(self):
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        # create vertical box layout to hold all the items
        self._layout = QVBoxLayout()
        self._layout.setSpacing(4)
        self.setLayout(self._layout)

        # Create 3 main parts for place in layout -- will add later
        self._header = QHBoxLayout()         #Top row       Features two labels - one at fixed width (for EventTitle), and another nested in a scroll-area
        #self._midsection = QScrollArea()     #Mid row       Features one label, nested inside a scroll-area
        self._footer = QLabel("Estimated travel time:")       #Bottom row

        # Header Components
        self._header.setSpacing(10)
        self._header1_wrapper = QScrollArea()               #Scroll Area
        self._header1title = QLabel(self.ETitle)           # ↪ For nested QLabel, displaying ETITLE
        self._header2time = QLabel(self.EStartTime[:5])   #QLabel, displaying ESTARTTIME

        #self._header2time.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        #   Header_1 wrapper settings 
        self._header1_wrapper.setWidget(self._header1title)
        self._header1_wrapper.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self._header1_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._header1_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._header1_wrapperscroll = self._create_uni_scroller(self._header1_wrapper)

        #   Header font styling for components
        self._headerfont = QFont()
        self._headerfont.setFamilies([u"Arial"])
        self._headerfont.setPointSize(24)
        self._header1title.setFont(self._headerfont)
        self._header2time.setFont(self._headerfont)

        self._header1title.adjustSize()
        self._header1_wrapper.setMaximumHeight(self._header1title.height()+2)
        self._header2time.adjustSize()
        self._header2time.setMaximumWidth(self._header2time.width())

        self._header.addWidget(self._header1_wrapper, 0)
        self._header.addWidget(self._header2time, 0)

        self._midsection = QVBoxLayout()
        self._midsection.setSpacing(4)
        
        if self._EJSON is not None:
            for key, value in self._EJSON.items():
                try:
                    objecttype, index_number = key.rsplit('_', 1) # Remove split & parse index number
                except:
                    print("Type index")
                if objecttype == 'EDescription':
                    self.object = self.EDescription(self, key, value*10)
                    self._midsection.addWidget(self.object)
                if objecttype == 'EToDo' :
                    self.object = self.EToDo(self, key, value['ETaskDescription'], value['EBool']) # Parse EToDo Date
                    self._midsection.addWidget(self.object)
                """if objecttype == 'object_index':
                    print(key,value)#"""

        """print('header size:',self._header2time.sizeHint())
        print('midsection size:',self._midsection.sizeHint())
        print('footer size:',self._footer.sizeHint())#"""

        # Add rows to layout
        self._layout.addLayout(self._header, 0)         # Add header row
        self._layout.addLayout(self._midsection, 1)     # Add midsection row
        self._layout.addWidget(self._footer, 0)         # Add footer row

class EBody(QWidget):
    """ Provides JSON Parsing of the Attributes column & constructs the internal body to be placed in Body & Dynamic 
        generation of internal body widgets
    """
    attributesChanged = Signal()

    def __init__(self, parent, Attributes: QByteArray = None):
        super().__init__(parent)
        self._Attributes = Attributes
        self._Json : Dict[str, QJsonValue] = None

    # Getters for _Json attributes
    def returnEventType(self): return self._Json['info']['event_type']
    def returnObjectIndex(self): return self._Json['info']['object_index']
    
    def _updateChecked(self, key: str, checked: bool):
        self._Json['objects'][key]['EBool'] = checked
        self._Attributes = QJsonDocument(self._Json).toJson(QJsonDocument.JsonFormat.Compact)
    
    def _updateJson(self):
        try: self.checkJDoc(QJsonDocument.fromJson(self._Attributes))
        except Exception as e: print(f"_updateJson()->{e}")

        new_Json = self.checkJsonStructure(
            QJsonDocument.fromJson(self._Attributes).object()
            )
        
        if (new_Json == self._Json): return
        elif self._Json is not None: self._reformatUi(n_Json=new_Json)
        else: self._generateUi(n_Json = new_Json)

    def _generateUi(self, n_Json: Dict[str, QJsonValue]):
        self.container = QVBoxLayout()
        self.container.setObjectName(u"body_container")
        self.container.setSpacing(4)
        self.layout = self.container

        self._Json = n_Json
        objects: Dict[str, QJsonValue] = self._Json.get('objects')
        for key, val in objects.items():

            component_type, index = str(key).rsplit('_', 1)

            if  (component_type == 'EDescription'):
                txt:  str                       = str(val)

                widget = EDescription(self, key)
                widget.setObjectName(key)
                widget.setText(txt)
                widget.adjustSize()
                
            elif(component_type == 'EToDo'):
                n_val:  Dict[str, QJsonValue]   = val
                val_bool, val_label             = bool(n_val.get('EBool')), str(n_val.get('EDescription'))
                checked, txt                    = bool(n_val.get('EBool')), str(n_val.get('EDescription'))

                widget = EToDo(self, key)
                widget.setObjectName(key)
                widget.setText(txt)
                widget.adjustSize()
                widget.setChecked(checked)

                widget._ui.checkbox.checkStateChanged.connect(lambda: self._updateChecked(key)) # Updating _Attributes will call a connection to the DB via the dataWidgetMapper
            
            self.container.addWidget(widget)

    def _reformatUi(self, n_Json: Dict[str, QJsonValue]):
        for key, val in n_Json.get('objects',{}).items():
            component_type, index = str(key).rsplit('_', 1)

            # If a key exists in self._Json
            if key in self._Json.get('objects',{}).keys():

                # Only run if the pre-existing ui object is mismatched w/ its value
                if (self._Json.get('objects',{}).get(key) != val):
                
                    if  (component_type == 'EDescription'): 
                        widget: EDescription            = self.container.findChild(EDescription, key)
                        n_val: str                      = val

                        if ((widget.text()) != n_val):          widget.setText(str(val))

                    elif(component_type == 'EToDo'):        
                        widget: EToDo                   = self.container.findChild(EToDo, key)
                        n_val:  Dict[str, QJsonValue]   = val
                        val_bool, val_label             = bool(n_val.get('EBool')), str(n_val.get('EDescription'))

                        if (widget.isChecked() != val_bool):    widget.setChecked(val_bool)
                        if (widget.text() != val_label):        widget.setText(val_label)
                
                # Otherwise, pass & don't update
                else: pass
            
            # If a key does not already exist in self._Json
            else:
                if  (component_type == 'EDescription'):
                    txt:  str                       = str(val)

                    widget = EDescription(self, key)
                    widget.setObjectName(key)
                    widget.setText(txt)
                    widget.adjustSize()

                elif(component_type == 'EToDo'):
                    n_val:  Dict[str, QJsonValue]   = val
                    val_bool, val_label             = bool(n_val.get('EBool')), str(n_val.get('EDescription'))
                    checked, txt                    = bool(n_val.get('EBool')), str(n_val.get('EDescription'))

                    widget = EToDo(self, key)
                    widget.setObjectName(key)
                    widget.setText(txt)
                    widget.adjustSize()
                    widget.setChecked(checked)

                    widget._ui.checkbox.checkStateChanged.connect(lambda: self._updateChecked(key)) # Updating _Attributes will call a connection to the DB via the dataWidgetMapper
                
                # Attempt to match index with another object, if it exists
                for o_key in self._Json.get('objects',{}).keys():
                    o_component_type, o_index = str(o_key).rsplit('_', 1)
                    if (index == o_index):  # Previous index holder for former; note it down
                        if (component_type == 'EDescription'): deleted_widget: EDescription    = self.container.findChild(EDescription, key)
                        if (component_type == 'EToDo'):        deleted_widget: EToDo           = self.container.findChild(EToDo, key)
                
                index = (int(index) - 1)
                other_widget = self.container.itemAt(index).widget()
                if  (deleted_widget is not None): 
                    self.container.replaceWidget(deleted_widget, widget)
                    deleted_widget.deleteLater()
                elif(other_widget is not None):
                    o_c, o_i = str(other_widget.objectName()).split('_',1)
                    o_i = (int(o_i) - 1)
                    if      (o_i > index): 
                        self.container.insertWidget(index, widget)
                    elif    (o_i < index):
                        self.container.insertWidget(index, widget)
                else:
                    self.container.addWidget(widget)
        
        self._Json['objects'] = n_Json['objects']
        self._Json['info'] = n_Json['info']

    def checkJDoc(self, t_Doc: QJsonDocument):
        if t_Doc.isNull(): raise Exception("validateJDoc error: QJsonDocument Null")
        t_Json = t_Doc.object()
        if not isinstance(t_Json, dict): raise Exception("validateJDoc error: Unpacked object not dict:",type(t_Json))
        return True  
    def checkJsonStructure(self, t_Json: Dict[str, QJsonValue]):
        """ Checks the Json Structure of a passed dict & checks its conformity against the expected structure; otherwise formats it """
        def formatTabInfo(info_Json: Dict[str, QJsonValue] = []):
            """ Formats an info tab"""
            object_index, event_type = info_Json.get('object_index'), info_Json.get('event_type')
            if (object_index is None): info_Json.update('object_index',0)
            if (event_type is None): info_Json.update('event_type',EventType.Complex.value)        
        def formatTabObject(objects_Json: Dict[str, QJsonValue] = []):
            """ Formats an objects tab """

            def formatEToDo(p_Json: Dict[str, QJsonValue]):
                """ Remove non whitelisted keys, and if values don't pre-exist generate them """
                EToDo: Dict[str, QJsonValue] = self.removeNonWhiteListedKeys(p_Json, ['EBool','ETaskDescription'])
                EBool, ETaskDescription = EToDo.get('EBool'), p_Json.get('ETaskDescription')
                if (EBool is None): EToDo.update({'EBool':False})
                if (ETaskDescription is None): EToDo.update({'ETaskDescription':'Task'})
                return EToDo
            def formatEDescription(p_Json: Dict[str, QJsonValue]):
                """ Search if any nested values/dictionary portions may have it stored, otherwise return default value """
                EDescription: str = self._jSearchKey(p_Json, 'EDescription')
                if (EDescription is None): EDescription = ''
                return EDescription

            # Convert Json Dict into a sorted list
            objects_ordered: List[Tuple[str, QJsonValue]] = sorted(
                objects_Json.items(), 
                key=lambda item: int(item[0].rsplit('_', 1)[1])
                )

            exp_index = 0 # Starting/expected index

            n_objects_Json = objects_Json.copy()
            n_objects_Json.clear()

            for key, value in objects_ordered:
                obj_type, index = key.rsplit('_', 1) # Remove split & parse index number

                exp_index += 1
                cur_index = int(index)
                
                if (cur_index != exp_index): key = f'{obj_type}_{exp_index}'

                if obj_type == 'EDescription':
                    if isinstance(value, str): pass
                    elif isinstance(value, dict): value = formatEDescription(value)
                    else: value = ''
                if obj_type == 'EToDo' :
                    value: Dict[str, QJsonValue] = formatEToDo(value)

                n_objects_Json.update({key:value})

            return n_objects_Json

        # Extract info & objects
        tab_Info: Dict[str, QJsonValue] = formatTabInfo(t_Json.get('info'))
        tab_Objects: Dict[str, QJsonValue] = t_Json.get('objects')

        # Should be fine, but adds a layer of precaution pre-reading it
        Index: int = tab_Info.get('object_index')
        if tab_Objects is not None:
            # First ensure the object branch is clear of any invalid keys
            tab_Objects = self.removeAllBlackListedKeys(tab_Objects,['object_index','event_type','info','objects'])

            # Set object_index to correct value
            if (len(tab_Objects)) == Index:         # if len(tab_Objects) == Index: 
                if Index == 0: tab_Objects = None                           # if (Index == 0) and (len(tab_Objects) == 0): Clear tab_Objects
                else: pass                                                  # if (Index == len(tab_Objects)) and (Index > 0): No action necessary          
            else:                                   # if len(tab_Objects) != Index:
                if bool(tab_Objects): Index, tab_Objects = 0, None          # if (tab_Objects.isEmpty()) and (Index != 0): Clear tab_Objects and set Index to 0
                else: Index = len(tab_Objects)                              # if (len(tab_Objects) > 0) and (len(tab_Objects) != Index): Set Index to length of tab_Objects

            if (Index != 0): tab_Objects = formatTabObject(tab_Objects)
            
            if (Index != tab_Info.get('object_index')): tab_Info.update({'object_index':Index})
        
        n_Json: Dict[str, QJsonValue] = []
        n_Json.update({'info':tab_Info})
        if (tab_Objects is not None): 
            tab_Objects = formatTabObject(tab_Objects)
            n_Json.update({'objects':tab_Objects})
        
        return n_Json

    def removeAllBlackListedKeys(self, p_Json: Dict[str, QJsonValue], 
                                 bl_Keys: List[str]):
        """ Recursively searches for a blacklisted key in a nested dictionary structure & removes it """
        n_Json = p_Json.copy()

        for key in bl_Keys:
            self._jDeleteKey(n_Json, key)
        
        return n_Json   
    def removeNonWhiteListedKeys(self, p_Json: Dict[str, QJsonValue],
                                 wl_Keys: List[str]):
        """ Looks for non-whitelisted keys in a regular/flat dictionary & removes them  """
        n_Json = p_Json.copy()

        invalid_keys: List[str] = []
        for key, value in n_Json.items():
            passed = False
            for wl_key in wl_Keys:
                if key == wl_key:
                    passed = True
            if not passed: invalid_keys.append(key)
        
        for inv_key in invalid_keys: n_Json.pop(inv_key)

        return n_Json
                
    def _jCheckKeysExist(self, root_dict: dict, fields: List[str]):
        for field in fields:
            found = self._jSearchKeyBool(root_dict, field)
            if not found: raise Exception(f'checkFields() error: jsonSearch() could not find "{field}"')
        return True
    def _jSearchKeyBool(self, s_dict: Dict[str, QJsonValue], field: str):
        """ Wrapper that converts into bool """
        value = self._jSearchKey(s_dict, field)
        if (value is not None): return True
        else: return False
    def _jSearchKey(self, s_dict: Dict[str, QJsonValue], field: str):
        """ Recursive json search function that searches for a field in a dictionary & if found the value associated """
        if field in s_dict: return s_dict[field]
        for key, val in s_dict.items():             
            if isinstance(val, dict):
                value = self._jSearchKey(val, field)
                if (value is not None): return value
    def _jDeleteKey(self, s_dict: Dict[str, QJsonValue], field: str):
        """ Recursive definitive json search which culminates in deleting a key (& any repeats) from a dictionary
            Be careful: Deleted keys have no way to be recovered.

            Use as following:
                'yourDict: Dict[str, QJsonValue] = self._jDeleteKey(yourDict, key)'
        """
        if field in s_dict: 
            s_dict.pop(field)
            return s_dict
        for key, val in s_dict.items():
            if isinstance(val, dict):
                value = self._jDeleteKey(val, field)
                if isinstance(value, dict): # If any dictionary was deleted, it'll return as type dictionary
                    if (len(value) == 0):   # If the key didn't contain any other information,
                        s_dict.pop(key)     # delete the key
                    else:
                        s_dict[key] = value # Otherwise, update the dictionary
        return s_dict
    def _jCountKeyRepeats(self, s_dict: Dict[str, QJsonValue], field: str):
        """ Recursive json search that checks for repeated keys """
        number: int = 0 
        if field in s_dict: number += 1
        for key, val in s_dict.items():
            if isinstance(val, dict):
                num = self._jCountKeyRepeats(val, field)
                if isinstance(num, int): number+=num
        return number

    @Property(QByteArray)
    def Attributes(self): return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes: QByteArray):
        if (self._Attributes != Attributes):
            self._Attributes = Attributes
            if (QJsonDocument.fromJson(self._Attributes).object() != self._Json): self._updateJson()
            self.attributesChanged.emit()

class ETime(QLabel):        # Time Label that provides multiple formatting/preset-styles & real-time time updating
    def __init__(self, parent):
        super().__init__(parent)
        pass

class ELocation(QLabel):    # Location Label that provides travel-time recommendations 
    def __init__(self, parent):
        super().__init__(parent)
        pass

class EDescription(QWidget):    # Description addition that provides a larger, scrollable box with horizontal word-wrapping
    def __init__(self, parent, key: str):
        super().__init__(parent)
        self.setObjectName(key)

        self._ui = Ui_event_description(self)
        self._ui.setupUi()

    def setText(self, new_txt: str):        self._ui.label.setText(new_txt)

    def text(self):                         return self._ui.label.text()

class EToDo(QWidget):           # ToDo Add-on that provides a checkable box & a specially formatted title
    def __init__(self, parent, key: str):
        super().__init__(parent)
        self.setObjectName(key)

        self._ui = Ui_event_todo(self)
        self._ui.setupUi()

    def setText(self, new_txt: str):        self._ui.label.setText(new_txt)
    def setChecked(self, new_bool: bool):   self._ui.checkbox.setChecked(new_bool)

    def text(self):                         return self._ui.label.text()
    def isChecked(self):                    return self._ui.checkbox.isChecked()


