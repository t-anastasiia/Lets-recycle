from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserRequestWindow import Ui_UserRequestWindow
from Domain.Entities.RequestModel import RequestModel
from Domain.Enums.Location.Cities import Cities


class UserRequestWindow(QMainWindow, Ui_UserRequestWindow):
    def __init__(self, email):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.email = email
        self.request_model = RequestModel()
        self.cities_model = Cities()

        self.cities = self.cities_model.get_cities()
        self.citiComboBox.addItems(self.cities)

        self.pushButton.clicked.connect(self.back_button_clicked)
        self.makeRequestButton.clicked.connect(self.make_request)

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow(self.email)
        self.login_window.show()
        self.close()

    def make_request(self):
        phone_number = self.phoneLineEdit.text().strip()
        street = self.streetLineEdit.text().strip()
        house = self.homeLineEdit.text().strip()

        if not phone_number or not street or not house:
            QtWidgets.QMessageBox.warning(self, "Форма неполная", "Все поля должны быть заполнены для отправки заявки.")
            return

        city = self.citiComboBox.currentText().strip()
        if not self.request_model.insert_request(self.email, phone_number, city, street, house):
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Вы уже оставили заявку. Нельзя оставлять более одной заявки.")
            return

        QtWidgets.QMessageBox.information(self, "Заявка отправлена", "Ваша заявка была успешно отправлена.")
