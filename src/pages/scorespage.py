import tkinter as tk
from tkinter import ttk

import darkdetect
import sv_ttk


class ScoresPage(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		button = ttk.Button(parent, text="Click me on the user page!")
		button.pack()


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	ScoresPage(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
