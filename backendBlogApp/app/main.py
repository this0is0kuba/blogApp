from fastapi import FastAPI
from database import create_db_and_tables, drop_database

# lines needed to initialize all models properly (It's necessary to import them to the main.py file)
from models import User, Blog, Role, Comment, Tag, Category  # noqa

app = FastAPI()


@app.on_event("startup")
def on_startup():

    drop_database()
    create_db_and_tables()
