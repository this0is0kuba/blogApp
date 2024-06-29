from fastapi import APIRouter, Query, HTTPException
from models import BlogPublic, BlogPublicWithAuthorAndComments
from app.controllers.blog_controller import *

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)


@router.get("/", response_model=list[BlogPublic])
async def read_blogs(offset: int = 0, limit: int = Query(default=12, le=24)):
    return find_blogs(offset, limit)


@router.get("/{blog_id}", response_model=BlogPublicWithAuthorAndComments)
async def read_blog(blog_id: int):

    blog = find_blog(blog_id)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    else:
        return blog

