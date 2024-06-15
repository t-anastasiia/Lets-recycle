import sys
from PyQt6 import QtWidgets
from Presentation.User.userWindow import UserMainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UserMainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
