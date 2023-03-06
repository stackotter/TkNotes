import tkinter as tk
from view.base import View

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.note_editor import NoteEditorController


class NoteEditorView(View):
    controller: "NoteEditorController"

    def __init__(self, parent):
        super().__init__(parent)

        self.title_field = tk.Entry(self, font=("Arial", 24))
        self.title_field.pack()

        self.content_field = tk.Text(self)
        self.content_field.pack()

        self.save_button = tk.Button(
            self,
            text="Save",
            command=self.save_button_pressed
        )
        self.save_button.pack()

        self.pack(side=tk.TOP)

    def set_controller(self, controller):
        super().set_controller(controller)

        note = self.controller.get_note()

        self.title_field.insert(tk.END, note.title)
        self.content_field.insert(tk.END, note.content)

    def save_button_pressed(self):
        self.controller.save(
            self.title_field.get(),
            self.content_field.get("1.0", tk.END)
        )
