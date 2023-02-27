from model.sign_in import SignInModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from view.sign_in import SignInView
    from app import App


class SignInController:
    view: "SignInView"
    model: SignInModel

    def __init__(self, app: "App", view: "SignInView", model: SignInModel):
        self.app = app
        self.view = view
        self.model = model

    def cancel(self):
        self.app.show("onboarding")

    def sign_in(self, email: str, password: str):
        if self.model.check_credentials(email, password):
            user = self.model.get_user(email)
            self.app.session.set_user_id(user["id"])
            self.app.show("home")
        else:
            self.view.show_error("Invalid email or password")
