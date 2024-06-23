import sqlite3
import os

class Cities:
    def __init__(self):
        self.db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Data/Location/Cities.db'))

    def get_cities(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM cities")
        cities = cursor.fetchall()
        conn.close()
        return [city[0] for city in cities]
