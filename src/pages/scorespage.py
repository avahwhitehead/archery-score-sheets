import tkinter as tk

import darkdetect
import sv_ttk
import tksheet

from src.data.archerydb import ArcheryDb
from src.data.databaseinit import DatabaseInit
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
		AddScoreForm(self).grid(row=0, sticky="nsew", padx=10, pady=10)

		# Display grid
		data = self.database.query_all(
			'''
			SELECT 
				Archer.Name,
				BowType.Name,
				Gender.Name,
				AgeCategory.Name,
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

		self.sheet = tksheet.Sheet(
			self,
			headers=['Name', 'Gender', 'Age Category', 'Bow Type', 'Round', 'Golds', 'Score'],
			# data=[[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(5)] for r in range(500)],
			data=data,
			auto_resize_rows=10,
			auto_resize_columns=100,
			vertical_grid_to_end_of_window=True,
		)
		self.sheet.enable_bindings()

		self.sheet.grid(row=1, sticky="nsew", padx=10, pady=10)


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	ScoresPage(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
