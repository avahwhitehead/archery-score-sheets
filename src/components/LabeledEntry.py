import tkinter as tk
from tkinter import StringVar

import customtkinter as ctk

class LabeledEntry(tk.Frame):
	def __init__(self, parent, label_text: str, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var)
		self.label.grid(row=0, column=0, sticky="w")

		self.entry_var = StringVar()
		self.entry = ctk.CTkEntry(self, placeholder_text=label_text, textvariable=self.entry_var)
		self.entry.grid(row=1, column=0, sticky="nsew")