import tkinter as tk

from customtkinter import StringVar, BooleanVar

from src.components.TabbableCheckBox import TabbableCheckBox


class LabeledCheckbox(tk.Frame):
	def __init__(self, parent, label_text: str, *args, **kwargs):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var, *args, **kwargs)
		self.label.grid(row=0, column=0, sticky="w")

		self.entry_var = BooleanVar()
		self.entry = TabbableCheckBox(self, text='', variable=self.entry_var, onvalue=True, offvalue=False)
		self.entry.grid(row=1, column=0, sticky="nsew")
