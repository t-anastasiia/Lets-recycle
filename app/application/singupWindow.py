import re
import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QApplication

from UI.UiSingUpWindow import Ui_SingUpWindow
from models.userModel import UserModel  # Относительный импорт


class SingupWindow(QMainWindow, Ui_SingUpWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.move_center()

        self.user_model = UserModel('../dataBases/users_info.json')

        self.passwordIsValid = False
        self.repeatedPassword = False
        self.emailIsValid = False
        self.emailTextEdit.textChanged.connect(self.validate_email)
        self.passwordTextEdit1.textChanged.connect(self.validate_password)
        self.passwordTextEdit2.textChanged.connect(self.match_password)

        self.signupButton.clicked.connect(self.singup_button_clicked)
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

    def singup_button_clicked(self):
        if (self.passwordIsValid and self.repeatedPassword and
                self.emailIsValid and self.nameTextEdit.text()):
            print("Niceeee")
            if self.user_model.add_user(self.emailTextEdit.text(), self.passwordTextEdit1.text(), self.nameTextEdit.text()):
                print("Пользователь успешно зарегистрирован")
            else:
                print("У вас уже есть аккаунт с этим email")
        else:
            print("looser")

    def back_button_clicked(self):
        from application.loginWindow import LoginWindow  # Отложенный импорт
        self.main_window = LoginWindow()
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SingupWindow()
    ex.show()
    sys.exit(app.exec())
