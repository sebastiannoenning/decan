from PySide6.QtSql import QSqlQueryModel, QSqlTableModel, QSqlDatabase, QSqlQuery 
from PySide6.QtCore import Qt

class  EditableSqlQueryModel (QSqlQueryModel) :
    def  __init__ (self, parent=None) :
        super(EditableSqlQueryModel, self).__init__(parent)
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)

    def  setData (self, index, value, role) :
        if index.isValid() and role == Qt.ItemDataRole.EditRole:
            record = self.record(index.row())
            field = self.record().field(index.column())
            if field.isAutoValue():
                return  False
            record.setValue(index.column(), value)
            self.setRecord(index.row(), record)
            self.dataChanged.emit(index, index)
            return  True
        return  False

    def  setEditStrategy (self, strategy) :
        if strategy == QSqlTableModel.EditStrategy.OnFieldChange:
            self.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        elif strategy == QSqlTableModel.EditStrategy.OnRowChange:
            self.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)
        elif strategy == QSqlTableModel.EditStrategy.OnManualSubmit:
            self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        else :
            super(EditableSqlQueryModel, self).setEditStrategy(strategy)