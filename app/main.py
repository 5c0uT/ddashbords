from fastapi import FastAPI
from app.routes import users, avto
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(avto.router)

@app.get("/")
async def root():
    return {"message": "Auto Service API"}
