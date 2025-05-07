from typing import Optional, List, Dict, Callable, Any, Tuple
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt, Slot, QModelIndex, Signal

from client.models.user_model import UserModel
from modules.userlist.usertab import UserTab

# Class for displaying all users in the system. Basic Read-Only functionality
class UserList(QWidget):

    userChanged = Signal(QModelIndex)

    def __init__(self) -> None:
        super().__init__()

        self.container = QHBoxLayout()
        self.container.setContentsMargins(0,0,0,0)
        self.container.setSpacing(10)

        self.setObjectName("UserDisplay")
        self.setLayout(self.container)

        self._Tabs: Dict[int, List[Optional[UserTab],bool]] = {}

        self._model : UserModel = None
        self._current : Optional[int] = None

    def tryExcept(func: Callable[[], Any], message: str = 'Generic error message', test_en: bool = False):
        try: func()
        except Exception as e: print(message, e)

    def resetList(self,
                  test_en:Tuple[bool,str]=[False,'']):
        if self._model is None: return
        self.clearList(test_en=[test_en[0],f'{test_en[1]}resetList()->'])
        self.populateList(test_en=[test_en[0],f'{test_en[1]}resetList()->'])

    def setModel(self, model: UserModel,
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

    def addTab(self, tab: UserTab, index: QModelIndex,
                test_en:Tuple[bool,str]=[False,'']):
        tab.setObjectName(f'UserTab_{index.row()}')
        if test_en[0]:
            print(f'{test_en[1]}addTab()->tab.objectName(): {tab.objectName()}')

        self.container.addWidget(tab)
        tab.trySelected.connect(lambda i: self.trySelected(i))
        tab.signInRequested.connect(lambda i: self.trySignIn(i))
        self._Tabs.update({index.row():[tab, False]}) #Row in model used as index
        if test_en[0]:
            print(f'{test_en[1]}addTab() user added({tab.objectName()}) added')

    def takeTab(self, tab: UserTab,
                 test_en:Tuple[bool,str]=[False,'']):
        tab: UserTab = self.findChild(UserTab, tab.objectName())
        key_of_tab: Optional[int] = None
        for key, tab_pair in self._Tabs.items():
            if tab_pair[0] == tab: key_of_tab = key

        if key_of_tab is not None:
            index = self._Ui.container.indexOf(tab)
            taken_tab: UserTab = self._Ui.container.takeAt(index).widget()
            self._Tabs.pop(key_of_tab)
            return taken_tab

        return None

    def removeTab(self, tab: UserTab,
                   test_en:Tuple[bool,str]=[False,'']):
        index = self._Ui.container.indexOf(tab)
        layout_item : QLayoutItem  = self._Ui.container.takeAt(index)

        user_tab  : UserTab    = layout_item.widget()
        if (test_en[0]): print(f'{test_en[1]}removeTab()->tab.objectName(): {user_tab.objectName()}')

        if user_tab is not None:
            user_tab.deleteLater()

    def populateList(self,
                     test_en:Tuple[bool,str]=[False,'']):
        for i in range(self._model.rowCount()):
            model_index : QModelIndex   = self._model.index(i, 0)
            new_tab     : UserTab       = UserTab(self, self._model, model_index)
            self.addTab(new_tab, model_index, test_en=[test_en[0],f'{test_en[1]}populateList()->'])

        if (test_en[0]): print(f'{test_en[1]}populateList() ui container length: {self._Ui.container.count()}')

    def clearList(self,
                  test_en:Tuple[bool,str]=[False,'']):
        for tab_pair in self._Tabs.values():
            self.removeTab(tab_pair[0], test_en=[test_en[0],f'{test_en[1]}clearList()->'])
            if (test_en[0]): print(f'{test_en[1]}clearList() event({tab_pair[0].objectName()}) removed, shiboken check: {Shiboken.isValid(user_tab)}')

        if (test_en[0]): print(f'{test_en[1]}clearList() len(tabs)[{len(self._Tabs)}]:len(container)[{self._Ui.container.count()}]')

        if len(self._Tabs) != 0: self._Tabs.clear()

    def openPinEntry(self): pass

    def trySelected(self, i: int):
        index = self._model.index(i,0)
        for key, (tab, selected) in list(self._Tabs.items()):
            if selected:
                tab.toggleActive(False)
                self._Tabs[key][1] = False
        tab_pair = self._Tabs.get(i)
        user_tab : UserTab = tab_pair[0]
        user_tab.toggleActive(True)
        self._Tabs[i][1] = True
        self._current = index.row()

        self.userChanged.emit(index)
