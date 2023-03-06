import tkinter as tk
from view.base import View

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.home import HomeController


class HomeView(View):
    controller: "HomeController"

    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="My notes", font=("Arial", 24))
        self.label.pack()

        self.notes_list_frame = tk.Frame(self)
        self.notes_list_frame.pack(pady=8)

        self.add_button = tk.Button(
            self,
            text="New note",
            command=self.new_note
        )
        self.add_button.pack()

        self.pack(side=tk.TOP)

    def set_controller(self, controller):
        super().set_controller(controller)
        self.set_notes(controller.get_notes())

    def set_notes(self, notes):
        for child in self.notes_list_frame.winfo_children():
            child.destroy()

        for note in notes:
            inner = tk.Frame(self.notes_list_frame)

            label = tk.Label(inner, text=note.title)
            label.pack(side=tk.LEFT)

            edit_button = tk.Button(
                inner,
                text="Edit",
                command=self.apply_action(self.edit_note, note.id_)
            )
            edit_button.pack(side=tk.LEFT)

            delete_button = tk.Button(
                inner,
                text="Delete",
                command=self.apply_action(self.delete_note, note.id_)
            )
            delete_button.pack(side=tk.LEFT)

            inner.pack(anchor=tk.W)

    def apply_action(self, action, note_id: int):
        def wrapped():
            return action(note_id)
        return wrapped

    def new_note(self):
        self.controller.new_note()

    def edit_note(self, note_id: int):
        self.controller.edit_note(note_id)

    def delete_note(self, note_id: int):
        self.controller.delete_note(note_id)
