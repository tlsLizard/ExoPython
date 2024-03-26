from PyQt6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QListView, QPushButton, QLineEdit
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from ui_TodoUi import Ui_Dialog

class TodoListModel(QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []
        self.validation_flags = [False] * len(self._data)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def add_item(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(item)
        self.validation_flags.append(False)
        self.endInsertRows()

    def toggle_validation(self, index):
        row = index.row()
        self.validation_flags[row] = not self.validation_flags[row]
        self.dataChanged.emit(self.index(row, 0), self.index(row, 0), [Qt.DecorationRole])

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.todo_list_model = TodoListModel()
        self.ui.listView.setModel(self.todo_list_model)
        self.ui.listView.clicked.connect(self.list_item_clicked)

        self.ui.pushButton.clicked.connect(self.add_todo_item)
        self.ui.Suppression.clicked.connect(self.on_suppression_clicked)

    def add_todo_item(self):
        new_item = self.ui.lineEdit.text()
        if new_item:
            self.todo_list_model.add_item(new_item)
            self.ui.lineEdit.clear()

    def list_item_clicked(self, index):
        self.todo_list_model.toggle_validation(index)

    def on_suppression_clicked(self):
        selected_indexes = self.ui.listView.selectedIndexes()
        for index in sorted(selected_indexes, reverse=True):
            row = index.row()
            self.todo_list_model.beginRemoveRows(QModelIndex(), row, row)
            del self.todo_list_model._data[row]
            del self.todo_list_model.validation_flags[row]
            self.todo_list_model.endRemoveRows()

        self.todo_list_model.dataChanged.emit(self.todo_list_model.index(0),
                                              self.todo_list_model.index(self.todo_list_model.rowCount() - 1))



if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()

