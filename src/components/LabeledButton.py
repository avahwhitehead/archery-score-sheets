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

		self.button.bind('<KeyRelease-space>', self.on_enter)
		self.button.bind('<KeyRelease-Return>', self.on_enter)

	def on_enter(self, e=None):
		original_fg_color = self.button.cget('fg_color')
		self.button.configure(fg_color=self.button.cget('hover_color'))

		self.button.invoke()

		self.after(150, lambda x=None: self.button.configure(fg_color=original_fg_color))

	def _on_focus(self, e=None):
		self.button.configure(border_color=self.button.cget('hover_color'))
		self.button.configure(border_width=3)

	def _on_focus_out(self, e=None):
		self.button.configure(border_width=0)
