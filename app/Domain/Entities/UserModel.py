import sqlite3
import os
from Domain.Enums.User.UserStatus import UserStatus


class User:
    def __init__(self, user_id, email, password, status, name):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.status = UserStatus.ADMIN if status == 1 else UserStatus.USER
        self.name = name

    @staticmethod
    def get_user_by_email(email, password):
        db_path = get_db_path()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, email, password, status, name FROM users WHERE email=? AND password=?",
                       (email, password))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            return User(user_id=user_data[0], email=user_data[1], password=user_data[2], status=user_data[3],
                        name=user_data[4])
        return None

    def save_to_db(self, cursor):
        cursor.execute("INSERT INTO users (email, password, status, name) VALUES (?, ?, ?, ?)",
                       (self.email, self.password, 0, self.name))


def get_db_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data/User/Users.db'))
