from typing import Any

import bcrypt

from model.base import Model

from db.file_db import FileDb
from db.file_db_table import FileDbTable


class SignInModel(Model):
    _table: FileDbTable

    def __init__(self, db: FileDb):
        super().__init__(db)
        self._table = db.get_table("users")

    def check_credentials(self, email: str, password: str) -> bool:
        rows = self._table.find_where(lambda row: row["email"] == email)
        if len(rows) == 0:
            return False

        return bcrypt.checkpw(
            password.encode("utf-8"),
            rows[0]["password_hash"].encode("utf-8")
        )

    def get_user(self, email: str) -> dict[str, Any]:
        return self._table.find_where(lambda row: row["email"] == email)[0]
