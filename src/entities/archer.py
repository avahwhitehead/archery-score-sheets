import datetime


class Archer:
	id: int
	name: str
	date_of_birth: datetime.date or None
	agb_number: str or None
	notes: str or None

	def __init__(self, id: int = None, name: str = None, date_of_birth: datetime.date = None, agb_number: str = None, notes: str = None):
		self.id = id
		self.name = name
		self.date_of_birth = date_of_birth
		self.agb_number = agb_number
		self.notes = notes