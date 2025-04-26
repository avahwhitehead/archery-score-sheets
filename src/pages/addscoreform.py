import tkinter as tk

import darkdetect
import sv_ttk

from src.components.LabeledEntry import LabeledEntry
from src.components.LabeledNumericEntry import LabeledNumericEntry
from src.components.LabeledOptionMenu import LabeledOptionMenu
from src.data.archerydb import ArcheryDb


class AddScoreForm(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.database = ArcheryDb()

		genders = self.database.query_all('SELECT Name FROM Gender')
		genders = [g['Name'] for g in genders]

		# Root layout
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_rowconfigure(0, weight=0, minsize=40)

		# Input fields
		input_frame = tk.Frame(self)
		input_frame.grid(row=0, column=0, sticky="nsew")

		input_frame.grid_rowconfigure(0, weight=1)

		name_field = LabeledEntry(self, "Name")
		name_field.grid(row=0, column=0, sticky="nsew")

		gender_field = LabeledOptionMenu(self, "Gender", genders[0], genders)
		gender_field.grid(row=0, column=1, sticky="nsew")

		score_field = LabeledNumericEntry(self, "Score")
		score_field.grid(row=0, column=2, sticky="w")


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	AddScoreForm(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
