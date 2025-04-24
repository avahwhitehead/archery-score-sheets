import tkinter as tk

class NumericEntry(tk.Entry):
	def __init__(self, master=None, **kwargs):
		self.var = tk.StringVar()
		tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)

		self.old_value = ''

		self.var.trace('w', self.check)
		self.get, self.set = self.var.get, self.var.set

		self.bind('<Up>', self.on_up_key)
		self.bind('<Down>', self.on_down_key)


	def check(self, *args):
		curr_value = self.get()

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
			self.set(self.old_value)

	def on_up_key(self, event):
		self.increment()

	def on_down_key(self, event):
		self.decrement()

	def increment(self):
		curr_val = self.get()
		if curr_val == '':
			curr_val = 0

		self.set(str(int(curr_val) + 1))

	def decrement(self):
		curr_val = self.get()
		if curr_val == '':
			curr_val = 0

		self.set(str(int(curr_val) - 1))