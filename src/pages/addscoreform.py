import tkinter as tk
import datetime

import customtkinter as ctk
import darkdetect
import sv_ttk

from src.components.LabeledButton import LabeledButton
from src.components.LabeledCheckbox import LabeledCheckbox
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

		self.genders = self.database.query_all('SELECT Id, Name FROM Gender')
		gender_values = [g['Name'] for g in self.genders]

		self.age_categories = self.database.query_all('SELECT Id, Name FROM main.AgeCategory')
		age_category_values = [c['Name'] for c in self.age_categories]

		self.bow_types = self.database.query_all('SELECT Id, Name FROM BowType')
		bow_type_values = [b['Name'] for b in self.bow_types]

		self.rounds = self.database.query_all('SELECT Id, Name FROM Round')
		round_values = [r['Name'] for r in self.rounds]

		# Root layout
		self.grid_rowconfigure(0, weight=0, minsize=40)

		# Input fields
		input_frame = tk.Frame(self)
		input_frame.grid(row=0, column=0, sticky="nsew")


		# First row (shoot info)

		self.round_field = LabeledOptionMenu(input_frame, "Round", round_values[0], round_values)
		self.round_field.grid(row=0, column=0, sticky="nsew")

		self.date_field = LabeledDateEntry(input_frame, "Date")
		self.date_field.grid(row=0, column=1, sticky="nsew")
		self.date_field.combobox.set(datetime.date.today().strftime("%Y-%m-%d"))

		# Second row (archer info)

		self.name_field = LabeledEntry(self, "Name")
		self.name_field.grid(row=1, column=0, sticky="nsew")

		self.gender_field = LabeledOptionMenu(self, "Gender", gender_values[0], gender_values)
		self.gender_field.grid(row=1, column=1, sticky="nsew")

		age_category_default = 'Senior' if 'Senior' in age_category_values else age_category_values[0]
		self.agecategory_field = LabeledOptionMenu(self, "Age Category", age_category_default, age_category_values)
		self.agecategory_field.grid(row=1, column=2, sticky="nsew")

		self.bowtype_field = LabeledOptionMenu(self, "Bow Type", bow_type_values[0], bow_type_values)
		self.bowtype_field.grid(row=1, column=3, sticky="nsew")

		self.club_member_field = LabeledCheckbox(self, "Club Member")
		self.club_member_field.grid(row=1, column=4, sticky="nsew")

		# Third row (score info)

		self.score_field = LabeledNumericEntry(self, "Score")
		self.score_field.grid(row=2, column=0, sticky="nsew")
		self.score_field.entry_var.set(0)

		self.golds_field = LabeledNumericEntry(self, "Golds")
		self.golds_field.grid(row=2, column=1, sticky="nsew")
		self.golds_field.entry_var.set(0)

		save_button = LabeledButton(self, "Save", self.save_score)
		save_button.grid(row=2, column=3, sticky="nsew")

	def save_score(self):
		round_val = self.round_field.entry_var.get()
		date_val = self.date_field.combobox.get()

		name_val = self.name_field.entry_var.get()
		gender_val = self.gender_field.entry_var.get()
		agecategory_val = self.agecategory_field.entry_var.get()
		bowtype_val = self.bowtype_field.entry_var.get()
		club_member_val = self.club_member_field.entry_var.get()

		score_val = int(self.score_field.entry_var.get())
		golds_val = int(self.golds_field.entry_var.get())

		round_id = next(r['Id'] for r in self.rounds if r['Name'] == round_val)
		gender_id = next(g['Id'] for g in self.genders if g['Name'] == gender_val)
		agecategory_id = next(c['Id'] for c in self.age_categories if c['Name'] == agecategory_val)
		bowtype_id = next(b['Id'] for b in self.bow_types if b['Name'] == bowtype_val)

		print("Saving score: ", round_val, date_val, name_val, gender_val, agecategory_val, bowtype_val, score_val, golds_val, club_member_val, sep=" | ")



if __name__ == "__main__":
	root = ctk.CTk()

	sv_ttk.set_theme(darkdetect.theme())

	AddScoreForm(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
