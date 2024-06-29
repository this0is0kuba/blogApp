from sqlmodel import Session, select
from models import Blog
from database import engine


def find_blogs(offset: int, limit: int):
    with Session(engine) as session:

        blogs = session.exec(
            select(Blog).offset(offset).limit(limit)
        ).all()

        return blogs


def find_blog(blog_id: int):
    with Session(engine) as session:
        blog = session.get(Blog, blog_id)

        return blog
