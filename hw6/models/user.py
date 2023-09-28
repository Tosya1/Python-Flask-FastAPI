from pydantic import BaseModel, EmailStr, Field


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr = Field(max_length=32)
    password: str = Field(min_length=6, max_length=50)


class User(UserIn):
    id: int


class UserOut(BaseModel):
    id: int
    name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr = Field(max_length=32)
