from fastapi import FastAPI
from database import create_db_and_tables, drop_database
from initial_values_db import insert_initial_values
from routers import blog_router, category_router


app = FastAPI()

app.include_router(blog_router)
app.include_router(category_router)


@app.on_event("startup")
def on_startup():

    drop_database()
    create_db_and_tables()
    insert_initial_values()

