from typing import Dict, Tuple, Optional

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt, Slot, Signal, QModelIndex

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
        self._items     : Dict[QModelIndex, EventItem]                  = []
        # Internal Model, passed to all children
        self._model     : EventModel                                    = None
        self._current   : Optional[int]                                 = None

    
    def tryExcept(func: function, message: str = 'Generic error message', test_en: bool = False):
        try: func()
        except Exception as e: print(message, e)

    def reset(self):
        self.clearList(self)
        self.populateList(self)

    def setModel(self, model: EventModel, test_en: bool = True):
        if self._model is not None:
            msg = 'eventList->setModel()->eventModel->disconnect() error:'
            self.tryExcept(self._model.rowsMoved.disconnect(),                      f'{msg} Could not disconnect rowsMoved',            test_en)
            self.tryExcept(self._model.rowsInserted.disconnect(),                   f'{msg} Could not disconnect rowsInserted',         test_en)
            self.tryExcept(self._model.rowsRemoved.disconnect(),                    f'{msg} Could not disconnect rowsRemoved',          test_en)
            self.tryExcept(self._model.rowsAboutToBeMoved.disconnect(),             f'{msg} Could not disconnect rowsAboutToBeMoved',   test_en)
            self.tryExcept(self._model.rowsAboutToBeInserted.disconnect(),          f'{msg} Could not disconnect rowsAboutToBeInserted',test_en)
            self.tryExcept(self._model.rowsAboutToBeRemoved.disconnect(),           f'{msg} Could not disconnect rowsAboutToBeRemoved', test_en)

            self.tryExcept(self._model.modelReset.disconnect(),                     f'{msg} Could not disconnect rowsAboutToBeRemoved', test_en)
            self.tryExcept(self._model.modelAboutToBeReset.disconnect(),            f'{msg} Could not disconnect rowsAboutToBeRemoved', test_en)
        
        self._model = model
        if (self._Ui.container.count() > 0): self.clearList()

    def deleteRow(self, index: QModelIndex):
        eventItem: EventItem = self._items[index]

        if eventItem is None: return
        

    def moveRow(self, index: QModelIndex):
        eventItem: EventItem = self._items[index]

    def clearList(self): pass

    def populateList(self):
        # Only called when a models values have been completely changed. 
        pass

    def clear_items(self, condition):
        while ((len(self.items) > 0) & (condition())):
            key, value = self.items.popitem()
            #print(value)
            try:
                self.setMinimumWidth(self.width())
                self._list_container.removeWidget(value)
                value.deleteLater()
            except Exception as e:
                print("Error deleting widget", e)

        """self._model.beforeInsert.connect()
        #self._model.beforeUpdate.connect()
        #self._model.beforeDelete.connect()
        #self._model.destroyed.connect()
        self._model.rowsInserted.connect()
        self._model.rowsRemoved.connect()
        self._model.dataChanged.connect()"""

    def refreshModel(self):
        self.clear_items(lambda: True)

    def deleteSelected(self): pass

