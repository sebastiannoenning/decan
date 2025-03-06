import sys, math, re
from enum import Enum

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QEasingCurve, Slot, QPointF
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QDialogButtonBox, QCalendarWidget, QSpinBox
from PySide6.QtWidgets import QSizePolicy, QScroller, QScrollerProperties
from PySide6.QtGui import QFont

class customQSpinBox(QSpinBox):
    def __init__(self, parent):
        super().__init__(parent)



class DateSelect(QCalendarWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        

class TDateEditDialog(QDialog):
    def __init__(self, parent = ..., f = ...):
        super().__init__(parent, f)
        self._dateSelect = DateSelect

    def dateSelect(self): return self._dateSelect