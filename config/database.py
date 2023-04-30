from pymongo import MongoClient


connection = MongoClient('mongodb://localhost:27017/')

neolegal_db = connection['neolegal_db']

