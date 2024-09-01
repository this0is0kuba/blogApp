from sqlmodel import Session
from app.repositories import comment_repository


def find_comments_by_blog_id(blog_id: int, offset: int, limit: int, session: Session):
    return comment_repository.find_comments_by_blog_id(blog_id, offset, limit, session)
