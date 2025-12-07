from datetime import date, datetime
from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .customers import Customers
    from .products import Products


# Base model with common fields
class SaleBase(SQLModel):
    sale_id: int
    customer_id: int
    product_id: int
    sale_date: date
    sale_timestamp: datetime
    quantity: int
    unit_price: float
    discount: float
    total_price: float
    payment_method: str
    store_id: int
    channel: str


# Table model (for database)
class Sales(SaleBase, table=True):
    sale_id: int = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customers.customer_id")
    product_id: int = Field(foreign_key="products.product_id")
    customer: Optional["Customers"] = Relationship(back_populates="sales")
    product: Optional["Products"] = Relationship(back_populates="sales")


# Response model for list
class SalesList(SQLModel):
    data: list[SaleBase]
    count: int