from model.base import Model

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from views.root import RootView

class RootController:
    view: 'RootView'
    model: Model

    def __init__(self, view: 'RootView', model: Model):
        self.view = view
        self.model = model

    def increment(self):
        self.model.count += 1
        self.view.update_count(self.model.count)

    def decrement(self):
        self.model.count -= 1
        self.view.update_count(self.model.count)
