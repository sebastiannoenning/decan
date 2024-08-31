from typing import Union
import json

from PySide6.QtWidgets import QFrame, QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlRecord
from PySide6.QtCore import Qt, QByteArray, Slot

from views.resources.custom_classes.eventitem import EventItem

class EventListView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.items = dict()
        self.current = int
        self.setup_ui()

    def setup_ui(self):
        size_policy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        self.setSizePolicy(size_policy)
        self._list_container = QVBoxLayout()
        self._list_container.setSpacing(0)
        self._list_container.setContentsMargins(0,0,0,0)
        self.setLayout(self._list_container)

    def add_item(self, record: QSqlRecord):
        eventinfo = {
            'EventID'       : record.value("EventID"),
            'ETitle'        : record.value("ETitle"),
            'EAttributes'   : record.value("EAttributes"),
            'ETime'         : record.value("EStart_Time")
        }
        self.items[eventinfo['EventID']] = EventItem(self, eventinfo['EventID'], eventinfo['ETitle'], eventinfo['ETime'], eventinfo['EAttributes'])
        self.items[eventinfo['EventID']].setMaximumWidth(self.width()-10)

        self.items[eventinfo['EventID']].mousePressed.connect(self.setSelected)
        self._list_container.addWidget(self.items[eventinfo['EventID']])
        self.resize(self.width(), (self.height()+self.items[eventinfo['EventID']].height()))
    
    def delete_item(self, EventID: int):
        key = str(EventID)
        print(type(key))
        try:
            self._list_container.removeWidget(self.items[key])
            self.items[EventID].deleteLater()
        except:
            print("No key")

    def setModel(self, model: Union[QSqlRelationalTableModel, QSqlTableModel]):
        self._model = model
        model_elements = model.rowCount()
        print(model_elements)
        for i in range (0, model_elements):
            record = self._model.record(i)
            self.add_item(record)

        """self._model.beforeInsert.connect()
        #self._model.beforeUpdate.connect()
        #self._model.beforeDelete.connect()
        #self._model.destroyed.connect()
        self._model.rowsInserted.connect()
        self._model.rowsRemoved.connect()
        self._model.dataChanged.connect()"""

    @Slot(EventItem)
    def setSelected(self, event: EventItem):
        self.current = event.EID
        print(self.current)

    def deleteSelected(self):
        if self.current is not None:
            self.delete_item(self.current)
        else:
            print('No item selected!')

