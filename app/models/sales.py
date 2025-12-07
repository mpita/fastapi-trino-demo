from datetime import date, datetime
from sqlmodel import SQLModel, Field


class Sales(SQLModel, table=True):
    sale_id: int = Field(default=None, primary_key=True)
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


class SalesList(SQLModel):
    data: list[Sales]
    count: int