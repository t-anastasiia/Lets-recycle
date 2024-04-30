import re
import sys
import csv
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QApplication

from UI.UiLoginWindow import Ui_Login
from adminWindow import AdminWindow


class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.move_center()

        self.loginTextEdit.textChanged.connect(self.validate_login)
        self.passwordTextEdit.textChanged.connect(self.validate_password)

        self.passwordIsValid = False
        self.loginIsValid = False

        self.loginButton.clicked.connect(self.login_button_clicked)

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)


    def validate_login(self):
        login_text = self.loginTextEdit.text()
        if login_text:
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', login_text):
                self.loginTextEdit.setStyleSheet("")
                self.loginIsValid = True
            else:
                self.loginTextEdit.setStyleSheet("color: #FA8072;")
                self.loginIsValid = False
        else:
            self.loginTextEdit.setStyleSheet("")
            self.loginIsValid = False


    def validate_password(self):
        password_text = self.passwordTextEdit.text()
        if password_text:
            if re.match(r'^[a-zA-Z0-9_]+$', password_text):
                self.passwordTextEdit.setStyleSheet("")
                self.passwordIsValid = True
            else:
                self.passwordTextEdit.setStyleSheet("color: #FA8072;")
                self.passwordIsValid = False
        else:
            self.passwordTextEdit.setStyleSheet("")
            self.passwordIsValid = False

    def login_button_clicked(self):
        if self.loginIsValid and self.passwordIsValid:
            user_login = self.loginTextEdit.text()
            user_password = self.passwordTextEdit.text()
            is_validUser = self.valid_user(user_login, user_password)[0]
            is_admin = self.valid_user(user_login, user_password)[1]
            if is_validUser:
                if is_admin:
                    self.main_window = AdminWindow()
                    self.main_window.show()
                    self.close()
                else:
                    pass
            else:
                pass

    def valid_user(self, login, password):
        with open('../dataBases/users_info.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            if reader is not None:
                for row in reader:
                    if row[0] == login and row[1] == password and row[2] == '1':
                        return [True, True]
                    elif row[0] == login and row[1] == password:
                        return [True, False]
                return [False, False]


app = QApplication(sys.argv)
ex = LoginWindow()
ex.show()
sys.exit(app.exec())
