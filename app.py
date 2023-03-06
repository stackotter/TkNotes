from typing import Optional

import tkinter as tk

from db.file_db import FileDb

from session import Session

from model.base import Model
from view.base import View
from controller.base import Controller

from model.onboarding import OnboardingModel
from view.onboarding import OnboardingView
from controller.onboarding import OnboardingController

from model.sign_in import SignInModel
from view.sign_in import SignInView
from controller.sign_in import SignInController

from model.sign_up import SignUpModel
from view.sign_up import SignUpView
from controller.sign_up import SignUpController

from model.home import HomeModel
from view.home import HomeView
from controller.home import HomeController

from model.note_editor import NoteEditorModel
from view.note_editor import NoteEditorView
from controller.note_editor import NoteEditorController


class App(tk.Tk):
    frames: dict[str, tuple[Model, View, Controller]]
    current_page: Optional[tk.Frame]
    db: FileDb
    session: Session

    def __init__(self):
        super().__init__()

        self.title("Vector")
        self.geometry("500x500")

        self.pages = {
            "onboarding": (
                OnboardingModel,
                OnboardingView,
                OnboardingController
            ),
            "sign_in": (SignInModel, SignInView, SignInController),
            "sign_up": (SignUpModel, SignUpView, SignUpController),
            "home": (HomeModel, HomeView, HomeController),
            "note_editor": (
                NoteEditorModel,
                NoteEditorView,
                NoteEditorController
            ),
        }
        self.db = FileDb("./db.json")
        self.session = Session()

        self.current_page = None
        self.show("onboarding")

    def show(self, page: str):
        if self.current_page is not None:
            self.current_page.pack_forget()
            self.current_page.destroy()

        M, V, C = self.pages[page]
        model = M(self.db)
        view = V(self)
        controller = C(self, view, model)

        view.set_controller(controller)

        self.current_page = view


if __name__ == "__main__":
    app = App()
    app.mainloop()
