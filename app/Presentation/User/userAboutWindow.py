from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from Presentation.UI.User.UiUserAboutWindow import Ui_MainWindow

class UserAboutWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BACK_BUTTON.clicked.connect(self.back_button_clicked)
        self.populate_combobox()

    def back_button_clicked(self):
        from Presentation.User.userWindow import UserMainWindow
        self.login_window = UserMainWindow()
        self.login_window.show()
        self.close()

    def populate_combobox(self):
        # Populate the combobox with actual data
        self.comboBox.clear()
        items = ["Recycling Plastic", "Recycling Paper", "Recycling Metal", "Recycling Glass", "Recycling Electronics"]
        self.comboBox.addItems(items)
        self.comboBox.currentIndexChanged.connect(self.display_info)

    def display_info(self, index):
        info = [
            "Recycling plastic involves collecting used plastic items and processing them into new products. This helps reduce the environmental impact and saves resources.",
            "Recycling paper is the process of converting waste paper into reusable paper products. This conserves trees and reduces landfill waste.",
            "Recycling metal involves collecting and processing used metal items to produce new metal products. This helps conserve natural resources and reduces pollution.",
            "Recycling glass involves collecting and melting down used glass items to create new glass products. This reduces the need for raw materials and decreases landfill waste.",
            "Recycling electronics involves dismantling old electronic devices and repurposing the components. This reduces electronic waste and recovers valuable materials."
        ]
        self.TEXT.setPlainText(info[index])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UserAboutWindow()
    mainWindow.show()
    sys.exit(app.exec())
