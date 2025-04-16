import sys, math, re
from enum import Enum
from datetime import datetime, date, time
from PySide6.QtCore import Qt, QDate, QDateTime, QTime

""" ### Custom DateTime Functions for QT Modules
    #   -   PyQt Custom Functions that are expected to be reused
"""

# Enum for DateTime
class EDateTime(Enum):
    Date = 0
    Time = 1

# Turns QDateTime into a formatted string, or into QTime/QDate equivalents based on user input
def DateTimeToFS(dateTime: QDateTime, 
                  cnvrt: EDateTime):     
    if (cnvrt == EDateTime.Date): return DateToFS(dateTime.date())
    if (cnvrt == EDateTime.Time): return TimeToFS(dateTime.time())
    return dateTime.toString('d/MMM/yyyy HH:mm a')
def DateTimeToISO(dateTime: QDateTime, 
                   cnvrt: EDateTime):
    if (cnvrt == EDateTime.Date): return DateToISO(dateTime.date())
    if (cnvrt == EDateTime.Time): return TimeToISO(dateTime.time())
    return dateTime.toString(format=Qt.DateFormat.ISODate)
def DateTimeToPy(dateTime: QDateTime,
                      cnvrt: EDateTime):
    if (cnvrt == EDateTime.Date): return DateToPy(dateTime.date())
    if (cnvrt == EDateTime.Time): return TimeToPy(dateTime.time())
    return dateTime.toPython()

# Turns QDate into a formatted string or datetime object
def DateToFS(date: QDate): return date.toString('d MMM yyyy')
def DateToISO(date: QDate): return date.toString(format=Qt.DateFormat.ISODate)
def DateToPy(date: QDate): return date.toPython()

# Turns QTime into a formatted string or datetime object
def TimeToFS(time: QTime): return time.toString('HH:mm')
def TimeToISO(time: QTime): return time.toString(format=Qt.DateFormat.ISODate)
def TimeToPy(time: QTime): return time.toPython()
