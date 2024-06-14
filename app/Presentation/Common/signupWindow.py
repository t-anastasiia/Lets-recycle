import re
import sqlite3
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Presentation.UI.Common.UiSingUpWindow import Ui_SingUpWindow
from Domain.Entities.User.UserInfo import User, get_db_path


class SignupWindow(QMainWindow, Ui_SingUpWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.move_center()

        self.passwordIsValid = False
        self.repeatedPassword = False
        self.emailIsValid = False
        self.emailTextEdit.textChanged.connect(self.validate_email)
        self.passwordTextEdit1.textChanged.connect(self.validate_password)
        self.passwordTextEdit2.textChanged.connect(self.match_password)

        self.signupButton.clicked.connect(self.signup_button_clicked)
        self.backButton.clicked.connect(self.back_button_clicked)

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def validate_email(self):
        login_text = self.emailTextEdit.text()
        if login_text:
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', login_text):
                self.emailTextEdit.setStyleSheet("")
                self.emailIsValid = True
            else:
                self.emailTextEdit.setStyleSheet("color: #FA8072;")
                self.emailIsValid = False
        else:
            self.emailTextEdit.setStyleSheet("")
            self.loginIsValid = False

    def validate_password(self):
        password_text = self.passwordTextEdit1.text()
        self.match_password()
        if password_text:
            if re.match(r'^[a-zA-Z0-9_]{6,}$', password_text):
                self.passwordTextEdit1.setStyleSheet("")
                self.passwordIsValid = True
            else:
                self.passwordTextEdit1.setStyleSheet("color: #FA8072;")
                self.passwordIsValid = False
        else:
            self.passwordTextEdit1.setStyleSheet("")
            self.passwordIsValid = False

    def match_password(self):
        if self.passwordTextEdit1.text() == self.passwordTextEdit2.text():
            self.repeatedPassword = True
            self.passwordTextEdit2.setStyleSheet("")
        else:
            self.passwordTextEdit2.setStyleSheet("color: #FA8072;")
            self.repeatedPassword = False

    def signup_button_clicked(self):
        if self.passwordIsValid and self.repeatedPassword and self.emailIsValid and self.nameTextEdit.text():
            self.add_user()
        else:
            QMessageBox.warning(self, "Signup Failed", "Please fill in all fields correctly.")

    def add_user(self):
        user_email = self.emailTextEdit.text()
        user_password = self.passwordTextEdit1.text()
        user_name = self.nameTextEdit.text()

        # Получаем путь к базе данных
        db_path = get_db_path()

        # Проверка наличия файла базы данных
        if not os.path.exists(db_path):
            QMessageBox.critical(self, "Database Error", "Database file not found.")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Проверка существования пользователя
        cursor.execute("SELECT * FROM users WHERE email=?", (user_email,))
        if cursor.fetchone():
            QMessageBox.warning(self, "Signup Failed", "User with this email already exists.")
            conn.close()
            return

        # Вставка нового пользователя с использованием класса User
        new_user = User(None, user_email, user_password, 0, user_name)
        new_user.save_to_db(cursor)
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Signup Successful", "You have successfully signed up!")
        self.show_login_window()

    def show_login_window(self):
        from Presentation.Common.loginWindow import LoginWindow
        self.main_window = LoginWindow()
        self.main_window.show()
        self.close()

    def back_button_clicked(self):
        self.show_login_window()
