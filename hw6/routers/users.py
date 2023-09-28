from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from db import users, database
from models.user import UserIn, UserOut

router = APIRouter()

"""
creating test users

@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(1, count + 1):
        query = users.insert().values(
            name=f"user{i}",
            last_name=f"last_name{i}",
            email=f"user{i}@mail.ru",
            password=f"password{i}",
        )
        await database.execute(query)
    return {"message": f"{count} fake users create"}
"""

@router.get("/users/", response_model=List[UserOut])
async def get_users():
    query = select(users.c.id, users.c.name, users.c.last_name, users.c.email)
    return await database.fetch_all(query)


@router.post("/users/", response_model=UserOut)
async def create_user(new_user: UserIn):
    query = users.insert().values(**new_user.model_dump())
    last_record_id = await database.execute(query)
    return {
        "id": last_record_id,
        "name": new_user.name,
        "last_name": new_user.last_name,
        "email": new_user.email,
    }


@router.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    query = select(users.c.id, users.c.name, users.c.last_name, users.c.email).where(
        users.c.id == user_id
    )
    return await database.fetch_one(query)


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**user.model_dump())
    await database.execute(query)
    return {
        "id": user_id,
        "name": user.name,
        "last_name": user.last_name,
        "email": user.email,
    }


@router.delete("/users/{user_id}")
async def del_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}
