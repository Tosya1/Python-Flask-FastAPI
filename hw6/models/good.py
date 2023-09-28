from pydantic import BaseModel, Field


class GoodIn(BaseModel):
    name: str = Field(max_length=64)
    description: str = Field(max_length=250, default='No description')
    price: float = Field(min=0)


class Good(GoodIn):
    id: int
