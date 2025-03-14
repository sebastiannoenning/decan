from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt, Slot


# Class for displaying all users in the system. Basic Read-Only functionality
class UserDisplay(QWidget):
    def __init__(self, parent):
        super.__init__(parent)

# Class for selecting a single user & returning the ID's of it
class UserSelect(QWidget):
    def __init__(self, parent):
        super.__init__(parent)

# Class for selecting multiple users & returning all their id's
class MultiUserSelect(UserSelect):
    def __init__(self, parent):
        super().__init__(parent)