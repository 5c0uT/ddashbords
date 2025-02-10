from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class AvtoCreate(BaseModel):
    brand: str
    model: str
    year: int

class AvtoResponse(AvtoCreate):
    id: int
