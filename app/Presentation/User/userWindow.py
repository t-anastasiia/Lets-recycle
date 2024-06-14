import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Presentation.UI.User.UiUserMainWindow import Ui_MainWindow
from Presentation.User.userAboutWindow import UserAboutWindow
from Presentation.User.userLocationsWindow import UserLocationsWindow
from Presentation.User.userRequestWindow import UserRequestWindow

class UserMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        # Подключение действий к кнопкам, если необходимо
        self.aboutButton.clicked.connect(self.about_recycling)
        self.locationsButton.clicked.connect(self.show_locations)
        self.RequestsButton.clicked.connect(self.show_requests)

    def about_recycling(self):
        # Логика для кнопки "About Recycling"
        self.about_window = UserAboutWindow()
        self.about_window.show()
        self.close()

    def show_locations(self):
        self.locations_window = UserLocationsWindow()
        self.locations_window.show()
        self.close()

    def show_requests(self):
        self.request_window = UserRequestWindow()
        self.request_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UserMainWindow()
    main_window.show()
    sys.exit(app.exec())
