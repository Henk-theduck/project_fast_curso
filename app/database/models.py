from database.base import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'category'
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    name = Column('name',String(100), nullable=False)
    slug = Column('slug',String(100), nullable=False)
    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'product'
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    name = Column('name',String(100), nullable=False)
    slug = Column('slug',String(100), nullable=False)
    price = Column('price',Float, nullable=False)
    stock = Column('stock', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    category_id = Column('category_id', Integer, ForeignKey('category.id'), nullable=False)
    category = relationship('Category', back_populates='products')