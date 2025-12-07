from datetime import date
from sqlmodel import SQLModel, Field


class Products(SQLModel, table=True):
    product_id: int = Field(default=None, primary_key=True)
    name: str
    category: str
    subcategory: str
    brand: str
    price: float
    weight: float
    manufacture_date: date


class ProductsList(SQLModel):
    data: list[Products]
    count: int

