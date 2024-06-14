from PyQt6.QtWidgets import QApplication
from Presentation.Common.loginWindow import LoginWindow

def main():
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec()

if __name__ == "__main__":
    main()
