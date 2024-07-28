from sqlmodel import Session, select
from models.category import Category
from database import engine


def find_controllers():
    with Session(engine) as session:

        categories = session.exec(
            select(Category)
        ).all()

        return categories
