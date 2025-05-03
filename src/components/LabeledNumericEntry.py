import tkinter as tk
from tkinter import StringVar

from src.components.NumericEntry import NumericEntry


class LabeledNumericEntry(tk.Frame):
	def __init__(self, parent, label_text: str, *args, **kwargs):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=0)

		self.label_var = StringVar()
		self.label_var.set(label_text)

		self.label = tk.Label(self, textvariable=self.label_var, *args, **kwargs)
		self.label.grid(row=0, column=0, sticky="w")

		self.entry = NumericEntry(self)
		self.entry.grid(row=1, column=0, sticky="nsew")

		self.entry_var = self.entry.var

		self.entry.bind('<Tab>', self.on_tab_pressed)
		self.entry.bind('<Shift-Tab>', self.on_shift_tab_pressed)

	def on_tab_pressed(self, event):
		"""Move focus to the next widget"""
		widget = event.widget
		next_widget = self._focus_next(widget)
		next_widget.focus()
		return "break"

	def on_shift_tab_pressed(self, event):
		"""Move focus to the previous widget"""
		widget = event.widget
		next_widget = self._focus_prev(widget)
		next_widget.focus()
		return "break"

	def _focus_next(self, widget):
		"""Return the next widget in tab order"""
		widget = self.tk.call('tk_focusNext', widget._w)
		if not widget:
			return None
		return self.nametowidget(widget.string)

	def _focus_prev(self, widget):
		"""Return the previous widget in tab order"""
		widget = self.tk.call('tk_focusPrev', widget._w)
		if not widget:
			return None
		return self.nametowidget(widget.string)
