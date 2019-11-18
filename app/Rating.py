

class Rating():
	def __init__(self, db):
		self.db = db

	def store(self, rating):
		return self.db.ratings.insert_one(rating)


	def all(self):
		return [r for r in self.db.ratings.find()]

	def find(self, filter):
		return [r for r in self.db.ratings.find(filter)]

	def update(self, filter, update):
		return self.db.ratings.update_many(filter, {'$set': update})

	def delete(self, filter):
		return self.db.ratings.delete_many(filter)