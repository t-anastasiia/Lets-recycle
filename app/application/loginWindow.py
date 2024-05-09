import sys
import csv
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QApplication

from adminWindow import AdminWindow
from UI.UiLoginWindow import Ui_Login
from singupWindow import SingupWindow


def valid_user(login, password):
    with open('../dataBases/users_info.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        if reader is not None:
            for row in reader:
                if row[0] == login and row[1] == password and row[2] == '1':
                    return [True, True]
                elif row[0] == login and row[1] == password:
                    return [True, False]
            return [False, False]


class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)

        self.move_center()

        self.passwordIsValid = False
        self.loginIsValid = False

        self.loginButton.clicked.connect(self.login_button_clicked)
        self.signupButton.clicked.connect(self.singup_button_clicked)

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)


    def login_button_clicked(self):
        if self.loginIsValid and self.passwordIsValid:
            user_login = self.loginTextEdit.text()
            user_password = self.passwordTextEdit.text()
            is_validUser = valid_user(user_login, user_password)[0]
            is_admin = valid_user(user_login, user_password)[1]
            if is_validUser:
                if is_admin:
                    self.main_window = AdminWindow()
                    self.main_window.show()
                    self.close()
                else:
                    pass
            else:
                pass

    def singup_button_clicked(self):
        self.main_window = SingupWindow()
        self.main_window.show()
        self.close()


app = QApplication(sys.argv)
ex = LoginWindow()
ex.show()
sys.exit(app.exec())
