from typing import Union
import json

from PySide6.QtWidgets import QFrame, QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt, QByteArray, Slot

from views.resources.custom_classes.eventitem import EventItem

class EventListView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.items = dict()
        self._model = None
        self.current = None
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
        self.items[eventinfo['EventID']].setObjectName(str(eventinfo['EventID']))

        self.items[eventinfo['EventID']].mousePressed.connect(self.setSelected)
        self.items[eventinfo['EventID']].itemChanged.connect(self.setData)
        self._list_container.addWidget(self.items[eventinfo['EventID']])
        self.resize(self.width(), (self.height()+self.items[eventinfo['EventID']].height()))
    
    def delete_item(self, EventID: int):
        try:
            self._list_container.removeWidget(self.items[EventID])
            self.items[EventID].deleteLater()
            del self.items[EventID]
        except Exception as e:
            print("No event passed:", Exception)

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

    def refresh_items(self, model: Union[QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel]):
        self._model = model
        model_elements = self._model.rowCount()
        for i in range (0, model_elements):
            record = self._model.record(i)
            self.add_item(record)

    def setModel(self, model: Union[QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel]):
        #print('Number of items currently in dict: ',len(self.items)) #Testing print // Schedule for removal at later date

        #Clear current list items under the condtion that the model has changed
        """     setModel should *not be used to update the widget model list conveniently; 
                that should be contingent w/ connections made via self._model.
                 ↪  events need to be cleared both via dictionary & removed from the widget;
                        failure to do both will either result in memory leaks or unlinked dict entries
                        'delete_item()' is a simple implementation intended to be used in conjunction
                        with model.onEvent.connect()ions & specifies an eventID to delete.
                ↪   that is why there is a seperate implementation for gradually removing events here:
                        dictionaries are inherently unordered & so this implementation rather uses popitem
                        to systematically remove & clear widgets in the order they were added in a LIFO fashion
                        from the stack. this ensures all widgets are removed & no dictionary events are left unlinked.
        """

        self.clear_items(lambda: model != self._model)

        """while ((len(self.items) > 0) & (model != self._model)):
            key, value = self.items.popitem()
            print(value)
            self._list_container.removeWidget(value)
            value.deleteLater()"""

        self.refresh_items(model)

        self._model.modelReset.connect(lambda: self.refreshModel())
        """self._model.beforeInsert.connect()
        #self._model.beforeUpdate.connect()
        #self._model.beforeDelete.connect()
        #self._model.destroyed.connect()
        self._model.rowsInserted.connect()
        self._model.rowsRemoved.connect()
        self._model.dataChanged.connect()""" #Implement later

    def refreshModel(self):
        self.clear_items(lambda: True)
        self.refresh_items(self._model)

    @Slot(EventItem)
    def setSelected(self, event: EventItem):
        try:
            if ((self.current is not None) & (self.current == event.EID)):
                temp_name = (self.items[self.current]).objectName()
                #print(temp_name)
                self.items[self.current].setStyleSheet(f'EventItem#{temp_name}{{ background-color: grey }}')
                self.current = None
            else:
                if self.current is not None:
                    prev_name = (self.items[self.current]).objectName()
                    self.items[self.current].setStyleSheet(f'EventItem#{prev_name}{{ background-color: grey }}')
                self.current = event.EID
                current_name = event.objectName()
                self.items[self.current].setStyleSheet(f'EventItem#{current_name}{{ background-color: lightblue }}')
        except Exception as e:
            print('Error:', e)

    @Slot(EventItem) 
    def setData(self, event: EventItem):
        id, new_attributes = event.EID, event.EAttributes
        for i in range(self._model.rowCount()):
            if self._model.record(i).value('EventID') == id:
                try:
                    index = self._model.index(i, 6)
                    self._model.setData(index, new_attributes, Qt.ItemDataRole.EditRole)
                    self._model.submitAll()
                except:
                    print('Unable to change data')

    def deleteSelected(self):
        if self.current is not None:
            print(self.current)
            self.delete_item(self.current)
            self.current = None
        else:
            print('No item selected!')

