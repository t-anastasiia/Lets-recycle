import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserLocationsWindow import Ui_UserLocationsWindow

class UserLocationsWindow(QMainWindow, Ui_UserLocationsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UserLocationsWindow()
    mainWindow.show()
    sys.exit(app.exec())
