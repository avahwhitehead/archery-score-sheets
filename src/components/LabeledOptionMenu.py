import tkinter as tk
from tkinter import StringVar

import customtkinter as ctk


class LabeledOptionMenu(tk.Frame):
	def __init__(self, parent, label_text, value: str, values: list[str], *args, **kwargs):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var)
		self.label.grid(row=0, column=0, sticky="w")

		self.entry_var = StringVar()
		self.entry_var.set(value)

		self._values = values

		self.entry = ctk.CTkComboBox(self, variable=self.entry_var, values=values, *args, **kwargs)
		self.entry.grid(row=1, column=0, sticky="nsew")

		self.entry.bind('<Up>', self.on_up_key)
		self.entry.bind('<Down>', self.on_down_key)

	def on_up_key(self, event):
		try:
			selected_index = self._values.index(self.entry_var.get())
		except ValueError:
			return

		if selected_index > 0:
			self.entry_var.set(self._values[selected_index - 1])

	def on_down_key(self, event):
		try:
			selected_index = self._values.index(self.entry_var.get())
		except ValueError:
			return

		if selected_index < len(self._values) - 1:
			self.entry_var.set(self._values[selected_index + 1])
