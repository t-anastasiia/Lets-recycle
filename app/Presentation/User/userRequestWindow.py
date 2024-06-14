import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserRequestWindow import Ui_UserRequestWindow  # Импортируем сгенерированный файл

class UserRequestWindow(QMainWindow, Ui_UserRequestWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back_button_clicked)  # Подключаем кнопку к методу

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UserRequestWindow()
    mainWindow.show()
    sys.exit(app.exec())
