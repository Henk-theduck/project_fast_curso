from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.category import Category
from app.routers.dependencies import get_db_session
from app.use_cases.category import CategoryUseCases

router = APIRouter(prefix='/category', tags=['Category'])



@router.post('/add')
def add_category(category: Category, db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category)
    return Response(status_code=status.HTTP_201_CREATED)


@router.get('/list')
def list_category(db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    categories = uc.list_categories()
    return categories

@router.delete('/delete/{id}')
def delete_category(id: int, db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id=id)
    
    return Response(status_code=status.HTTP_200_OK)