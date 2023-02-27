import tkinter as tk

from typing import Callable, Optional
from component.labelled_entry import LabelledEntry


class EmailPasswordForm(tk.Frame):
    def __init__(
            self,
            parent,
            submit_label: str = "Submit",
            cancel_handler: Optional[Callable[[], None]] = None,
            submit_handler: Optional[Callable[[str, str], None]] = None):
        super().__init__(parent)

        self.cancel_handler = cancel_handler
        self.submit_handler = submit_handler

        self.error_label = tk.Label(self)
        self.error_label.pack(pady=4)

        self.email_entry = LabelledEntry(self, "Email")
        self.email_entry.pack(pady=4)

        self.password_entry = LabelledEntry(self, "Password", show="*")
        self.password_entry.pack(pady=4)

        self.button_frame = tk.Frame(self)
        self.cancel_button = tk.Button(
            self.button_frame,
            text="Cancel",
            command=self.cancel_clicked)
        self.cancel_button.pack(side=tk.LEFT)
        self.sign_in_button = tk.Button(
            self.button_frame,
            text=submit_label,
            command=self.submit_clicked)
        self.sign_in_button.pack(side=tk.LEFT)
        self.button_frame.pack()

    def get_email(self) -> str:
        return self.email_entry.get()

    def get_password(self) -> str:
        return self.password_entry.get()

    def cancel_clicked(self):
        if self.cancel_handler is not None:
            self.cancel_handler()

    def submit_clicked(self):
        if self.submit_handler is not None:
            self.submit_handler(self.get_email(), self.get_password())
