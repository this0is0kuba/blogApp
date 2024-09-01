from sqlmodel import Session, select
from models import User


def find_user(username: str, session: Session):

    return session.exec(
        select(User).where(User.username == username)
    ).first()
