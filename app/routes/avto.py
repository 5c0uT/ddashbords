from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.models import Avto
from app.schemas import AvtoCreate, AvtoResponse
from app.auth import get_current_user

router = APIRouter()

@router.post("/avto/", response_model=AvtoResponse)
async def create_avto(avto: AvtoCreate, current_user: dict = Depends(get_current_user)):
    db = SessionLocal()
    db_avto = Avto(**avto.dict())
    db.add(db_avto)
    db.commit()
    db.refresh(db_avto)
    return db_avto

@router.get("/avto/{avto_id}", response_model=AvtoResponse)
async def read_avto(avto_id: int, current_user: dict = Depends(get_current_user)):
    db = SessionLocal()
    avto = db.query(Avto).filter(Avto.id == avto_id).first()
    if not avto:
        raise HTTPException(status_code=404, detail="Avto not found")
    return avto
