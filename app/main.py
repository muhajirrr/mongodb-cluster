from pymongo import MongoClient
from Rating import Rating

client = MongoClient("mongodb://mongo-admin:password@192.168.16.107:27017/?authSource=admin")
db = client.ramen_rating

rating = Rating(db)
rating.test()