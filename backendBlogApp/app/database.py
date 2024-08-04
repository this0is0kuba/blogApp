from sqlmodel import create_engine, SQLModel, Session

# lines needed to initialize all models properly
from models import User, Blog, Role, Comment, Tag, Category  # noqa

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def drop_database():
    SQLModel.metadata.drop_all(engine)
