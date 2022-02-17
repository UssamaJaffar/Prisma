from operator import imod
from pymongo import MongoClient

db = MongoClient()

db_vehicles = db['vehicle']