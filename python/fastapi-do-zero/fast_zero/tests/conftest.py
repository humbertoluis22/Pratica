import pytest
from fastapi.testclient import TestClient
from fast_zero.app import app
from fast_zero.database import get_session

from sqlalchemy import create_engine
from fast_zero.models import table_registry,User
from sqlalchemy.orm import Session
from fast_zero.security import get_password_hash

from sqlalchemy.pool import StaticPool
from datetime import datetime


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override

        yield client

    return app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    session.close()
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def user(session:Session):
    pwd = 'testtest'
    user = User(
        username="Teste",
        email="teste@test.com",
        password=get_password_hash(pwd) ,
        update_at=datetime.now())
    
    session.add(user)   
    session.commit()
    session.refresh(user)

    user.clean_password = pwd #monkey patch
    return user

@pytest.fixture
def token(client,user):
    response = client.post(
        '/auth/token',
        data = {'username':user.email,'password':user.clean_password}
    )
    return response.json()['access_token']