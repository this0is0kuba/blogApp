from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel

# lines needed to initialize all models properly (It's necessary to import them to the main.py file)
from models import User, Blog, Role, Comment, Tag, Category, UserRoleLink, BlogCategoryLink, BlogTagLink  # noqa

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

