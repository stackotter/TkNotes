import bcrypt

from model.base import Model

from db.file_db import FileDb
from db.file_db_table import FileDbTable


class SignUpModel(Model):
    _table: FileDbTable

    def __init__(self, db: FileDb):
        super().__init__(db)
        self._table = db.get_table("users")

    def user_exists(self, email: str) -> bool:
        result = self._table.find_where(lambda row: row["email"] == email)
        return len(result) != 0

    def insert_user(self, email: str, password: str):
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)

        user = {
            "email": email,
            "password_hash": password_hash.decode("utf-8")
        }

        return self._table.insert(user)
