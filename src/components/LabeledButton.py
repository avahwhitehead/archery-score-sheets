import tkinter as tk
from tkinter import StringVar
from typing import Any

import customtkinter as ctk

class LabeledButton(tk.Frame):
	button: ctk.CTkButton

	def __init__(self, parent, text: str, command: callable(Any), *args, **kwargs):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		# TODO: How to get this to align without the label?
		ctk.CTkLabel(self, text="", height=21).grid(row=0, column=0, sticky="w")

		self.button_var = StringVar()
		self.button_var.set(text)
		self.button = ctk.CTkButton(self, textvariable=self.button_var, command=command, *args, **kwargs)
		self.button.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

		self.button.configure(border_width=0)

		self.bind("<FocusIn>", self._on_focus)
		self.bind("<FocusOut>", self._on_focus_out)

	def _on_focus(self, e=None):
		self.button.configure(border_color=self.button.cget('hover_color'))
		self.button.configure(border_width=3)

	def _on_focus_out(self, e=None):
		self.button.configure(border_width=0)
