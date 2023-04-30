import bcrypt

from pymongo import MongoClient

# Configuration de la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['neolegal_db']
collection = db['users']

# Création de la collection 'users' avec des champs de base
  
# generating the salt
salt = bcrypt.gensalt()

# example password
password1 = 'test1'
  
# converting password to array of bytes
bytes1 = password1.encode('utf-8')
  
# Hashing the password
hash1 = bcrypt.hashpw(bytes1, salt)

collection.insert_one({"username": "massi_bek", "password": hash1, "firstname": "Massi", "lastname": "Bekr"})

# example password
password2 = 'test2'

# converting password to array of bytes
bytes2 = password2.encode('utf-8')
  
# Hashing the password
hash2 = bcrypt.hashpw(bytes2, salt)

collection.insert_one({"username": "dave_khal", "password": hash2, "firstname": "Dave", "lastname": "Khal"})

# example password
password3 = 'test3'

# converting password to array of bytes
bytes3 = password3.encode('utf-8')
  
# Hashing the password
hash3 = bcrypt.hashpw(bytes3, salt)

collection.insert_one({"username": "karima_khal", "password": hash3, "firstname": "Karima", "lastname": "Khal"})


# example password
password4 = 'test4'

# converting password to array of bytes
bytes4 = password4.encode('utf-8')
  
# Hashing the password
hash4 = bcrypt.hashpw(bytes4, salt)

collection.insert_one({"username": "sarah_khal", "password": hash4, "firstname": "Sarah", "lastname": "Khal"})