from PySide6.QtWidgets import QScrollArea, QWidget
from PySide6.QtCore import Qt

from eventlist.eventlist import EventList

# sets scrollable area for 
class EventListScrollArea(QScrollArea):
    def __init__(self, parent: QWidget, eventlist: EventList):
        super().__init__(parent)

        
