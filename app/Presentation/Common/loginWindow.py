import re
from PyQt6.QtGui import QGuiApplication, QRegularExpressionValidator
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import QRegularExpression

from Presentation.Admin.adminWindow import AdminWindow
from Presentation.UI.Common.UiLoginWindow import Ui_Login
from Presentation.Common.signupWindow import SignupWindow
from Domain.Enums.User.UserStatus import UserStatus
from Domain.Entities.User.UserInfo import User
from Presentation.User.userWindow import UserMainWindow


class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)
        self.move_center()

        self.passwordIsValid = False
        self.loginIsValid = False

        self.loginButton.setEnabled(False)

        self.loginTextEdit.textChanged.connect(self.validate_input)
        self.passwordTextEdit.textChanged.connect(self.validate_input)
        self.loginButton.clicked.connect(self.login_button_clicked)
        self.signupButton.clicked.connect(self.signup_button_clicked)

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def validate_input(self):
        email_regex = QRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]{2,}\.[a-zA-Z]{2,}$")
        email_validator = QRegularExpressionValidator(email_regex)
        email = self.loginTextEdit.text()
        password = self.passwordTextEdit.text()

        email_valid = email_validator.validate(email, 0)[0] == QRegularExpressionValidator.State.Acceptable
        password_valid = len(password) > 0

        self.loginIsValid = email_valid
        self.passwordIsValid = password_valid

        self.loginButton.setEnabled(email_valid and password_valid)

    def login_button_clicked(self):
        user_login = self.loginTextEdit.text()
        user_password = self.passwordTextEdit.text()

        email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]{2,}\.[a-zA-Z]{2,}$")
        if not email_regex.match(user_login):
            self.loginTextEdit.setStyleSheet("border: 1px solid red;")
            self.passwordTextEdit.setStyleSheet("")
            QMessageBox.warning(self, "Invalid Email", "Invalid email format.")
            return

        user = User.get_user_by_email(user_login, user_password)
        if not user:
            self.loginTextEdit.setStyleSheet("border: 1px solid red;")
            self.passwordTextEdit.setStyleSheet("border: 1px solid red;")
            QMessageBox.warning(self, "Login Failed", "Invalid email or password")
            return

        self.loginTextEdit.setStyleSheet("")
        self.passwordTextEdit.setStyleSheet("")
        if user.status == UserStatus.ADMIN:
            self.main_window = AdminWindow()
        else:
            self.main_window = UserMainWindow(self.loginTextEdit.text())
        self.main_window.show()
        self.close()

    def signup_button_clicked(self):
        self.main_window = SignupWindow()
        self.main_window.show()
        self.close()
