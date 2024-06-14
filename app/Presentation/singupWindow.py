import re
import csv
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow

from Presentation.UI.UiSingUpWindow import Ui_SingUpWindow


class SingupWindow(QMainWindow, Ui_SingUpWindow):
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

        # self.backButton.clicked.connect(self.back_button_clicked)
        self.signupButton.clicked.connect(self.singup_button_clicked)

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

    # def back_button_clicked(self):
    #     self.signupButton

    def singup_button_clicked(self):
        if (self.passwordIsValid and self.repeatedPassword and
                self.emailIsValid and self.nameTextEdit.text()):
            print("Niceeee")
            self.add_user()
        else:
            print("looser")

    def add_user(self):
        with open('../Data/users_info.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            user_exist = False
            lastrow = 0
            if reader is not None:
                for row in reader:
                    if row[0] == self.emailTextEdit.text():
                        user_exist = True
                    lastrow = row.index()

            if user_exist:
                print("U have an account with that email")
            else:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(lastrow+1)