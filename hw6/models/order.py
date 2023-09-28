from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Status(Enum):
    CREATED = "created"
    CONFIRMED = "confirmed"
    PAID = "paid"
    SENT = "sent"
    DELIVERED = "delivered"


class OrderIn(BaseModel):
    user_id: int
    good_id: int
    created_on: datetime
    status: Status


class Order(OrderIn):
    id: int


class OrderOut(BaseModel):
    id: int
    user_id: int
    user_name: str = Field(max_length=32)
    user_last_name: str = Field(max_length=32)
    good_id: int
    good_name: str = Field(max_length=64)
    good_price: float = Field(min=0)
    created_on: datetime
    status: Status
