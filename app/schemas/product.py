import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel


class Product(CustomBaseModel):
    name: str
    slug: str
    price: float
    stock: int

    @field_validator('slug')
    def slug_validator(cls, value):
        if not re.match(r'^[a-z\-]+$', value):
            raise ValueError('Invalid slug')
        return value
    
    @field_validator('price')
    def price_validator(cls, value):
        if value <= 0:
            raise ValueError('Invalid price')
        return value