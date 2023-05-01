from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse, FileResponse
from typing import Optional
import bcrypt

from config.database import neolegal_db
from models.user import User
from schemas.user import usersList, usersEntity
from app.auth.jwt_hundler import get_token, check_token
from app.filter.validate import validate_schema
from app.pdf.pdf_generator import generate_pdf

user = APIRouter()
security = HTTPBearer()
users_col = neolegal_db['users']


# Endpoint d'authentification
@user.post("/authenticate")
async def authenticate(user: User):
    user_db = users_col.find_one({"username": user.username})
    password = user.password.encode('utf-8')
    isValidPassword = False
    if user_db:
        isValidPassword = bcrypt.checkpw(password, user_db['password'])
        
    if isValidPassword:
        # Créer le JWT
        token = get_token(user.username)
        return JSONResponse(content={"access token": token})
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

# Endpoint de liste des utilisateurs
@user.get("/users")
def list_users(response: Response, filter: Optional[str] = None, download: Optional[str] = None, token: HTTPAuthorizationCredentials = Depends(security)):
    users = []
    try:
        payload = check_token(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        filters = None
        if filter:
            filters = validate_schema(filter)
            # Obtenir la liste des utilisateurs
        users = users_col.find(filters)

    except:
        raise HTTPException(status_code=401, detail="Invalid filter structure")
    
    # Retourner la réponse
    if download == "pdf":
        # Générer le fichier PDF et le retourner
        pdf_name = generate_pdf(usersList(users))
        # Set the Content-Disposition header and return the PDF file as a response
        response.headers["Content-Type"] = 'application/pdf';
        response.headers["Content-Disposition"] = 'attachment; filename='+pdf_name
        return FileResponse(pdf_name)
    else:
        # Retourner la liste des utilisateurs en JSON
        return JSONResponse(content=usersEntity(users))