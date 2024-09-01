from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.token import Token
from typing import Annotated
from database import get_session, Session
from app.controllers.security_controller import create_token, authenticate_user

router = APIRouter(
    prefix="/token",
    tags=["security"]
)


@router.post("")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_session)]
) -> Token:

    user = authenticate_user(form_data.username, form_data.password, session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return create_token(user)
