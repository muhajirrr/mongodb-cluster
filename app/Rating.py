class Rating():
	def __init__(self, collection):
		self.collection = collection

	def store(self, rating):
		return self.collection.insert_one(rating)

	def all(self):
		return list(self.collection.find({}, {'_id': False}))

	def find(self, filter):
		return list(self.collection.find(filter, {'_id': False}))

	def update(self, filter, update):
		return self.collection.update_many(filter, {'$set': update})

	def delete(self, filter):
		return self.collection.delete_many(filter)

	def get_review_count_by_stars(self):
		pipeline = [
			{ "$group": { "_id": "$stars", "total": { "$sum": 1 } } }
		]

		return list(self.collection.aggregate(pipeline))

	def get_average_stars_by_country(self):
		pipeline = [
			{ "$group": { "_id": "$country", "average": { "$avg": "$stars" } } }
		]

		return list(self.collection.aggregate(pipeline))