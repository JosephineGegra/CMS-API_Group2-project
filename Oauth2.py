from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from JWTtoken import verify_token
from sqlalchemy.orm import Session
from Database import get_db
from Models import User

# Configuration
SECRET_KEY = "905004490J2J"
ALGORITHM = "HS256"

auth_scheme = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme), db: Session = Depends(get_db)):
    data = verify_token(token.credentials)
    user = db.query(User).filter(User.email == data["email"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def require_role(role: str):
    def checker(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
        data = verify_token(token.credentials)
        if data["role"] != role:
            raise HTTPException(status_code=403, detail="Access forbidden: Admins only")
        return data
    return checker

