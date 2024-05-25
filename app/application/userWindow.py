import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI.UiUserWindow import Ui_UserWindow  # Импортируем внешний вид окна пользователя

class UserWindow(QMainWindow, Ui_UserWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move_center()

    def move_center(self):
        primary_screen = QGuiApplication.primaryScreen()
        screen_geometry = primary_screen.availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserWindow()
    window.show()
    sys.exit(app.exec())