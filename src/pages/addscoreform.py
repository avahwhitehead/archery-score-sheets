import tkinter as tk
from tkinter import StringVar

import darkdetect
import sv_ttk

from src.components.NumericEntry import NumericEntry


class AddScoreForm(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		# Root layout
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0, minsize=40)

		# Input fields
		input_frame = tk.Frame(self)
		input_frame.grid_rowconfigure(0, weight=1)
		input_frame.grid_rowconfigure(1, weight=1)
		input_frame.grid(row=0, column=0, sticky="nsew")

		name_label_var = StringVar()
		name_label_var.set("Name")

		name_label = tk.Label(input_frame, textvariable=name_label_var)
		name_label.grid(row=0, column=0, sticky="w")

		name_input = tk.Entry(input_frame)
		name_input.grid(row=1, column=0, sticky="nsew")

		score_label_var = StringVar()
		score_label_var.set("Score")

		score_label = tk.Label(input_frame, textvariable=score_label_var)
		score_label.grid(row=0, column=1, sticky="w")

		score_input = NumericEntry(input_frame)
		score_input.grid(row=1, column=1, sticky="nsew")


if __name__ == "__main__":
	root = tk.Tk()

	sv_ttk.set_theme(darkdetect.theme())

	AddScoreForm(root).pack(side="top", fill="both", expand=True)

	root.mainloop()
