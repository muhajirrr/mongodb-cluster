class Rating():
	def __init__(self, collection):
		self.collection = collection

	def store(self, rating):
		return self.collection.insert_one(rating)

	def all(self):
		return [r for r in self.collection.find({}, {'_id': False})]

	def find(self, filter):
		return [r for r in self.collection.find(filter, {'_id': False})]

	def update(self, filter, update):
		return self.collection.update_many(filter, {'$set': update})

	def delete(self, filter):
		return self.collection.delete_many(filter)