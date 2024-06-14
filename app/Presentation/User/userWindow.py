import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Presentation.UI.User.UiUserMainWindow import Ui_MainWindow

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
        self.aboutText.setVisible(not self.aboutText.isVisible())

    def show_locations(self):
        # Логика для кнопки "Locations"
        self.locationsText.setVisible(not self.locationsText.isVisible())

    def show_requests(self):
        # Логика для кнопки "Requests"
        self.requestsText.setVisible(not self.requestsText.isVisible())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UserMainWindow()
    main_window.show()
    sys.exit(app.exec())
