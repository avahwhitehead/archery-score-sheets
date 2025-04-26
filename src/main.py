import tkinter as tk
import customtkinter as ctk

import darkdetect
import sv_ttk

from src.data.databaseinit import DatabaseInit
from src.pages.scorespage import ScoresPage


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		user_page = ScoresPage(self)
		user_page.pack(expand=True, fill="both")


if __name__ == "__main__":
	root = ctk.CTk()

	DatabaseInit().initialize()

	sv_ttk.set_theme(darkdetect.theme())

	MainApplication(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
