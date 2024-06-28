from fastapi import FastAPI
from database import create_db_and_tables
from routers import blog_router, category_router


app = FastAPI()

app.include_router(blog_router)
app.include_router(category_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

