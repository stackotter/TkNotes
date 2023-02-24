import tkinter as tk

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.root import RootController

class RootView(tk.Frame):
    controller: 'RootController'

    def __init__(self, parent):
        super().__init__(parent)

        self.increment_button = tk.Button(self, text="Inc", command=self.increment_clicked)
        self.increment_button.pack()

        self.decrement_button = tk.Button(self, text="Dec", command=self.decrement_clicked)
        self.decrement_button.pack()

        self.count_label = tk.Label(self, text="0")
        self.count_label.pack()

    def increment_clicked(self):
        self.controller.increment()

    def decrement_clicked(self):
        self.controller.decrement()

    def update_count(self, new_count: int):
        self.count_label["text"] = str(new_count)

    def set_controller(self, controller: 'RootController'):
        self.controller = controller
