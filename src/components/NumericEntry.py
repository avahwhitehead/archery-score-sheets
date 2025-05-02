import tkinter as tk
from tkinter import IntVar, StringVar

import customtkinter as ctk


class NumericEntry(ctk.CTkEntry):
	def __init__(self, parent, **kwargs):
		self.var = tk.StringVar()
		ctk.CTkEntry.__init__(self, parent, **kwargs, textvariable=self.var)

		self.old_value = ''

		self.var.trace('w', self.check)

		self.bind('<Up>', self.on_up_key)
		self.bind('<Down>', self.on_down_key)


	def check(self, *args):
		curr_value = self.var.get()

		if curr_value == '':
			self.old_value = ''
			return

		is_digit = True
		try:
			int(curr_value)
		except ValueError:
			is_digit = False

		if is_digit:
			# the current value is only digits; allow this
			self.old_value = curr_value
		else:
			# there's non-digit characters in the input; reject this
			self.var.set(self.old_value)

	def on_up_key(self, event):
		self.increment()

	def on_down_key(self, event):
		self.decrement()

	def increment(self):
		curr_val = self.var.get()
		if curr_val == '':
			curr_val = '0'

		next_val = str(int(curr_val) + 1)

		self.var.set(next_val)

	def decrement(self):
		curr_val = self.get()
		if curr_val == '':
			curr_val = '0'

		next_val = str(int(curr_val) - 1)

		self.var.set(next_val)