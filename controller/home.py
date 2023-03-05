from model.home import HomeModel

from typing import TYPE_CHECKING

from model.note import Note
if TYPE_CHECKING:
    from view.home import HomeView
    from app import App


class HomeController:
    view: "HomeView"
    model: HomeModel

    def __init__(
            self,
            app: "App",
            view: "HomeView",
            model: HomeModel):
        self.app = app
        self.view = view
        self.model = model

    def sign_in(self):
        self.app.show("sign_in")

    def sign_up(self):
        self.app.show("sign_up")

    def get_notes(self) -> list[Note]:
        return self.model.get_notes(self.app.session.get_user_id())

    def new_note(self):
        self.app.session.set_current_note_id(None)
        self.app.show("note_editor")

    def edit_note(self, note_id: int):
        self.app.session.set_current_note_id(note_id)
        self.app.show("note_editor")

    def delete_note(self, note_id: int):
        self.model.delete_note(note_id)
        notes = self.model.get_notes(self.app.session.get_user_id())
        self.view.set_notes(notes)
