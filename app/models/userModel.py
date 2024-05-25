import json

class UserModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8-sig') as jsonfile:
                return json.load(jsonfile)
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.file_path, 'w', encoding='utf-8-sig') as jsonfile:
            json.dump(self.users, jsonfile, ensure_ascii=False, indent=4)

    def user_exists(self, email):
        return any(user['email'] == email for user in self.users)

    def add_user(self, email, password, name):
        if not self.user_exists(email):
            new_user = {
                "email": email,
                "password": password,
                "isAdmin": "0",
                "place": "",
                "name": name
            }
            self.users.append(new_user)
            self.save_users()
            return True
        return False