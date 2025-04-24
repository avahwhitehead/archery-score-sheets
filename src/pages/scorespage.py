import tkinter as tk

import darkdetect
import sv_ttk
import tksheet

from src.pages.addscoreform import AddScoreForm


class ScoresPage(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		# Root layout
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0, minsize=40)
		self.grid_rowconfigure(1, weight=1, minsize=40)

		# Input fields
		AddScoreForm(self).grid(row=0, sticky="nsew", padx=10, pady=10)

		# Display grid
		self.sheet = tksheet.Sheet(
			self,
			data=[[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(5)] for r in range(500)],
			auto_resize_rows=10,
			auto_resize_columns=100,
			vertical_grid_to_end_of_window=True
		)
		self.sheet.enable_bindings()

		self.sheet.grid(row=1, sticky="nsew", padx=10, pady=10)


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	ScoresPage(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
