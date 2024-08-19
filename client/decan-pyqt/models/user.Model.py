from PySide6.QtCore import QObject, QAbstractItemModel

class UserModel(QAbstractItemModel):
    def __init__(self, parent: QObject | None = ...):
        super().__init__(parent)

class User(QObject):
    def __init__(self, parent: QObject | None = ...):
        super().__init__(parent)
        int self.userID = 0
         
