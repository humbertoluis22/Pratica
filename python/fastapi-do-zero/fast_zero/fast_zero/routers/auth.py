from fastapi import APIRouter,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm

from fast_zero.models import User
from fast_zero.security import create_access_token,verify_password
from fast_zero.schemas import Token
from fast_zero.database import get_session
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select

router = APIRouter(prefix='/auth',tags=['auth'])

T_Session = Annotated[Session,Depends(get_session)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm,Depends()]

@router.post("/token", response_model=Token)
def login_for_acess_token(
    session: T_Session,
    form_data:T_OAuth2Form
):
    user = session.scalar(select(User).where(User.email == form_data.username))
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "Bearer"}

