import sys
import sqlite3
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QApplication

from Presentation.adminWindow import AdminWindow
from Presentation.UI.UiLoginWindow import Ui_Login
from Presentation.signupWindow import SignupWindow

def valid_user(login, password):
    conn = sqlite3.connect('app/Data/User/Users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, password, status FROM users WHERE email=? AND password=?", (login, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return [True, user[2] == 1]
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
        self.signupButton.clicked.connect(self.signup_button_clicked)

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def login_button_clicked(self):
        user_login = self.loginTextEdit.text()
        user_password = self.passwordTextEdit.text()
        is_validUser, is_admin = valid_user(user_login, user_password)
        if is_validUser:
            if is_admin:
                self.main_window = AdminWindow()
                self.main_window.show()
                self.close()
            else:
                # Добавьте логику для обычного пользователя, если требуется
                pass
        else:
            # Добавьте логику обработки неверного логина, если требуется
            pass

    def signup_button_clicked(self):
        self.main_window = SignupWindow()
        self.main_window.show()
        self.close()
