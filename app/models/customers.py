from datetime import date, datetime
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sales import Sales


# Base model with common fields (for responses)
class CustomerBase(SQLModel):
    customer_id: int
    first_name: str
    last_name: str
    gender: str
    birthdate: date
    email: str
    phone: str
    address: str
    city: str
    state: str
    country: str
    postal_code: str
    signup_date: date
    last_login: datetime
    loyalty_points: int
    yearly_income: float
    marital_status: str
    num_children: int
    education_level: str
    occupation: str
    home_owner: bool


# Table model (for database)
class Customers(CustomerBase, table=True):
    customer_id: int = Field(default=None, primary_key=True)
    sales: list["Sales"] = Relationship(back_populates="customer")


class CustomersList(SQLModel):
    data: list[CustomerBase]
    count: int
