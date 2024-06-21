from fastapi import FastAPI
from app.routers.category_routes import router as category_routes


app = FastAPI()


app.include_router(category_routes)

@app.get("/")
def read_root():
    return {"Hello": "World"}
