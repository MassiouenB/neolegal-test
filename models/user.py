from pydantic import BaseModel

# Modèle d'utilisateur

class User(BaseModel):
    username: str
    password: str
