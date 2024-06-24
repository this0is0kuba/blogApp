from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class UserBase(SQLModel):
    email: EmailStr = Field(max_length=50, index=True, unique=True)
    username: str = Field(max_length=20, index=True, unique=True)
    disabled: bool = False


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    passwordHash: str


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=30)


class UserPublic(UserBase):
    id: int

