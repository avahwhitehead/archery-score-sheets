import os
import tkinter as tk
from tkinter import StringVar

import customtkinter as ctk

from PIL import Image, ImageTk

class LabeledOptionMenu(tk.Frame):
	def __init__(self, parent, label_text, value: str, values: list[str], *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var)
		self.label.grid(row=0, column=0, sticky="w")

		self.entry_var = StringVar()
		self.entry_var.set(value)

		self.entry = ctk.CTkOptionMenu(self, variable=self.entry_var, values=values)

		self.entry.grid(row=1, column=0, sticky="nsew")
