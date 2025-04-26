import tkinter as tk

import customtkinter as ctk
import darkdetect
import sv_ttk

from src.components.LabeledButton import LabeledButton
from src.components.LabeledDateEntry import LabeledDateEntry
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

		age_categories = self.database.query_all('SELECT Name FROM main.AgeCategory')
		age_categories = [c['Name'] for c in age_categories]

		bow_types = self.database.query_all('SELECT Name FROM BowType')
		bow_types = [b['Name'] for b in bow_types]

		rounds = self.database.query_all('SELECT Name FROM Round')
		rounds = [r['Name'] for r in rounds]

		# Root layout
		self.grid_rowconfigure(0, weight=0, minsize=40)

		# Input fields
		input_frame = tk.Frame(self)
		input_frame.grid(row=0, column=0, sticky="nsew")


		# First row (shoot info)

		self.round_field = LabeledOptionMenu(input_frame, "Round", rounds[0], rounds)
		self.round_field.grid(row=0, column=0, sticky="nsew")

		self.date_field = LabeledDateEntry(input_frame, "Date")
		self.date_field.grid(row=0, column=1, sticky="nsew")

		# Second row (archer info)

		self.name_field = LabeledEntry(self, "Name")
		self.name_field.grid(row=1, column=0, sticky="nsew")

		self.gender_field = LabeledOptionMenu(self, "Gender", genders[0], genders)
		self.gender_field.grid(row=1, column=1, sticky="nsew")

		age_category_default = 'Senior' if 'Senior' in age_categories else age_categories[0]
		self.agecategory_field = LabeledOptionMenu(self, "Age Category", age_category_default, age_categories)
		self.agecategory_field.grid(row=1, column=2, sticky="nsew")

		self.bowtype_field = LabeledOptionMenu(self, "Bow Type", bow_types[0], bow_types)
		self.bowtype_field.grid(row=1, column=3, sticky="nsew")

		# Third row (score info)

		self.score_field = LabeledNumericEntry(self, "Score")
		self.score_field.grid(row=2, column=0, sticky="nsew")

		self.golds_field = LabeledNumericEntry(self, "Golds")
		self.golds_field.grid(row=2, column=1, sticky="nsew")

		save_button = LabeledButton(self, "Save", self.save_score)
		save_button.grid(row=2, column=3, sticky="nsew")

	def save_score(self):
		round_val = self.round_field.entry_var.get()
		date_val = self.date_field.combobox.get()

		name_val = self.name_field.entry_var.get()
		gender_val = self.gender_field.entry_var.get()
		agecategory_val = self.agecategory_field.entry_var.get()
		bowtype_val = self.bowtype_field.entry_var.get()

		score_val = int(self.score_field.entry_var.get())
		golds_val = int(self.golds_field.entry_var.get())

		print("Saving score: ", name_val, gender_val, agecategory_val, bowtype_val, score_val, golds_val, round_val, date_val, sep=" |")



if __name__ == "__main__":
	root = ctk.CTk()

	sv_ttk.set_theme(darkdetect.theme())

	AddScoreForm(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
