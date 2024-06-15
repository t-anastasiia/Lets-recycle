import sys
from PyQt6 import QtWidgets
from Presentation.Common.loginWindow import LoginWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = LoginWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
