from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserRequestWindow import Ui_UserRequestWindow
import sqlite3


def get_cities():
    conn = sqlite3.connect('./Data/Location/Cities.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM cities")
    cities = cursor.fetchall()
    conn.close()
    return [city[0] for city in cities]


def insert_request(email, phone_number, city, street, house):
    conn = sqlite3.connect('./Data/Request/Requests.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Contacts (email, phone, city, street, house, done)
        VALUES (?, ?, ?, ?, ?, 0)
    ''', (email, phone_number, city, street, house))
    conn.commit()
    conn.close()


class UserRequestWindow(QMainWindow, Ui_UserRequestWindow):
    def __init__(self, email):
        super().__init__()
        self.setupUi(self)

        self.email = email

        self.cities = get_cities()
        self.citiComboBox.addItems(self.cities)

        self.pushButton.clicked.connect(self.back_button_clicked)
        self.makeRequestButton.clicked.connect(self.make_request)

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow()
        self.login_window.show()
        self.close()

    def make_request(self):
        phone_number = self.phoneTextEdit.toPlainText().strip()
        street = self.streetTextEdit.toPlainText().strip()
        house = self.homeTextEdit.toPlainText().strip()

        default_phone = "Phone number"
        default_street = "Street"
        default_house = "House"

        if (not phone_number or phone_number == default_phone or
                not street or street == default_street or
                not house or house == default_house):
            QtWidgets.QMessageBox.warning(self, "Форма неполная", "Все поля должны быть заполнены для отправки заявки.")
            return

        city = self.citiComboBox.currentText().strip()
        insert_request(self.email, phone_number, city, street, house)
        QtWidgets.QMessageBox.information(self, "Заявка отправлена", "Ваша заявка была успешно отправлена.")
