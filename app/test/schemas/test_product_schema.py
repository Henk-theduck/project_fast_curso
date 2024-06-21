

import pytest
from app.schemas.product import Product


def test_product_schema():
    product = Product(
        name = 'Camiseta Monte Neon',
        slug = 'camiseta-monte-neon',
        price = 100.00,
        stock = 10
    )

    assert product.model_dump() == {
        'name' : 'Camiseta Monte Neon',
        'slug' : 'camiseta-monte-neon',
        'price' : 100.00,
        'stock' : 10
    }

def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        Product(
            name = 'Camiseta Monte Neon',
            slug = 'cão',
            price = 100.00,
            stock = 10)
    with pytest.raises(ValueError):
        Product(
            name = 'Camiseta Monte Neon',
            slug = 'Camiseta-monte-neon',
            price = 100.00,
            stock = 10)
    with pytest.raises(ValueError):
        Product(
            name = 'Camiseta Monte Neon',
            slug = 'camiseta monte neon',
            price = 100.00,
            stock = 10)


def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        Product(
            name = 'Camiseta Monte Neon',
            slug = 'camiseta-monte-neon',
            price = -100.00,
            stock = 10)
    with pytest.raises(ValueError):
        Product(
            name = 'Camiseta Monte Neon',
            slug = 'camiseta-monte-neon',
            price = 0.00,
            stock = 10)