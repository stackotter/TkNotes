from typing import Optional
from db.file_db import FileDb
from db.file_db_table import FileDbTable
from model.base import Model
from model.note import Note


class NoteEditorModel(Model):
    _table: FileDbTable

    def __init__(self, db: FileDb):
        super().__init__(db)
        self._table = db.get_table("notes")

    def get_note(self, note_id: int) -> Optional[Note]:
        row = self._table.get(note_id)
        if row is None:
            return None

        return Note.from_row(row)

    def save_note(self, note: Note):
        """
        Performs an upsert of the given note. If the note has an id, it is
        updated, otherwise it's inserted.
        """
        row = note.to_row()

        if note.id_ is not None:
            self._table.update(row)
        else:
            self._table.insert(row)
