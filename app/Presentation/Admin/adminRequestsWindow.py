import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QStyledItemDelegate, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
import sqlite3
from Presentation.UI.Admin.UiAdminRequestsWindow import Ui_MainWindow  # Импортируйте сгенерированный файл


class PlusMinusDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setMaxLength(1)
        return editor

    def setEditorData(self, editor, index):
        text = index.model().data(index, Qt.ItemDataRole.EditRole)
        editor.setText(text)

    def setModelData(self, editor, model, index):
        text = editor.text()
        if text in ['+', '-']:
            model.setData(index, text, Qt.ItemDataRole.EditRole)
        else:
            QMessageBox.warning(editor, "Неверное значение", "Можно вводить только '+' или '-'.")
            model.setData(index, '',
                          Qt.ItemDataRole.EditRole)  # Очистить значение, если оно не соответствует требованиям


class AdminRequestsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_data()

        # Установка делегата для последнего столбца
        delegate = PlusMinusDelegate()
        self.tableWidget.setItemDelegateForColumn(3, delegate)

        # Подключение кнопки "Назад" к методу back_button_clicked
        self.backButton.clicked.connect(self.back_button_clicked)

    def load_data(self):
        # Подключение к базе данных
        conn = sqlite3.connect('./Data/Request/Requests.db')
        cursor = conn.cursor()

        # Извлечение данных из таблицы Contacts
        cursor.execute("SELECT email, city, phone, done FROM Contacts")
        rows = cursor.fetchall()

        # Закрытие соединения с базой данных
        conn.close()

        # Настройка таблицы
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Email', 'City', 'Phone', 'Done'])

        # Заполнение таблицы данными
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                if column_index == 3:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)  # Сделать последний столбец редактируемым
                else:
                    item.setFlags(
                        item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Сделать остальные столбцы нередактируемыми
                self.tableWidget.setItem(row_index, column_index, item)

    def back_button_clicked(self):
        # Вернуть на главное окно администратора
        from Presentation.Admin.adminWindow import AdminWindow
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = AdminRequestsWindow()
    mainWindow.show()
    sys.exit(app.exec())
