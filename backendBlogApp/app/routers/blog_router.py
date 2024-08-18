from fastapi import APIRouter, Query, HTTPException, Depends
from controllers.security_controller import get_current_active_user
from models import BlogPublic, BlogPublicWithAuthor, User
from app.controllers.blog_controller import *

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)


@router.get("/", response_model=list[BlogPublic])
def read_blogs(
        offset: int = 0,
        limit: int = Query(default=12, le=24),
        session: Session = Depends(get_session)
):

    return find_blogs(offset, limit, session)


@router.get("/{blog_id}", response_model=BlogPublicWithAuthor)
def read_blog(
        blog_id: int,
        current_user: User = Depends(get_current_active_user),
        session: Session = Depends(get_session)
):

    print(current_user.username)

    blog = find_blog_with_author(blog_id, session)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    else:
        return blog

