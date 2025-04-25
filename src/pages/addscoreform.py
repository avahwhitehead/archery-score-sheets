import tkinter as tk

import darkdetect
import sv_ttk

from src.components.NumericEntry import NumericEntry
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
		self.grid_rowconfigure(0, weight=0, minsize=40)

		# Input fields
		input_frame = tk.Frame(self)
		input_frame.grid_rowconfigure(0, weight=1)
		input_frame.grid_rowconfigure(1, weight=1)
		input_frame.grid(row=0, column=0, sticky="nsew")

		name_label_var = tk.StringVar()
		name_label_var.set("Name")

		name_label = tk.Label(input_frame, textvariable=name_label_var)
		name_label.grid(row=0, column=0, sticky="w")

		name_input = tk.Entry(input_frame)
		name_input.grid(row=1, column=0, sticky="nsew")

		gender_label_var = tk.StringVar()
		gender_label_var.set("Gender")

		gender_label = tk.Label(input_frame, textvariable=gender_label_var)
		gender_label.grid(row=0, column=1, sticky="w")

		gender_var = tk.StringVar()
		gender_var.set(genders[0])

		gender_input = tk.OptionMenu(input_frame, gender_var, *genders)
		gender_input.grid(row=1, column=1, sticky="nsew")

		score_label_var = tk.StringVar()
		score_label_var.set("Score")

		score_label = tk.Label(input_frame, textvariable=score_label_var)
		score_label.grid(row=0, column=2, sticky="w")

		score_input = NumericEntry(input_frame)
		score_input.grid(row=1, column=2, sticky="nsew")


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	AddScoreForm(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
