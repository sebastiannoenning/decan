import sys, math, re
from enum import Enum
from datetime import datetime, date, time
from PySide6.QtCore import Qt, QDate, QDateTime, QTime

""" ### Custom DateTime Functions for QT Modules
    #   -   PyQt Custom Functions that are expected to be reused
"""

class DateTime(Enum):
    Date = 0
    Time = 1

# Turns QDateTime into a formatted string, or into QTime/QDate equivalents based on user input
def QDateTimeToFS(dateTime: QDateTime, 
                  cnvrt: DateTime):     
    if (cnvrt == DateTime.Date): return QDateToFS(dateTime.date())
    if (cnvrt == DateTime.Time): return QTimeToFS(dateTime.time())
    return dateTime.toString('d/MMM/yyyy HH:mm a')
def QDateTimeToISO(dateTime: QDateTime, 
                   cnvrt: DateTime):
    if (cnvrt == DateTime.Date): return QDateToISO(dateTime.date())
    if (cnvrt == DateTime.Time): return QTimeToISO(dateTime.time())
    return dateTime.toString(format=Qt.DateFormat.ISODate)
def QDateTimeToPy(dateTime: QDateTime,
                      cnvrt: DateTime):
    if (cnvrt == DateTime.Date): return QDateToPy(dateTime.date())
    if (cnvrt == DateTime.Time): return QTimeToPy(dateTime.time())
    return dateTime.toPython()

# Turns QDate into a formatted string or datetime object
def QDateToFS(date: QDate): return date.toString('d MMM yyyy')
def QDateToISO(date: QDate): return date.toString(format=Qt.DateFormat.ISODate)
def QDateToPy(date: QDate): return date.toPython()

# Turns QTime into a formatted string or datetime object
def QTimeToFS(time: QTime): return time.toString('HH:mm')
def QTimeToISO(time: QTime): return time.toString(format=Qt.DateFormat.ISODate)
def QTimeToPy(time: QTime): return time.toPython()
