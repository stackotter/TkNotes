import tkinter as tk

from model.base import Model
from view.root import RootView
from controller.root import RootController

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
