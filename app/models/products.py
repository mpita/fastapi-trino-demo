from datetime import date
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sales import Sales


# Base model with common fields (for responses)
class ProductBase(SQLModel):
    product_id: int
    name: str
    category: str
    subcategory: str
    brand: str
    price: float
    weight: float
    manufacture_date: date


# Table model (for database)
class Products(ProductBase, table=True):
    product_id: int = Field(default=None, primary_key=True)
    sales: list["Sales"] = Relationship(back_populates="product")


class ProductsList(SQLModel):
    data: list[ProductBase]
    count: int

