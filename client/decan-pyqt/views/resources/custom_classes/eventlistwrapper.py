from PySide6.QtWidgets import QScrollArea, QWidget
from PySide6.QtCore import Qt

# sets scrollable area for 
class EventListContainer(QScrollArea):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        
