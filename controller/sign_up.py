from model.sign_up import SignUpModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from view.sign_up import SignUpView
    from app import App


class SignUpController:
    view: "SignUpView"
    model: SignUpModel

    def __init__(self, app: "App", view: "SignUpView", model: SignUpModel):
        self.app = app
        self.view = view
        self.model = model

    def cancel(self):
        self.app.show("onboarding")

    def sign_up(self, email: str, password: str):
        if self.model.user_exists(email):
            self.view.show_error("A user already exists with that email")
        else:
            user_id = self.model.insert_user(email, password)
            self.app.session.set_user_id(user_id)
            self.app.show("home")
