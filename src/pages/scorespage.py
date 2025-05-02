import tkinter as tk

import customtkinter as ctk

import darkdetect
import sv_ttk
import tksheet

from src.data.archerydb import ArcheryDb
from src.pages.addscoreform import AddScoreForm


class ScoresPage(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.database = ArcheryDb()

		# Root layout
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0, minsize=40)
		self.grid_rowconfigure(1, weight=1, minsize=40)

		# Input fields
		add_score_form = AddScoreForm(self)
		add_score_form.grid(row=0, sticky="nsew", padx=10, pady=10)

		add_score_form.onSave.subscribe(lambda _: self.after(0, self.load_scores))

		# Display grid
		sheet_frame = tk.Frame(self)
		sheet_frame.grid(row=1, sticky="nsew")
		sheet_frame.grid_rowconfigure(0, weight=1)
		sheet_frame.grid_columnconfigure(0, weight=1)

		sheet_headers = ['Name', 'Gender', 'Age Category', 'Bow Type', 'Round', 'Golds', 'Score']

		self.sheet = tksheet.Sheet(
			sheet_frame,
			headers=sheet_headers,
			data=[[]],
			vertical_grid_to_end_of_window=True,
		)
		self.sheet.enable_bindings()

		self.sheet.grid(row=0, sticky="nsew", padx=10, pady=10)

		self.after(100, self.load_scores)

	def load_scores(self):
		data = self.database.query_all(
			'''
            SELECT
                Archer.Name,
                Gender.Name,
                AgeCategory.Name,
                BowType.Name,
                Round.Name,
                Score.Golds,
                Score.Score
            FROM Score
                     INNER JOIN Archer ON Score.ArcherId = Archer.Id
                     INNER JOIN BowType ON Score.BowTypeId = BowType.Id
                     INNER JOIN Gender ON Score.GenderId = Gender.Id
                     INNER JOIN AgeCategory ON Score.AgeCategoryId = AgeCategory.Id
                     INNER JOIN Round ON Score.RoundId = Round.Id
			'''
		)

		self.sheet.set_sheet_data(data)


if __name__ == "__main__":
	root = ctk.CTk()

	sv_ttk.set_theme(darkdetect.theme())

	ScoresPage(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
