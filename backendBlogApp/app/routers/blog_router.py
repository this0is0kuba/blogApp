from fastapi import APIRouter, Query, HTTPException, Depends
from models import BlogPublic, BlogPublicWithAuthor
from database import get_session
from app.controllers.blog_controller import *

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)


@router.get("/", response_model=list[BlogPublic])
async def read_blogs(session: Session = Depends(get_session),
                     offset: int = 0,
                     limit: int = Query(default=12, le=24)):

    return find_blogs(offset, limit, session)


@router.get("/{blog_id}", response_model=BlogPublicWithAuthor)
def read_blog(blog_id: int,
              session: Session = Depends(get_session)):

        blog = find_blog_with_author(blog_id, session)

        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        else:
            return blog

