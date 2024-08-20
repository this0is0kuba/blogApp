from sqlmodel import Session
from app.repositories import blog_repository


def find_blogs(offset: int, limit: int, session: Session):
    return blog_repository.find_blogs(offset, limit, session)


def find_blog(blog_id: int, session: Session):
    return blog_repository.find_blog(blog_id, session)


def find_blog_with_author(blog_id: int, session: Session):
    return blog_repository.find_blog_with_author(blog_id, session)
