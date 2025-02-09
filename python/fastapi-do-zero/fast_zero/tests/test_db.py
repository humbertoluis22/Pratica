from fast_zero.models import User, table_registry
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session
from datetime import datetime

def test_create_user(session):
   
    user = User(
        username="Humberto", password="MinhaSenhaLegal", email="humberto@gmail.com",update_at =  datetime.now()

    )
    session.add(user)
    session.commit()
    # session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == 'humberto@gmail.com')
    )#retorna um objeto python

    assert  result.id == 1