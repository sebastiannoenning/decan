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
        self._Ui = Ui_event_list(self)
        self._Ui.setupUi()

        # Internal Dictionary for quick lookup of EventItems via their QModelIndex
        self._items     : Dict[QModelIndex, EventItem]                  = []
        # Internal Model, passed to all children
        self._model     : EventModel                                    = None
        self._current   : Optional[int]                                 = None

    def setModel(self, model: EventModel):
        self._model = model
        if (self._Ui.container.count() > 0): self.clearList()

    def clearList(self): pass

    def populateList(self):
        # Only called when a models values have been completely changed. 
        pass

    def addItem(self, modelIndex: QModelIndex): pass
    
    def deleteItem(self, modelIndex: QModelIndex):
        try:
            self._items[modelIndex][0]
        except Exception as e: print(f"error msg: {e}")

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

    @Slot(EventItem)
    def setSelected(self, event: EventItem): pass

    @Slot(EventItem) 
    def setData(self, event: EventItem): pass

    def deleteSelected(self):
        if self.current is not None:
            print(self.current)
            self.delete_item(self.current)
            self.current = None
        else:
            print('No item selected!')

