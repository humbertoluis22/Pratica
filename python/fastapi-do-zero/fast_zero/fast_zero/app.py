from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm
from fast_zero.schemas import Message,UserSchema,UserPublic,UserList
from http import HTTPStatus

from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session

from fast_zero.settings import Settings
from fast_zero.models import User
from fast_zero.schemas import UserDB,UserList,UserPublic,UserSchema
from fast_zero.security import get_password_hash,verify_password

from fast_zero.database import get_session
from datetime import datetime


app = FastAPI()

@app.get("/",status_code = HTTPStatus.OK,response_model=Message)
def read_root():
    return {"message": "Hello world"}


@app.post('/users/',status_code=HTTPStatus.CREATED ,response_model=UserPublic)
def create_user(user:UserSchema,session:Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.user)| (User.email == user.email)
        )
    )
    if db_user:
        if db_user.username == user.user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail = 'Username already exists'
            )
        if db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail = 'Email already exists'
            )    
    db_user = User(
        username=user.user,
        email = user.email,
        password=get_password_hash(user.password),
        update_at=datetime.now())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user    



@app.get('/users/',response_model=UserList)
def read_users(limit:int = 10,skip:int = 0 ,session: Session = Depends(get_session)):
    user = session.scalars(
        select(User).limit(limit).offset(skip)
    )
    return {'users': user}


@app.put('/users/{user_id}',response_model=UserPublic)
def update_user(user_id :int , user:UserSchema,session:Session= Depends(get_session)):
    db_user = session.scalars(select(User).where(User.id== user_id)).first()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,detail='not found')
    
    db_user.email = user.email
    db_user.password = get_password_hash(user.password)
    db_user.user = user.user

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user



@app.delete('/users/{user_id}',response_model=Message)
def delete_user(user_id : int,session:Session = Depends(get_session)):
    db_user = session.scalars(select(User).where(User.id== user_id)).first()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,detail='not found')
    
    session.delete(db_user)
    session.commit()
    return {'message':'User deleted'}



@app.get('/users/{user_id}',response_model=UserPublic)
def read_users_id(user_id:int,session:Session = Depends(get_session)):
    db_user = session.scalars(select(User).where(User.id== user_id)).first()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,detail='not found')
    
    return  db_user


@app.post('/token')
def login_for_acess_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    user = session.scalar(select(User).where(User.email == form_data.email))
    if not user or not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=400,detail='Incorrect email or password')