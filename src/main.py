import tkinter as tk

import darkdetect
import sv_ttk

from src.pages.scorespage import ScoresPage


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		text_var = tk.StringVar()
		text_var.set("here is my text on the mian page!")

		label = tk.Label(self, textvariable=text_var)
		label.pack()

		user_page = ScoresPage(self)
		user_page.pack()


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	MainApplication(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
