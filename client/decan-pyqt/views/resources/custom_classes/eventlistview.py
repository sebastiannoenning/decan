from typing import Union

from PySide6.QtWidgets import QFrame, QWidget, QVBoxLayout
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel
from PySide6.QtCore import Qt

from views.resources.custom_classes.eventitem import EventItem

class EventListView(QFrame):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self._list_container = QVBoxLayout()
        self._list_container.setSpacing(0)
        self._list_container.setContentsMargins(2,2,2,2)
        self.setLayout(self._list_container)
        print('complete')

    def add_item(self, item: EventItem):
        _list = self._list_container
        print(type(item))
        _list.addWidget(item, 0)

    def setModel(self, model: Union[QSqlRelationalTableModel, QSqlTableModel]):
        self._model = model
        model_elements = model.rowCount()
        print(model_elements)

        for i in range (0, 5):
            event = EventItem()
            self.add_item(event)

        #self._model.beforeInsert.connect()
        #self._model.beforeUpdate.connect()
        #self._model.beforeDelete.connect()
        #self._model.destroyed.connect()
