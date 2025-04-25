import sqlite3


class ArcheryDb:
	def __init__(self):
		self.connection = sqlite3.connect('C:\\tmp\\test_archery.db')
		self.connection.row_factory = sqlite3.Row

	def query_one(self, query):
		cursor = self.connection.cursor()
		res = cursor.execute(query)
		return res.fetchone()

	def query_all(self, query):
		cursor = self.connection.cursor()
		res = cursor.execute(query)
		return res.fetchall()

	def execute(self, query):
		cursor = self.connection.cursor()
		cursor.execute(query)
		self.connection.commit()

	def execute_many(self, query, values):
		cursor = self.connection.cursor()
		cursor.executemany(query, values)
		self.connection.commit()
