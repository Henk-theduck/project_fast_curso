import pytest
from app.use_cases.category import CategoryUseCases
from app.database.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput
from fastapi.exceptions import HTTPException
def test_add_category_uc(database_session):
    uc = CategoryUseCases(database_session)
    category = Category(
        name = 'Roupa',
        slug = 'roupa'
    )
    uc.add_category(category=category)
    
    categories_on_db = database_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    assert categories_on_db[0].name == 'Roupa'
    assert categories_on_db[0].slug == 'roupa'

    database_session.delete(categories_on_db[0])
    database_session.commit()

def test_list_categories_uc(database_session, categories_on_db):
    uc = CategoryUseCases(db_session=database_session)

    categories = uc.list_categories()

    assert len(categories) == len(categories_on_db)
    assert type(categories[0]) == CategoryOutput
    assert categories[0].id == categories_on_db[0].id
    assert categories[0].name == categories_on_db[0].name
    assert categories[0].slug == categories_on_db[0].slug

def test_delete_category_uc(database_session):
    category_model = CategoryModel(
        name = 'Roupa',
        slug = 'roupa'
    )
    database_session.add(category_model)
    database_session.commit()
    uc = CategoryUseCases(db_session=database_session)
    uc.delete_category(id=category_model.id)


    category_model = database_session.query(CategoryModel).first()
    assert category_model is None

def test_delete_category_uc_no_exist(database_session):
    uc = CategoryUseCases(db_session=database_session)
    with pytest.raises(HTTPException):
        uc.delete_category(id=1)
    