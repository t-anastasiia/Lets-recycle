import sqlite3
import os

class RequestModel:
    def __init__(self):
        self.db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data/Request/Requests.db'))

    def fetch_all_requests(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT email, city, phone, done FROM Contacts")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def update_request_status(self, email, status):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE Contacts SET done = ? WHERE email = ?", (status, email))
        conn.commit()
        conn.close()

    def insert_request(self, email, phone_number, city, street, house):
        if self.request_exists(email):
            return False
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Contacts (email, phone, city, street, house, done)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (email, phone_number, city, street, house, "-"))
        conn.commit()
        conn.close()
        return True

    def delete_request(self, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Contacts WHERE email = ?", (email,))
        conn.commit()
        conn.close()

    def request_exists(self, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Contacts WHERE email = ?", (email,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists
