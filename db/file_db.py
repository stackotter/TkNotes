import json

from typing import Any
from db.file_db_table import FileDbTable


class FileDb:
    """
    A highly inefficient yet simple db that stores rows in a json
    file and has no form of indexing whatsoever. Most operations
    are O(n).
    """

    _file: str
    _tables: dict[str, list[dict[str, Any]]]
    _highest_id: int

    def __init__(self, file: str):
        self._file = file

        try:
            with open(self._file, "r") as f:
                self._tables = json.loads(f.read())
        except Exception:
            self._tables = {}
            self._save()

    def get_table(self, name: str) -> FileDbTable:
        """
        Returns the table with the given name, creating one if one doesn't
        already exist.
        """

        return FileDbTable(self, name)

    def _save(self):
        """
        Saves the in-memory db to its underlying file using json.
        """

        with open(self._file, "w") as f:
            f.write(json.dumps(self._tables))
