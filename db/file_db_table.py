from typing import TYPE_CHECKING, Any, Optional, Callable
if TYPE_CHECKING:
    from db.file_db import FileDb


class FileDbTable:
    _db: "FileDb"
    _name: str
    _rows: list[dict[str, Any]]
    _highest_id: int

    def __init__(self, db: "FileDb", name: str) -> None:
        self._db = db
        self._name = name

        if name in self._db._tables:
            self._rows = self._db._tables[name]
        else:
            self._rows = []
            self._save()

        self._update_highest_id()

    def get(self, row_id: int) -> Optional[dict[str, Any]]:
        """
        Gets the row with the given id. Returns `None` if no such row
        exists.
        """

        for row in self._rows:
            if row["id"] == row_id:
                return row
        return None

    def insert(self, row: dict[str, Any]) -> int:
        """
        Appends a new row to the end of the db. Overrides the `id`
        property of the row if it already has one. Returns the
        `id` that was assigned to the row.
        """

        self._refresh_rows()
        row["id"] = self._highest_id + 1
        self._highest_id += 1
        self._rows.append(row)
        self._save()
        return row["id"]

    def update(self, row: dict[str, Any]) -> bool:
        """
        Returns whether the row was updated. Only has an effect if a
        row exists with the same id already.
        """

        self._refresh_rows()
        for i, other in enumerate(self._rows):
            if other["id"] == row["id"]:
                self._rows[i] = row
                self._save()
                return True
        return False

    def remove(self, id_: int) -> Optional[dict[str, Any]]:
        """
        Removes the row with the given id from the db. Returns the
        removed row if any.
        """

        self._refresh_rows()
        for i, row in enumerate(self._rows):
            if row["id"] == id_:
                self._rows.pop(i)
                self._save()
                return row
        return None

    def find_where(
            self,
            condition: Callable[
                [dict[str, Any]], bool
            ]) -> list[dict[str, Any]]:
        """
        Returns any rows that meet the given condition.
        """

        self._refresh_rows()
        selected_rows = []
        for row in self._rows:
            if condition(row):
                selected_rows.append(row)
        return selected_rows

    def _refresh_rows(self):
        self._rows = self._db._tables[self._name]

    def _save(self):
        self._db._tables[self._name] = self._rows
        self._db._save()

    def _update_highest_id(self):
        """
        Updates the internal `_highest_id` property used to generate
        the ids of inserted rows.
        """

        self._highest_id = 0
        for row in self._rows:
            if row["id"] > self._highest_id:
                self._highest_id = row["id"]
