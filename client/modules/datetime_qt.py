from enum import Enum
from PySide6.QtCore import Qt, QDate, QDateTime, QTime

""" ### Custom DateTime Functions for QT Modules
    #   -   PyQt Custom Functions that are expected to be reused
"""


# Enum for DateTime


class EDateTime(Enum):
    Date = 0
    Time = 1


#  Turns QDateTime into a formatted string, or into QTime/QDate equivalents based on user input
def date_time_to_fs(date_time: QDateTime,
                    cnvrt: EDateTime):
    if cnvrt == EDateTime.Date:
        return date_to_fs(date_time.date())
    if cnvrt == EDateTime.Time:
        return time_to_fs(date_time.time())
    return date_time.toString('d/MMM/yyyy HH:mm a')


def date_time_to_iso(date_time: QDateTime,
                     cnvrt: EDateTime):
    if cnvrt == EDateTime.Date:
        return date_to_iso(date_time.date())
    if cnvrt == EDateTime.Time:
        return time_to_iso(date_time.time())
    return date_time.toString(format=Qt.DateFormat.ISODate)


def date_time_to_py(date_time: QDateTime,
                    cnvrt: EDateTime):
    if cnvrt == EDateTime.Date:
        return date_to_py(date_time.date())
    if cnvrt == EDateTime.Time:
        return time_to_py(date_time.time())
    return date_time.toPython()


# Turns QDate into a formatted string or datetime object
def date_to_fs(date: QDate): return date.toString('d MMM yyyy')


def date_to_fs_long(date: QDate): return date.toString('ddd, d MMM yyyy')


def date_to_iso(date: QDate): return date.toString(format=Qt.DateFormat.ISODate)


def date_to_py(date: QDate): return date.toPython()


# Turns QTime into a formatted string or datetime object
def time_to_fs(time: QTime): return time.toString('HH:mm')


def time_to_iso(time: QTime): return time.toString(f=Qt.DateFormat.ISODate)


def time_to_py(time: QTime): return time.toPython()
