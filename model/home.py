from db.file_db import FileDb
from db.file_db_table import FileDbTable
from model.base import Model
from model.note import Note


class HomeModel(Model):
    _table: FileDbTable

    def __init__(self, db: FileDb):
        super().__init__(db)
        self._table = db.get_table("notes")

    def get_notes(self, user_id) -> list[Note]:
        rows = self._table.find_where(
            lambda row: row["author_id"] == user_id
        )

        print(self._table._rows)

        notes = []
        for row in rows:
            notes.append(Note(
                row["id"],
                row["author_id"],
                row["title"],
                row["content"]
            ))

        return notes

    def delete_note(self, note_id):
        self._table.remove(note_id)
