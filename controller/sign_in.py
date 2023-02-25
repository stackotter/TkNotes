from model.sign_in import SignInModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from view.sign_in import SignInView
    from app import App

class SignInController:
    view: 'SignInView'
    model: SignInModel

    def __init__(self, app: 'App', view: 'SignInView', model: SignInModel):
        self.app = app
        self.view = view
        self.model = model

    def cancel(self):
        self.app.show("onboarding")

    def sign_in(self, email: str, password: str):
        print(email + ": " + password)
