import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QApplication

from adminWindow import AdminWindow
from UI.UiLoginWindow import Ui_Login
from models.userModel import UserModel  # Относительный импорт

def valid_user(user_model, login, password):
    for user in user_model.users:
        if user['email'] == login and user['password'] == password:
            return [True, user['isAdmin'] == '1']
    return [False, False]

class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)

        self.user_model = UserModel('../dataBases/users_info.json')

        self.move_center()

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
        user_login = self.loginTextEdit.text()
        user_password = self.passwordTextEdit.text()
        is_validUser, is_admin = valid_user(self.user_model, user_login, user_password)
        if is_validUser:
            if is_admin:
                self.main_window = AdminWindow()
                self.main_window.show()
                self.close()
            else:
                from userWindow import UserWindow  # Отложенный импорт для пользовательского окна
                self.main_window = UserWindow()
                self.main_window.show()
                self.close()
        else:
            print("Invalid login credentials")

    def singup_button_clicked(self):
        from singupWindow import SingupWindow  # Отложенный импорт для окна регистрации
        self.main_window = SingupWindow()
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec())