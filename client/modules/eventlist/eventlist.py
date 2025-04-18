from typing import Dict, Tuple, Optional, Callable, Any
from shiboken6 import Shiboken

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt, Slot, Signal, QModelIndex, QSize

from models.event_model import EventModel
from modules.eventlist.event_list_ui import Ui_event_list
from modules.eventlist.eventitem import EventItem

class EventList(QWidget):
    """ Event List is a container widget for multiple EventItems 
        It is not concerned/aware about changes made to or within the EventItem attributes, & solely manages the removal & insertion of rows.
    """
    def __init__(self) -> None:
        super().__init__()
        self._Ui = Ui_event_list()
        self._Ui.setupUi(self)

        # Internal Dictionary for quick lookup of EventItems via their QModelIndex
        self._Items     : Dict[int, EventItem]                          = {}
        # Internal Model, passed to all children
        self._model     : EventModel                                    = None
        self._current   : Optional[int]                                 = None
    
    def tryExcept(func: Callable[[], Any], message: str = 'Generic error message', test_en: bool = False):
        try: func()
        except Exception as e: print(message, e)

    def resetList(self):
        self.clearList(self)
        self.populateList(self)

    def setModel(self, model: EventModel, test_en: bool = True):
        if self._model is not None:
            msg = 'eventList->setModel()->eventModel->disconnect() error:'
            self.tryExcept(self._model.rowsMoved.disconnect,                      f'{msg} Could not disconnect rowsMoved',            test_en)
            self.tryExcept(self._model.rowsInserted.disconnect,                   f'{msg} Could not disconnect rowsInserted',         test_en)
            self.tryExcept(self._model.rowsRemoved.disconnect,                    f'{msg} Could not disconnect rowsRemoved',          test_en)
            self.tryExcept(self._model.rowsAboutToBeMoved.disconnect,             f'{msg} Could not disconnect rowsAboutToBeMoved',   test_en)
            self.tryExcept(self._model.rowsAboutToBeInserted.disconnect,          f'{msg} Could not disconnect rowsAboutToBeInserted',test_en)
            self.tryExcept(self._model.rowsAboutToBeRemoved.disconnect,           f'{msg} Could not disconnect rowsAboutToBeRemoved', test_en)

            self.tryExcept(self._model.modelReset.disconnect,                     f'{msg} Could not disconnect rowsAboutToBeRemoved', test_en)
            self.tryExcept(self._model.modelAboutToBeReset.disconnect,            f'{msg} Could not disconnect rowsAboutToBeRemoved', test_en)
        
        self._model = model
        self._model.modelReset.connect(self.resetList())
        self._model.modelAboutToBeReset.connect()

        self.resetList()

    def deleteRow(self, index: QModelIndex):
        eventItem: EventItem = self._Items[index]
        if eventItem is None: return

    def moveRow(self, index: QModelIndex):
        eventItem: EventItem = self._Items[index]

    def minimumHeight(self):
        """ Absolute minimum height for the QScrollArea wrapper holding this """
        spacing = (self._Ui.container.spacing() * len(self._Items))

        item_dimensions: Tuple[int] = tuple(event_item.sizeHint().height() for event_item in self._Items.values())
        max_dimension = max(item_dimensions)
        return max_dimension
    
    def layoutWidth(self): 
        return (self._Ui.container.sizeHint().width() - (self._Ui.container.contentsMargins().left() + self._Ui.container.contentsMargins().right()))

    def addItem(self, item: EventItem, index: QModelIndex, 
                test_en:bool=False):
        item.setMaximumWidth(self.layoutWidth())

        self._Ui.container.addWidget(item)
        self._Items.update({index.row():item}) #Row in model used as index 

        self.setMinimumHeight(self._Ui.container.sizeHint().height())

    def takeItem(self, item: EventItem,
                   test_en:bool=False):
        item: EventItem = self.findChild(EventItem, item.objectName())
        key_of_item: Optional[int] = None
        for key, value in self._Items.items():
            if (value == item): key_of_item = key
        
        if key_of_item is not None:
            index = self._Ui.container.indexOf(item)
            taken_item: EventItem = self._Ui.container.takeAt(index).widget()
            self._Items.pop[key_of_item]
            return taken_item
         
        return None

    def removeItem(self, item: EventItem, 
                   test_en:bool=False):
        item: EventItem = self.findChild(EventItem, item.objectName())
        try: self._Ui.container.removeWidget(item)
        except Exception as e: 
            if (test_en): print(f"removeItem() error: {e}")
        item.deleteLater()

    def populateList(self, test_en):
        if len(self._Items) > 0: self.clearList(test_en=test_en)
        if self._model is None: return

        for i in (self._model.rowCount()):
            model_index : QModelIndex   = self._model.index(i, 0, QModelIndex)
            new_item    : EventItem     = EventItem(self, self._model, model_index)
            self.addItem(new_item, i)

    def clearList(self, test_en=False):
        for key, value in self._Items.items():
            self.removeItem(value, test_en=test_en)
            if (test_en): print(Shiboken.isValid(self._Items[key]))
        
        for key in self._Items:
            if Shiboken.isValid(self._Items[key]): 
                self.removeItem(self._Items[key])
            self._Items.pop[key]
        
        if len(self._Items) != 0: self._Items.clear()

