import os
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class MapView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        path_to_html = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Data/Location/Map.html'))
        self.load(QUrl.fromLocalFile(path_to_html))
