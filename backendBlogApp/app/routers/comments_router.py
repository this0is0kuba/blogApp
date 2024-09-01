from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from controllers.comments_controller import find_comments_by_blog_id
from controllers.security_controller import get_current_active_user
from database import get_session
from models import CommentPublic, User

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)


@router.get('/blog/{blog_id}', response_model=list[CommentPublic])
def read_comments_by_blog_id(
        blog_id: int,
        offset: int = 0,
        limit: int = Query(default=12, le=24),
        current_user: User = Depends(get_current_active_user),
        session: Session = Depends(get_session),
):
    return find_comments_by_blog_id(blog_id, offset, limit, session)