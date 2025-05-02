import sqlite3
from sqlite3 import Cursor


class ArcheryDb:
	def __init__(self):
		self.connection = sqlite3.connect('C:\\tmp\\test_archery.db')
		self.connection.row_factory = sqlite3.Row

	def query_one(self, query, values):
		cursor = self.connection.cursor()
		res = cursor.execute(query, values)
		return res.fetchone()

	def query_all(self, query):
		cursor = self.connection.cursor()
		res = cursor.execute(query)
		return res.fetchall()

	def execute(self, query) -> Cursor:
		cursor = self.connection.cursor()
		cursor_used = cursor.execute(query)
		self.connection.commit()
		return cursor_used

	def execute_many(self, query, values) -> Cursor:
		cursor = self.connection.cursor()
		cursor_used = cursor.executemany(query, values)
		self.connection.commit()
		return cursor_used
