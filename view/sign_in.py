import tkinter as tk

from view.base import View
from component.email_password_form import EmailPasswordForm

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.sign_in import SignInController

class SignInView(View):
    controller: 'SignInController'

    def __init__(self, parent):
        super().__init__(parent)

        self.form = EmailPasswordForm(
            self,
            submit_label="Sign in",
            cancel_handler=self.cancel,
            submit_handler=self.sign_in)
        self.form.pack()

        self.pack(anchor=tk.CENTER, expand=True, side=tk.BOTTOM)

    def cancel(self):
        self.controller.cancel()

    def sign_in(self, email, password):
        self.controller.sign_in(email, password)
