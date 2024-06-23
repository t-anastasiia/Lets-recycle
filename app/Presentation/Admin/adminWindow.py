from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication
from Presentation.UI.Admin.UiAdminMainWindow import Ui_AdminWindow
from Presentation.Admin.adminRequestsWindow import AdminRequestsWindow
from Presentation.Admin.adminRecycleInfoWindow import AdminRecycleInfoWindow

class AdminWindow(QMainWindow, Ui_AdminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.move_center()
        self.requestsButton.clicked.connect(self.open_requests_window)
        self.recyclingButton.clicked.connect(self.open_recycleInfo_window)

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def open_requests_window(self):
        self.requests_window = AdminRequestsWindow()
        self.requests_window.show()
        self.close()

    def open_recycleInfo_window(self):
        self.recycleInfo_window = AdminRecycleInfoWindow()
        self.recycleInfo_window.show()
        self.close()
