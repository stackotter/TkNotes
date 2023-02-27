import tkinter as tk
from view.base import View

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.onboarding import OnboardingController


class OnboardingView(View):
    controller: "OnboardingController"

    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Welcome to Vector!")
        self.label.pack()

        self.sign_in_button = tk.Button(
            self,
            text="Sign in",
            command=self.sign_in_clicked)
        self.sign_in_button.pack()

        self.sign_up_button = tk.Button(
            self,
            text="Sign up",
            command=self.sign_up_clicked)
        self.sign_up_button.pack()

        self.pack(anchor=tk.CENTER, expand=True, side=tk.BOTTOM)

    def sign_in_clicked(self):
        self.controller.sign_in()

    def sign_up_clicked(self):
        self.controller.sign_up()
