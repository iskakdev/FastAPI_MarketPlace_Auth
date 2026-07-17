from pydantic import BaseModel, EmailStr
from typing import Optional
from db.models import RoleChoices
from datetime import date, datetime


class UserProfileInputSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone_number: Optional[str]


class UserProfileOutSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    phone_number: Optional[str]
    status: RoleChoices
    registered_date: datetime


class UserLoginSchema(BaseModel):
    username: str
    password: str