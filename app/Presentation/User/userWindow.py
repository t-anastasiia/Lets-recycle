from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserMainWindow import Ui_MainWindow
from Presentation.User.userAboutWindow import UserAboutWindow
from Presentation.User.userLocationsWindow import UserLocationsWindow
from Presentation.User.userRequestWindow import UserRequestWindow

class UserMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, email):
        super().__init__()
        self.setupUi(self)
        self.initialize_ui()

        self.email = email

    def initialize_ui(self):
        self.aboutButton.clicked.connect(self.about_recycling)
        self.locationsButton.clicked.connect(self.show_locations)
        self.RequestsButton.clicked.connect(self.show_requests)

    def about_recycling(self):
        self.about_window = UserAboutWindow(self.email)
        self.about_window.show()
        self.close()

    def show_locations(self):
        self.locations_window = UserLocationsWindow(self.email)
        self.locations_window.show()
        self.close()

    def show_requests(self):
        self.request_window = UserRequestWindow(self.email)
        self.request_window.show()
        self.close()
