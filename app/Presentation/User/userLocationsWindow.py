from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserLocationsWindow import Ui_UserLocationsWindow
from Presentation.UI.Common.UiMapView import MapView

class UserLocationsWindow(QMainWindow, Ui_UserLocationsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_view = MapView(self)  # Создание виджета карты
        self.layout().addWidget(self.map_view)  # Добавление виджета карты в макет окна
        self.backButton.clicked.connect(self.back_button_clicked)  # Подключение кнопки назад

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow()
        self.login_window.show()
        self.close()
