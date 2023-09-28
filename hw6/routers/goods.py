import random
from typing import List
from fastapi import APIRouter
from db import goods, database
from models.good import Good, GoodIn

router = APIRouter()

"""
creating test goods

@router.get("/fake_goods/{count}")
async def create_good(count: int):
    for i in range(1, count + 1):
        query = goods.insert().values(
            name=f"good{i}",
            description=f"good{i}_description",
            price=random.randint(1, 250),
        )
        await database.execute(query)
    return {"message": f"{count} fake goods create"}
"""

@router.get("/goods/", response_model=List[Good])
async def get_goods():
    query = goods.select()
    return await database.fetch_all(query)


@router.post("/goods/", response_model=Good)
async def create_good(new_good: GoodIn):
    query = goods.insert().values(**new_good.model_dump())
    last_record_id = await database.execute(query)
    return {"id": last_record_id, **new_good.model_dump()}


@router.get("/goods/{good_id}", response_model=Good)
async def get_good(good_id: int):
    query = goods.select().where(goods.c.id == good_id)
    return await database.fetch_one(query)


@router.put("/goods/{good_id}", response_model=Good)
async def update_good(good_id: int, good: GoodIn):
    query = goods.update().where(goods.c.id == good_id).values(**good.model_dump())
    await database.execute(query)
    return {"id": good_id, **good.model_dump()}


@router.delete("/goods/{good_id}")
async def del_good(good_id: int):
    query = goods.delete().where(goods.c.id == good_id)
    await database.execute(query)
    return {"message": "Good deleted"}
