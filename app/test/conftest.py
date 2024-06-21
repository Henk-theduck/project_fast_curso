import  pytest
from app.database.config import Session
from app.database.models import Category as CategoryModel

@pytest.fixture()
def database_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(database_session):
    categories = [
        CategoryModel(
            name = 'Roupa',
            slug = 'roupa-de-cama'
        ),
        CategoryModel(
            name = 'Eletrônicos',
            slug = 'eletronicos'
        ),
        CategoryModel(
            name = 'Móveis',
            slug ='moveis'
        ),
        CategoryModel(
            name = 'Livros',
            slug = 'livros'
        ),
        CategoryModel(
            name = 'Jogos',
            slug = 'jogos'
        )
    ]

    for category in categories:
        database_session.add(category)
    database_session.commit()

    for category in categories:
        database_session.refresh(category)

    yield categories

    for category in categories:
        database_session.delete(category)
    
    database_session.commit()