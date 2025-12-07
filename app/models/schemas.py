"""Response schemas for API endpoints."""
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class CustomerResponse(BaseModel):
    """Customer data for API responses."""
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


class ProductResponse(BaseModel):
    """Product data for API responses."""
    product_id: int
    name: str
    category: str
    subcategory: str
    brand: str
    price: float
    weight: float
    manufacture_date: date


class SaleDetail(BaseModel):
    """Sale detail with nested customer and product data."""
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
    customer: Optional[CustomerResponse] = None
    product: Optional[ProductResponse] = None
