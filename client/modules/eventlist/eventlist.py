from typing import Dict, Tuple, Optional, Callable, Any
from shiboken6 import Shiboken

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QLayoutItem
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt, Slot, Signal, QModelIndex, QSize

from models.event_model import EventModel
from modules.eventlist.event_list_ui import Ui_event_list
from modules.eventlist.eventitem import EventItem

class EventList(QWidget):
    """ Event List is a container widget for multiple EventItems 
        It is not concerned/aware about changes made to or within the EventItem attributes, & solely manages the removal & insertion of rows.
    """
    itemSelected = Signal(bool)

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

    def current(self) -> int:
        if self._current is None: return -1
        return self._current

    def resetList(self, 
                  test_en:Tuple[bool,str]=[False,'']):
        if self._model is None: return
        self._current = None
        self.clearList(test_en=[test_en[0],f'{test_en[1]}resetList()->'])
        self.populateList(test_en=[test_en[0],f'{test_en[1]}resetList()->'])

    def setModel(self, model: EventModel, 
                 test_en: bool = False):
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
        self._model.modelAboutToBeReset.connect(lambda: self.clearList(test_en=[test_en,'modelAboutToBeReset()->']))
        self._model.modelReset.connect(lambda: self.populateList(test_en=[test_en,'modelReset()->']))
        #self._model.layoutChanged.connect(lambda *a: self.resetList())
        #self._model.modelAboutToBeReset.connect()  Add caching here

    def deleteRow(self, index: QModelIndex):
        eventItem: EventItem = self._Items[index]
        if eventItem is None: return

    def moveRow(self, index: QModelIndex):
        eventItem: EventItem = self._Items[index]

    def realWidth(self): 
        width = max((self.minimumWidth()-20),(self._Ui.container.sizeHint().width() - (self._Ui.container.contentsMargins().left() + self._Ui.container.contentsMargins().right())))
        return width

    def addItem(self, item: EventItem, index: QModelIndex, 
                test_en:Tuple[bool,str]=[False,'']):
        item.setMinimumWidth(self.realWidth())
        item.setObjectName(f'EventItem_{index.row()}')
        if test_en[0]:
            print(f'{test_en[1]}addItem()->item.objectName(): {item.objectName()}')
        item.mousePressed.connect(lambda i_index: self.setSelected(i_index))
        self._Ui.container.addWidget(item)
        self._Items.update({index.row():item}) #Row in model used as index
        if test_en[0]:
            print(f'{test_en[1]}addItem() event added({item.objectName()}) added')

        self.setMinimumHeight(self._Ui.container.sizeHint().height())

    def takeItem(self, item: EventItem,
                   test_en:Tuple[bool,str]=[False,'']):
        item: EventItem = self.findChild(EventItem, item.objectName())
        key_of_item: Optional[int] = None
        for key, value in self._Items.items():
            if (value == item): key_of_item = key

        if key_of_item is not None:
            index = self._Ui.container.indexOf(item)
            taken_item: EventItem = self._Ui.container.takeAt(index).widget()
            self._Items.pop(key_of_item)
            return taken_item

        return None

    def removeItem(self, item: EventItem, 
                   test_en:Tuple[bool,str]=[False,'']):
        index = self._Ui.container.indexOf(item)
        layout_item : QLayoutItem  = self._Ui.container.takeAt(index)

        event_item  : EventItem    = layout_item.widget()
        event_item.mousePressed.disconnect(self.setSelected)
        if (test_en[0]): print(f'{test_en[1]}removeItem()->item.objectName(): {event_item.objectName()}')

        if event_item is not None: 
            event_item.deleteLater()

    def populateList(self, 
                     test_en:Tuple[bool,str]=[False,'']):
        for i in range(self._model.rowCount()):
            model_index : QModelIndex   = self._model.index(i, 0)
            new_item    : EventItem     = EventItem(self, self._model, model_index)
            self.addItem(new_item, model_index, test_en=[test_en[0],f'{test_en[1]}populateList()->'])

        if (test_en[0]): print(f'{test_en[1]}populateList() ui container length: {self._Ui.container.count()}')

    def clearList(self, 
                  test_en:Tuple[bool,str]=[False,'']):
        for event_item in self._Items.values():
            self.removeItem(event_item, test_en=[test_en[0],f'{test_en[1]}clearList()->'])
            if (test_en[0]): print(f'{test_en[1]}clearList() event({event_item.objectName()}) removed, shiboken check: {Shiboken.isValid(event_item)}')
        """
        for key in self._Items:
            if Shiboken.isValid(self._Items[key]): 
                self.removeItem(self._Items[key])"""
        if (test_en[0]): print(f'{test_en[1]}clearList() len(items)[{len(self._Items)}]:len(container)[{self._Ui.container.count()}]')

        if len(self._Items) != 0: self._Items.clear()

    @Slot(QModelIndex)
    def setSelected(self, calling_index: QModelIndex):
        calling_item: EventItem = self._Items[calling_index.row()]
        if calling_index.row() == self._current:
            calling_item.toggleSelected()
            self._current = None
            self.itemSelected.emit(False)
            return

        if isinstance(self._current, int):
            previous_item: EventItem = self._Items[self._current]
            previous_item.toggleSelected()

        self._current = calling_index.row()
        calling_item.toggleSelected()
        self.itemSelected.emit(True)

    def reject(self):
        if self._current is None: return
        reject_item: EventItem = self._Items[self._current]
        reject_item.toggleSelected()
        self._current = None

