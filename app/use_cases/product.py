from fastapi import HTTPException, status
from app.database.models import Product as ProducModel
from app.database.models import Category as CategoryModel
from app.schemas.product import Product

class ProductUseCases:
    def __init__(self, db_session):
        self.db_session = db_session
    
    def add_product(self, product: Product, category_slug: str):
        category = self.db_session.query(CategoryModel).filter_by(slug=category_slug).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Category not found with {category_slug}')
        product_model = ProducModel(**product.model_dump())
        product_model.category_id = category.id
        self.db_session.add(product_model)
        self.db_session.commit()
        