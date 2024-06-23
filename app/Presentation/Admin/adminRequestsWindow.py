from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from Presentation.UI.Admin.UiAdminRequestsWindow import Ui_MainWindow
from Domain.Entities.RequestModel import RequestModel

class AdminRequestsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.request_model = RequestModel()
        self.load_data()

        self.tableWidget.cellChanged.connect(self.handle_cell_changed)
        self.backButton.clicked.connect(self.back_button_clicked)

    def load_data(self):
        rows = self.request_model.fetch_all_requests()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Email', 'City', 'Phone', 'Done', 'Delete'])

        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                if column_index == 3:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidget.setItem(row_index, column_index, item)

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda ch, email=row_data[0]: self.delete_request(email))
            self.tableWidget.setCellWidget(row_index, 4, delete_button)

    def handle_cell_changed(self, row, column):
        if column == 3:
            email_item = self.tableWidget.item(row, 0)
            status_item = self.tableWidget.item(row, column)
            if email_item and status_item:
                email = email_item.text()
                status = status_item.text()
                if status in ['+', '-']:
                    self.request_model.update_request_status(email, status)
                else:
                    QMessageBox.warning(self, "Неверное значение", "Можно вводить только '+' или '-'.")
                    status_item.setText('')

    def delete_request(self, email):
        reply = QMessageBox.question(self, 'Удалить заявку', 'Вы уверены, что хотите удалить эту заявку?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.request_model.delete_request(email)
            self.load_data()

    def back_button_clicked(self):
        from Presentation.Admin.adminWindow import AdminWindow
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.close()
