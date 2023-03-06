from model.note_editor import NoteEditorModel
from model.note import Note

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from view.note_editor import NoteEditorView
    from app import App


class NoteEditorController:
    view: "NoteEditorView"
    model: NoteEditorModel

    def __init__(
            self,
            app: "App",
            view: "NoteEditorView",
            model: NoteEditorModel):
        self.app = app
        self.view = view
        self.model = model

    def new_note(self, title: str, content: str) -> Note:
        user_id = self.app.session.get_user_id()
        if user_id is None:
            raise Exception("user_id unexpectedly None")
        return Note(None, user_id, title, content)

    def get_note(self):
        note_id = self.app.session.get_current_note_id()
        if note_id is None:
            return self.new_note("Untitled", "")
        else:
            note = self.model.get_note(note_id)
            if note is None:
                self.app.session.set_current_note_id(None)
                return self.new_note("Untitled", "")
            else:
                return note

    def cancel(self):
        self.app.show("home")

    def save(self, title: str, content: str):
        note_id = self.app.session.get_current_note_id()

        note = None
        if note_id is not None:
            note = self.model.get_note(note_id)
            if note is None:
                note = self.new_note(title, content)
            else:
                note.title = title
                note.content = content
        else:
            note = self.new_note(title, content)

        self.model.save_note(note)
        self.app.show("home")
