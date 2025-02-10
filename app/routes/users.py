from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, Token
from app.auth import create_access_token
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    db = SessionLocal()
    if db.query(User).filter(User.login == user.login).first():
        raise HTTPException(status_code=400, detail="Login already registered")
    hashed_password = pwd_context.hash(user.password)
    db_user = User(login=user.login, password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"access_token": create_access_token({"sub": user.login}), "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.login == user.login).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_access_token({"sub": user.login}), "token_type": "bearer"}
