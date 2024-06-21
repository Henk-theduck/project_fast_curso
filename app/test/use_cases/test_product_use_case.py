from fastapi import HTTPException
import pytest
from app.database.models import Product as ProductModel
from app.schemas.product import Product
from app.use_cases.product import ProductUseCases

def test_add_product_uc(database_session, categories_on_db):
    uc = ProductUseCases(database_session)
    product = Product(
        name = 'Camiseta Monte Neon',
        slug = 'camiseta-monte-neon',
        price = 100.00,
        stock = 10
    )

    uc.add_product(product, category_slug=categories_on_db[0].slug)

    product_on_db = database_session.query(ProductModel).first()

    assert product_on_db is not None
    assert product_on_db.name == product.name
    assert product_on_db.slug == product.slug
    assert product_on_db.price == product.price
    assert product_on_db.stock == product.stock
    assert product_on_db.category.name == categories_on_db[0].name

    database_session.delete(product_on_db)
    database_session.commit()

def test_add_product_uc_invalid_category(database_session):
    uc = ProductUseCases(database_session)
    product = Product(
        name = 'Camiseta Monte Neon',
        slug = 'camiseta-monte-neon',
        price = 100.00,
        stock = 10
    )

    with pytest.raises(HTTPException):
        uc.add_product(product, category_slug='invalid')