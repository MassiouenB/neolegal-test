import time
import jwt
from decouple import config

# Configuration de JWT
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm") 

def get_token(username: str):
    payload = {
        "username": username,
        "expiry": time.time() + 600
        }        
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def check_token(token):
    # Vérifier le JWT
    payload = jwt.decode(token.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload