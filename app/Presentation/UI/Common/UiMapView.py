import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class MapView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        path_to_html = os.path.abspath('app/Data/Location/Map.html')
        self.load(QUrl.fromLocalFile(path_to_html))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.map_view = MapView(self)
        self.setCentralWidget(self.map_view)
