from datetime import date, datetime
from sqlmodel import SQLModel, Field


class Customers(SQLModel, table=True):
    customer_id: int = Field(default=None, primary_key=True)
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


class CustomersList(SQLModel):
    data: list[Customers]
    count: int
