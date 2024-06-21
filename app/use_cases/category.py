from app.database.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status

class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_category(self, category: Category):
        category_model = CategoryModel(**category.model_dump())
        self.db_session.add(category_model)
        self.db_session.commit()
    
    def list_categories(self):
        categories = self.db_session.query(CategoryModel).all()
        return [self.serialize_category(category_model=category) for category in categories]
    
    def delete_category(self, id: int):
        category_model = self.db_session.query(CategoryModel).filter_by(id=id).first()
        if not category_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
        
        self.db_session.delete(category_model)
        self.db_session.commit()
    def serialize_category(self, category_model: CategoryModel):
        return CategoryOutput(**category_model.__dict__)