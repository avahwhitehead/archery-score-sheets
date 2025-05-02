from sqlite3 import Cursor

from src.data.dbwrapper import DbWrapper
from src.entities.archer import Archer
from src.exceptions.DatabaseException import DatabaseException


class ArcheryDb:
	def __init__(self):
		self.db_wrapper = DbWrapper('C:\\tmp\\test_archery.db')

	def query_one(self, query, values = None):
		return self.db_wrapper.query_one(query, values)

	def query_all(self, query, values = None):
		return self.db_wrapper.query_all(query, values)

	def execute(self, query, values = None) -> Cursor:
		return self.db_wrapper.execute(query, values)

	def execute_many(self, query, values = None) -> Cursor:
		return self.db_wrapper.execute_many(query, values)

	def add_archer(self, archer: Archer) -> Archer:
		"""
		Adds a new Archer record to the database.
		:param archer: The Archer object containing the details to be added to the database.
		:return: The Archer object updated with the database ID.
		:raises DatabaseException: If the database query does not return a lastrowid
		:raises Exception: If the insertion fails
		"""
		cursor = self.execute(
			'INSERT INTO Archer (Name, Dob, AgbNumber, Notes) VALUES (?, ?, ?, ?)',
			[archer.name, archer.date_of_birth, archer.agb_number, archer.notes]
		)

		if cursor.lastrowid is None:
			raise DatabaseException("Could not get last row id after insert")

		archer.id = cursor.lastrowid

		return archer

	def get_archer_by_name(self, name: str):
		"""
		Finds and returns an Archer object, representing the object found in the database, with the given name.
		:param name: The name of the archer to look for.
		:return: Archer object representing the entity found in the database.
		:return: None, if no archer with the given name was found in the database.
		"""
		archer_row = self.query_one(
			'''
            SELECT Id, Name, Dob, AgbNumber, Notes FROM Archer
            WHERE Name = ?
			''',
			[name]
		)

		if archer_row is None:
			return None

		return Archer(
			id = archer_row['Id'],
			name = archer_row['Name'],
			date_of_birth = archer_row['Dob'],
			agb_number = archer_row['AgbNumber'],
			notes = archer_row['Notes']
		)