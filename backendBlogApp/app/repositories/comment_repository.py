from sqlmodel import select
from database import Session
from models import Comment


def find_comments_by_blog_id(blog_id: int, offset: int, limit: int, session: Session):

    return session.exec(
        select(Comment).where(Comment.blog_id == blog_id).offset(offset).limit(limit)
    ).all()