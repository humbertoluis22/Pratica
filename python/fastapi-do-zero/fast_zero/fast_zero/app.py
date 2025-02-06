from fastapi import FastAPI,HTTPException,Depends
from fast_zero.schemas import Message,UserSchema,UserPublic,UserDB,UserList
from http import HTTPStatus

from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session

from fast_zero.settings import Settings
from fast_zero.models import User
from fast_zero.schemas import UserDB,UserList,UserPublic,UserSchema

from fast_zero.database import get_session
from datetime import datetime


app = FastAPI()
database = []

@app.get("/",status_code = HTTPStatus.OK,response_model=Message)
def read_root():
    return {"message": "Hello world"}


@app.post('/users/',status_code=HTTPStatus.CREATED ,response_model=UserPublic)
def create_user(user:UserSchema,session = Depends(get_session)):
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
        email=user.email,
        password=user.password,
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
def update_user(user_id :int , user:UserSchema,session= Depends(get_session)):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404,detail='not found')
    
    user_with_id = UserDB(id=user_id,**user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}',response_model=Message)
def delete_user(user_id : int,session:Session = Depends(get_session)):
    db_user = session.scalars(select(User).where(User.id== user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,detail='not found')
    
    session.delete(db_user)
    session.commit()
    session.refresh()
    return {'message':'User deleted'}



@app.get('/users/{user_id}',response_model=UserPublic)
def read_users_id(user_id:int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404,detail='not found')
    
    user = database[user_id - 1]
    return user