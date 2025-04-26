from src.data.archerydb import ArcheryDb


class DatabaseInit:
	def __init__(self):
		self.database = ArcheryDb()

		self._age_categories = [
			('Under 12',),
			('Under 14',),
			('Under 15',),
			('Under 16',),
			('Under 18',),
			('Under 21',),
			('Adult',),
			('50+',),
		]

		self._bow_types = [
			('Barebow',),
			('Compound',),
			('Longbow',),
			('Recurve',),
		]

		self._genders = [
			('Male',),
			('Female',),
		]

		self._rounds = [
			['Portsmouth', False],
			['Vegas', False],
			['Worcester', False],
			['Frostbite', False],

			['10yds 252', True],
			['20yds 252', True],
			['30yds 252', True],
			['40yds 252', True],
			['50yds 252', True],
			['60yds 252', True],
			['70yds 252', True],
			['80yds 252', True],
			['100yds 252', True],
		]

		self._archers = [
			('John Doe',),
			('Alice Aliceton',),
			('Bob Boberton',),
			('Charlie Charlieton',),
		]

		self._scores = [
			(1, 1, 1, 1, 1, 1745601664, 10, 100)
		]

	def initialize(self):
		if self._is_db_empty():
			self._create_database()
			self._prefill_data()

	def _is_db_empty(self):
		return not self._is_db_populated()

	def _is_db_populated(self):
		tables = self.database.query_all("SELECT name FROM sqlite_master WHERE type='table'")

		for t in tables:
			if t[0] in ['AgeCategory', 'Archer', 'BowType', 'Gender', 'Round', 'Score']:
				return True

		return False

	def _create_database(self):
		self.database.execute('''
			CREATE TABLE "AgeCategory" (
				"Id"		INTEGER NOT NULL,
				"Name"		INTEGER NOT NULL,
				PRIMARY KEY("Id" AUTOINCREMENT)
			)
		''')

		self.database.execute('''
			CREATE TABLE "Archer" (
				"Id"		INTEGER NOT NULL,
				"Name"		TEXT NOT NULL,
				"Dob"		INTEGER,
				"AgbNumber"	TEXT,
				"Notes"		TEXT,
				PRIMARY KEY("Id" AUTOINCREMENT)
			)
		''')

		self.database.execute('''
			CREATE TABLE "BowType" (
				"Id"		INTEGER NOT NULL,
				"Name"		TEXT NOT NULL,
				PRIMARY KEY("Id" AUTOINCREMENT)
			)
		''')

		self.database.execute('''
			CREATE TABLE "Gender" (
				"Id"			INTEGER NOT NULL UNIQUE,
				"Name"			TEXT NOT NULL,
				PRIMARY KEY("Id" AUTOINCREMENT)
			)
		''')

		self.database.execute('''
			CREATE TABLE "Round" (
				"Id"		INTEGER NOT NULL,
				"Name"		INTEGER NOT NULL,
				"Outdoor"	INTEGER NOT NULL,
				PRIMARY KEY("Id" AUTOINCREMENT)
			)
		''')

		self.database.execute('''
			CREATE TABLE "Score" (
				"Id"			INTEGER NOT NULL,
				"ArcherId"		INTEGER NOT NULL,
				"BowTypeId"		INTEGER NOT NULL,
				"GenderId"		INTEGER NOT NULL,
				"RoundId"		INTEGER NOT NULL,
				"AgeCategoryId"	INTEGER NOT NULL,
				"DateAchieved"	INTEGER NOT NULL,
				"Golds"			INTEGER,
				"Score"			INTEGER NOT NULL,
				"ClubMember"	INTEGER NOT NULL,
				"Notes"			TEXT,
				PRIMARY KEY("Id" AUTOINCREMENT),
				FOREIGN KEY("AgeCategoryId") REFERENCES "AgeCategory"("Id"),
				FOREIGN KEY("ArcherId") REFERENCES "Archer"("Id"),
				FOREIGN KEY("BowTypeId") REFERENCES "BowType"("Id"),
				FOREIGN KEY("GenderId") REFERENCES "Gender"("Id"),
				FOREIGN KEY("RoundId") REFERENCES "Round"("Id")
			)
		''')

	def _prefill_data(self):
		self.database.execute_many("INSERT INTO Gender (Name) VALUES (?)", self._genders)

		self.database.execute_many("INSERT INTO AgeCategory (Name) VALUES (?)", self._age_categories)

		self.database.execute_many("INSERT INTO BowType (Name) VALUES (?)", self._bow_types)

		self.database.execute_many("INSERT INTO Round (Name, Outdoor) VALUES (?, ?)", self._rounds)

		self.database.execute_many("INSERT INTO Archer (Name) VALUES (?)", self._archers)

		self.database.execute_many("INSERT INTO Score (ArcherId, BowTypeId, GenderId, RoundId, AgeCategoryId, DateAchieved, Golds, Score) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", self._scores)

