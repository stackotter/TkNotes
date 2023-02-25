import tkinter as tk

from view.base import View
from component.email_password_form import EmailPasswordForm

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.sign_up import SignUpController

class SignUpView(View):
    controller: 'SignUpController'

    def __init__(self, parent):
        super().__init__(parent)

        self.form = EmailPasswordForm(
            self,
            submit_label="Sign up",
            cancel_handler=self.cancel,
            submit_handler=self.sign_up)
        self.form.pack()

        self.pack(anchor=tk.CENTER, expand=True, side=tk.BOTTOM)

    def cancel(self):
        self.controller.cancel()

    def sign_up(self, email, password):
        self.controller.sign_up(email, password)
