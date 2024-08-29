import datetime

# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties
from PySide6.QtGui import QFont

from views.resources.custom_classes.eventitem import EventItem

class Director():
    def __init__(self, builder):
        self.builder = builder

# Builder interface
class EventBuilder():
    def reset() -> EventItem():
        pass

    def 
