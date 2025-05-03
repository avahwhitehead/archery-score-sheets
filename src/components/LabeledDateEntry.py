import tkinter as tk
from tkinter import StringVar

import customtkinter as ctk

from src.components.ctkdatepicker import CTkDatePicker


class LabeledDateEntry(tk.Frame):
	def __init__(self, parent, label_text: str, *args, **kwargs):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var, *args, **kwargs)
		self.label.grid(row=0, column=0, sticky="w")

		self.combobox = ctk.CTkComboBox(self)

		self.date_picker = CTkDatePicker(self.combobox)
		self.combobox.grid(row=1, column=0, sticky="nsew")
