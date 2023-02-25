import tkinter as tk

class LabelledEntry(tk.Frame):
    def __init__(self, parent, label: str, **kwargs):
        super().__init__(parent)

        self.label = tk.Label(self, text=label)
        self.label.pack(anchor=tk.W)
        self.entry = tk.Entry(self, **kwargs)
        self.entry.pack(anchor=tk.W)

    def get(self) -> str:
        return self.entry.get()
