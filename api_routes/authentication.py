from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schema import Login, UserOut, UserCreate
from Database import get_db
from models import User
from hashing import Hash
from JWTtoken import create_access_token

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()

    if not user or not Hash.verify(user.hashed_password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )


    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
