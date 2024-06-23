from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from Presentation.UI.User.UiUserLocationsWindow import Ui_UserLocationsWindow
import os

class UserLocationsWindow(QtWidgets.QMainWindow, Ui_UserLocationsWindow):
    def __init__(self, email):
        super().__init__()
        self.setupUi(self)
        self.add_map()
        self.backButton.clicked.connect(self.back_button_clicked)

        self.email = email

    def add_map(self):
        path_to_html = os.path.abspath('./Data/Location/Map.html')
        self.placeForMap.setUrl(QUrl.fromLocalFile(path_to_html))

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow(self.email)
        self.login_window.show()
        self.close()
