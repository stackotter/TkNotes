import tkinter as tk

from controllers.root import RootController
from model.base import Model
from views.root import RootView

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Vector")

        model = Model()
        view = RootView(self)
        controller = RootController(view, model)

        view.set_controller(controller)
        view.pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()
