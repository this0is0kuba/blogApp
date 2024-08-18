from typing import Annotated
from sqlalchemy.orm import selectinload
from sqlmodel import select
from fastapi import Depends
from database import get_session, Session
from models import Blog


def find_blogs(offset: int, limit: int, session: Session):

    return session.exec(
        select(Blog).offset(offset).limit(limit)
    ).all()


def find_blog(blog_id: int, session: Session):

    return session.get(Blog, blog_id)


def find_blog_with_author(blog_id: int, session: Session):

    statement = select(Blog).where(Blog.id == blog_id).options(
        selectinload(Blog.author)
    )

    return session.exec(statement).first()
