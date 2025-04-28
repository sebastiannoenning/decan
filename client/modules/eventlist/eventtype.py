from enum import Enum

class EventType(Enum):
    Simple      = 0, 'Simple'
    Complex     = 1, 'Complex'
    Note        = 2, 'Note'
    Task        = 3, 'Task'

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]