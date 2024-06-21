from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.database.models import Category as CategoryModel
from app.use_cases.category import CategoryUseCases
from app.schemas.category import CategoryOutput
client = TestClient(app)

def test_add_category_route(database_session):
    body = {
        'name' : 'Roupa',
        'slug' : 'roupa'
    }

    response = client.post('/category/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories_on_db = database_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    database_session.delete(categories_on_db[0])
    database_session.commit()


def test_list_categories_route(categories_on_db):
    response = client.get('/category/list')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert len(data) == 5
    assert data[0] == {
         'name': categories_on_db[0].name,
         'slug': categories_on_db[0].slug,
         'id': categories_on_db[0].id
    }

def test_get_category_route(database_session):
    category_model = CategoryModel(
        name = 'Roupa',
        slug = 'roupa'
    )
    database_session.add(category_model)
    database_session.commit()

    response = client.delete(f'category/delete/{category_model.id}')

    assert response.status_code == status.HTTP_200_OK

    category_model = database_session.query(CategoryModel).first()
    assert category_model is None