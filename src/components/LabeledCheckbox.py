import tkinter as tk

import customtkinter as ctk
from customtkinter import StringVar, BooleanVar


class LabeledCheckbox(tk.Frame):
	def __init__(self, parent, label_text: str, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var)
		self.label.grid(row=0, column=0, sticky="w")

		self.entry_var = BooleanVar()
		self.entry = ctk.CTkCheckBox(self, text='', variable=self.entry_var, onvalue=True, offvalue=False)
		self.entry.grid(row=1, column=0, sticky="nsew")