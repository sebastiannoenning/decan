import sys, math, re
from PySide6.QtCore import QObject
from PySide6.QtSql import QSqlQuery
""" ### Custom Object Manipulation for QT Module
    #   -   PyQt Custom Functions that are expected to be reused
"""

def execnext(query: QSqlQuery):
    query.exec()
    query.next()
    return query
    