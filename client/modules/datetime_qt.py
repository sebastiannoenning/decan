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
def dateTimeToFS(dateTime: QDateTime, 
                  cnvrt: EDateTime):     
    if (cnvrt == EDateTime.Date): return dateToFS(dateTime.date())
    if (cnvrt == EDateTime.Time): return timeToFS(dateTime.time())
    return dateTime.toString('d/MMM/yyyy HH:mm a')
def dateTimeToISO(dateTime: QDateTime, 
                   cnvrt: DateTime):
    if (cnvrt == EDateTime.Date): return dateToISO(dateTime.date())
    if (cnvrt == EDateTime.Time): return timeToISO(dateTime.time())
    return dateTime.toString(format=Qt.DateFormat.ISODate)
def QDateTimeToPy(dateTime: QDateTime,
                      cnvrt: DateTime):
    if (cnvrt == EDateTime.Date): return dateToPy(dateTime.date())
    if (cnvrt == EDateTime.Time): return timeToPy(dateTime.time())
    return dateTime.toPython()

# Turns QDate into a formatted string or datetime object
def dateToFS(date: QDate): return date.toString('d MMM yyyy')
def dateToISO(date: QDate): return date.toString(format=Qt.DateFormat.ISODate)
def dateToPy(date: QDate): return date.toPython()

# Turns QTime into a formatted string or datetime object
def timeToFS(time: QTime): return time.toString('HH:mm')
def timeToISO(time: QTime): return time.toString(format=Qt.DateFormat.ISODate)
def timeToPy(time: QTime): return time.toPython()
