import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel

class Category(CustomBaseModel):
    name: str
    slug: str

    @field_validator('slug')
    def slug_validator(cls, value):
        if not re.match(r'^[a-z\-]+$', value):
            raise ValueError('Invalid slug')
        return value
    
class CategoryOutput(Category):
    id: int