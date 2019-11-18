from pymongo import MongoClient
from Rating import Rating
from flask import Flask, request
import json

app = Flask(__name__)

client = MongoClient("mongodb://mongo-admin:password@192.168.16.107:27017/?authSource=admin&retryWrites=false")
db = client.ramen_rating
collection = db.ratings
rating = Rating(collection)

@app.route('/', methods = ['GET'])
def hello_world():
	return 'Hello World'

@app.route('/api/rating', methods = ['GET'])
def get_all_ratings():
	return json.dumps(rating.all())

@app.route('/api/rating/search', methods = ['GET'])
def search_ratings():
	query = request.args.to_dict()
	if 'stars' in query:
		query['stars'] = float(query['stars'])

	if 'review_id' in query:
		query['review_id'] = int(query['review_id'])

	return json.dumps(rating.find(query))

@app.route('/api/rating/store', methods = ['POST'])
def store_rating():
	data = request.form.to_dict()
	if 'stars' in data:
		data['stars'] = float(data['stars'])

	if 'review_id' in data:
		data['review_id'] = int(data['review_id'])

	res = rating.store(data)
	return json.dumps(rating.find({'_id': res.inserted_id}))

@app.route('/api/rating/update', methods = ['POST'])
def update_rating():
	query = request.args.to_dict()
	if 'stars' in query:
		query['stars'] = float(query['stars'])

	if 'review_id' in query:
		query['review_id'] = int(query['review_id'])

	data = request.form.to_dict()
	if 'stars' in data:
		data['stars'] = float(data['stars'])

	if 'review_id' in data:
		data['review_id'] = int(data['review_id'])

	res = rating.update(query, data)
	return str(res.modified_count) + " ratings updated."

@app.route('/api/rating/delete', methods = ['POST'])
def delete_rating():
	data = request.form.to_dict()
	if 'stars' in data:
		data['stars'] = float(data['stars'])

	if 'review_id' in data:
		data['review_id'] = int(data['review_id'])

	res = rating.delete(data)
	return str(res.deleted_count) + " ratings deleted."

@app.route('/api/rating/review_count', methods = ['GET'])
def get_review_count():
	return json.dumps(rating.get_review_count_by_stars())

@app.route('/api/rating/average_stars', methods = ['GET'])
def get_average_stars():
	return json.dumps(rating.get_average_stars_by_country())

if __name__ == '__main__':
   app.run(host='127.0.0.1', debug=True)