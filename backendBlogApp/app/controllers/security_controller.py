from datetime import timedelta, datetime, timezone
from typing import Annotated
import jwt
from fastapi import HTTPException, Depends, status
from jwt import InvalidTokenError
from app.configs.configs import ACCESS_TOKEN_EXPIRE_DAYS, SECRET_KEY, ALGORITHM, pwd_context, oauth2_scheme
from database import get_session
from models.token import Token, TokenData
from models import User
from sqlmodel import Session
from app.repositories import user_repository


def validate_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, session: Session):

    user: User = user_repository.find_user(username, session)

    if not user:
        return None

    if not validate_password(password, user.password_hash):
        return None

    return user


def create_access_token(data: dict, expires_delta: timedelta):

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_token(user: User) -> Token:

    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")


def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: Session = Depends(get_session)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)

    except InvalidTokenError:
        raise credentials_exception

    user = user_repository.find_user(token_data.username, session)

    if user is None:
        raise credentials_exception

    return user


def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
