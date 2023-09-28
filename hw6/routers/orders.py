from datetime import datetime
import random
from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from db import orders, database, goods, users
from models.order import Order, OrderIn, OrderOut, Status


router = APIRouter()

"""
creating test orders

@router.get("/fake_orders/{count}")
async def create_order(count: int, users_count: int, goods_count: int):
    for i in range(1, count + 1):
        query = orders.insert().values(
            user_id=random.randint(1, users_count),
            good_id=random.randint(1, goods_count),
            created_on=datetime.now(),
            status=random.choice(Status._member_names_),
        )
        await database.execute(query)
    return {"message": f"{count} fake orders create"}
"""
@router.get("/orders/", response_model=List[OrderOut])
async def get_orders():
    query = (
        select(
            orders.c.id,
            orders.c.created_on,
            orders.c.status,
            goods.c.id.label("good_id"),
            goods.c.name.label("good_name"),
            goods.c.price.label("good_price"),
            users.c.id.label("user_id"),
            users.c.name.label("user_name"),
            users.c.last_name.label("user_last_name"),
        )
        .join(goods)
        .join(users)
    )
    return await database.fetch_all(query)


@router.post("/orders/", response_model=Order)
async def create_order(new_order: OrderIn):
    query = orders.insert().values(**new_order.model_dump())
    last_record_id = await database.execute(query)
    return {"id": last_record_id, **new_order.model_dump()}


@router.get("/orders/{order_id}", response_model=OrderOut)
async def get_order(order_id: int):
    query = (
        select(
            orders.c.id,
            orders.c.created_on,
            orders.c.status,
            goods.c.id.label("good_id"),
            goods.c.name.label("good_name"),
            goods.c.price.label("good_price"),
            users.c.id.label("user_id"),
            users.c.name.label("user_name"),
            users.c.last_name.label("user_last_name"),
        )
        .join(goods)
        .join(users)
        .where(orders.c.id == order_id)
    )
    return await database.fetch_one(query)


@router.get("/orders/user/{user_id}", response_model=List[OrderOut])
async def get_orders_by_user_id(user_id: int):
    query = (
        select(
            orders.c.id,
            orders.c.created_on,
            orders.c.status,
            goods.c.id.label("good_id"),
            goods.c.name.label("good_name"),
            goods.c.price.label("good_price"),
            users.c.id.label("user_id"),
            users.c.name.label("user_name"),
            users.c.last_name.label("user_last_name"),
        )
        .join(goods)
        .join(users)
        .where(orders.c.user_id == user_id)
    )
    return await database.fetch_all(query)

@router.get("/orders/status/{status}", response_model=List[OrderOut])
async def get_orders_by_user_id(status: Status):
    query = (
        select(
            orders.c.id,
            orders.c.created_on,
            orders.c.status,
            goods.c.id.label("good_id"),
            goods.c.name.label("good_name"),
            goods.c.price.label("good_price"),
            users.c.id.label("user_id"),
            users.c.name.label("user_name"),
            users.c.last_name.label("user_last_name"),
        )
        .join(goods)
        .join(users)
        .where(orders.c.status == status)
    )
    return await database.fetch_all(query)


@router.get("/orders/good/{good_id}", response_model=List[OrderOut])
async def get_orders_by_good_id(good_id: int):
    query = (
        select(
            orders.c.id,
            orders.c.created_on,
            orders.c.status,
            goods.c.id.label("good_id"),
            goods.c.name.label("good_name"),
            goods.c.price.label("good_price"),
            users.c.id.label("user_id"),
            users.c.name.label("user_name"),
            users.c.last_name.label("user_last_name"),
        )
        .join(goods)
        .join(users)
        .where(orders.c.good_id == good_id)
    )
    return await database.fetch_all(query)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, good: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**good.model_dump())
    await database.execute(query)
    return {"id": order_id, **good.model_dump()}


@router.delete("/orders/{order_id}")
async def del_good(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "Order deleted"}
