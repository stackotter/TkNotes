import tkinter as tk

from view.base import View
from component.labelled_entry import LabelledEntry

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.sign_in import SignInController

class SignInView(View):
    controller: 'SignInController'

    def __init__(self, parent):
        super().__init__(parent)

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
            text="Sign in",
            command=self.sign_in_clicked)
        self.sign_in_button.pack(side=tk.LEFT)
        self.button_frame.pack()

        self.pack(anchor=tk.CENTER, expand=True, side=tk.BOTTOM)

    def cancel_clicked(self):
        self.controller.cancel()

    def sign_in_clicked(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.controller.sign_in(email, password)
