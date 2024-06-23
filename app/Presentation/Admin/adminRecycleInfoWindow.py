import os
from PyQt6 import QtWidgets
from Presentation.UI.Admin.UiAdminRecycleInfoWindow import Ui_MainWindow
import sqlite3


class AdminRecycleInfoWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.backButton.clicked.connect(self.on_back_button_clicked)

        self.load_data()

        self.marksTable.itemChanged.connect(self.on_item_changed)

        self.modified_data = {}

    def on_back_button_clicked(self):
        from Presentation.Admin.adminWindow import AdminWindow
        self.adminWindow = AdminWindow()
        self.adminWindow.show()
        self.close()

    def load_data(self):
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data/Recycling/RecyclingInfo.db'))
        connection = sqlite3.connect(db_path)
        query = "SELECT * FROM RecyclingInfo"
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        self.marksTable.setRowCount(len(data))
        self.marksTable.setColumnCount(len(column_names))
        self.marksTable.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.marksTable.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        connection.close()

    def on_item_changed(self, item):
        row = item.row()
        column = item.column()
        value = item.text()
        column_name = self.marksTable.horizontalHeaderItem(column).text()

        if row not in self.modified_data:
            self.modified_data[row] = {}
        self.modified_data[row][column_name] = value

        self.update_database(row, column_name, value)

    def update_database(self, row, column_name, value):
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data/Recycling/RecyclingInfo.db'))
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        record_id = self.marksTable.item(row, 0).text()

        query = f"UPDATE RecyclingInfo SET {column_name} = ? WHERE id = ?"
        cursor.execute(query, (value, record_id))
        connection.commit()
        connection.close()
