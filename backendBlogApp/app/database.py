from sqlmodel import create_engine, SQLModel

# lines needed to initialize all models properly (It's necessary to import them to the main.py file)
# from models import *  # noqa

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
