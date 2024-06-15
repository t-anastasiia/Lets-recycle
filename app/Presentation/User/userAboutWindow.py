import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserAboutWindow import Ui_MainWindow
import os

class UserAboutWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BACK_BUTTON.clicked.connect(self.back_button_clicked)
        self.populate_combobox()

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow()
        self.login_window.show()
        self.close()

    def populate_combobox(self):
        # Определяем абсолютный путь к базе данных
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, '../../Data/Recycling/RecyclingInfo.db')

        # Подключаемся к базе данных SQLite
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Заполняем combobox категориями из базы данных
        self.comboBox.clear()
        self.cursor.execute('SELECT DISTINCT category FROM RecyclingInfo')
        categories = [row[0] for row in self.cursor.fetchall()]
        self.comboBox.addItems(categories)
        self.comboBox.currentIndexChanged.connect(self.display_info)

    def display_info(self, index):
        category = self.comboBox.itemText(index)
        self.cursor.execute('SELECT type, recyclable_locally, common_uses, description FROM RecyclingInfo WHERE category = ?', (category,))
        records = self.cursor.fetchall()

        info_text = ""
        for record in records:
            type_, recyclable_locally, common_uses, description = record
            info_text += f"Type: {type_}\nIs recycling in our point: {recyclable_locally}\nAreas of application: {common_uses}\nDescription: {description}\n\n"

        self.TEXT.setPlainText(info_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UserAboutWindow()
    mainWindow.show()
    sys.exit(app.exec())
