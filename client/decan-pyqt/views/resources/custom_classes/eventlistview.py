from typing import Union
import json

from PySide6.QtWidgets import QFrame, QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel
from PySide6.QtCore import Qt

from views.resources.custom_classes.eventitem import EventItem

class EventListView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        size_policy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        self.setSizePolicy(size_policy)
        self._list_container = QVBoxLayout()
        self._list_container.setSpacing(0)
        self._list_container.setContentsMargins(0,0,0,0)
        self.setLayout(self._list_container)
        print('complete')

    def add_item(self, item: EventItem):
        _list = self._list_container
        item.setMaximumWidth(self.width()-10)
        print('item size',self.sizeHint())
        #print(type(item))
        _list.addWidget(item)
        self.resize(self.width(), (self.height()+item.height()))
        print('widget size',self.sizeHint())

    def setModel(self, model: Union[QSqlRelationalTableModel, QSqlTableModel]):
        self._model = model
        model_elements = model.rowCount()
        print(model_elements)

        for i in range (0, 5):
            record = self._model.record(i)
            print(self._model.record(i).value("EAttributes"))
            _json = '{"object_index": 0, "EDescription_1": "Wow this is a description", "EDescription_2": "Wow this is a description"}'
            print(json.loads(_json))
            eventinfo = {
                'EventID'       : record.value("EventID"),
                'ETitle'        : record.value("ETitle"),
                'EAttributes'   : json.loads(_json),#record.value("EAttributes"),
                'ETime'         : record.value("EStart_Time")
            }
            event = EventItem(self, eventinfo['EventID'], eventinfo['ETitle'], eventinfo['ETime'], eventinfo['EAttributes'])
            self.add_item(event)

        """self._model.beforeInsert.connect()
        #self._model.beforeUpdate.connect()
        #self._model.beforeDelete.connect()
        #self._model.destroyed.connect()
        self._model.rowsInserted.connect()
        self._model.rowsRemoved.connect()
        self._model.dataChanged.connect()"""
