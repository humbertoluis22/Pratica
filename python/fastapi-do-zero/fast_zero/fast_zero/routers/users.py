from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

from fast_zero.schemas import UserSchema, UserList, UserPublic, Message
from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.security import get_current_user, get_session, get_password_hash

T_Session = Annotated[Session,Depends(get_session)]
T_Current_user = Annotated[User ,Depends(get_current_user)] 

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UserList)
def read_users(
    session: T_Session,
    limit: int = 10,
    skip: int = 0,
):
    user = session.scalars(select(User).limit(limit).offset(skip))
    return {"users": user}


@router.post("/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: T_Session):
    db_user = session.scalar(
        select(User).where((User.username == user.user) | (User.email == user.email))
    )
    if db_user:
        if db_user.username == user.user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail="Username already exists"
            )
        if db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail="Email already exists"
            )
    db_user = User(
        username=user.user,
        email=user.email,
        password=get_password_hash(user.password),
        update_at=datetime.now(),
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.put("/{user_id}", response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: T_Session,
    current_user: T_Current_user,
):
    if current_user.id != user_id:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Not enough permission")

    current_user.email = user.email
    current_user.password = get_password_hash(user.password)
    current_user.user = user.user

    session.add(current_user)
    session.commit()
    session.refresh(current_user)

    return current_user


@router.delete("/{user_id}", response_model=Message)
def delete_user(
    user_id: int,
    session: T_Session,
    current_user:T_Current_user,
):
    if current_user.id != user_id:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Not enough permission")

    session.delete(current_user)
    session.commit()
    return {"message": "User deleted"}


@router.get("/{user_id}", response_model=UserPublic)
def read_users_id(user_id: int, session: T_Session):
    db_user = session.scalars(select(User).where(User.id == user_id)).first()
    if not db_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="not found")

    return db_user
