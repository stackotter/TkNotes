from model.base import Model
from view.base import View

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import App


class Controller:
    app: "App"
    view: View
    model: Model

    def __init__(self, app: "App", view: View, model: Model):
        self.app = app
        self.view = view
        self.model = model
