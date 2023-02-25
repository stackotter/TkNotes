from typing import Optional

import tkinter as tk

from model.onboarding import OnboardingModel
from view.onboarding import OnboardingView
from controller.onboarding import OnboardingController

from model.sign_in import SignInModel
from view.sign_in import SignInView
from controller.sign_in import SignInController

class App(tk.Tk):
    frames: dict[str, tuple]
    current_page: Optional[tk.Frame]

    def __init__(self):
        super().__init__()

        self.title("Vector")
        self.geometry("500x500")

        self.pages = {
            "onboarding": (OnboardingModel, OnboardingView, OnboardingController),
            "sign_in": (SignInModel, SignInView, SignInController),
        }

        self.current_page = None
        self.show("onboarding")

    def show(self, page: str):
        if self.current_page != None:
            self.current_page.pack_forget()
            self.current_page.destroy()

        M, V, C = self.pages[page]
        model = M()
        view = V(self)
        controller = C(self, view, model)

        view.set_controller(controller)

        self.current_page = view

if __name__ == '__main__':
    app = App()
    app.mainloop()
