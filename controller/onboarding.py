from model.onboarding import OnboardingModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from view.onboarding import OnboardingView
    from app import App

class OnboardingController:
    view: 'OnboardingView'
    model: OnboardingModel

    def __init__(self, app: 'App', view: 'OnboardingView', model: OnboardingModel):
        self.app = app
        self.view = view
        self.model = model

    def sign_in(self):
        self.app.show("sign_in")

    def sign_up(self):
        self.app.show("sign_up")
