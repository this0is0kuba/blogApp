from fastapi import APIRouter
from controllers.category_controller import *
from models import Category

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@router.get("/", response_model=list[Category])
async def read_categories():
    return find_controllers()
