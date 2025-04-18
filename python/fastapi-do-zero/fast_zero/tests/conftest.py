import pytest
from fastapi.testclient import TestClient
from fast_zero.app import app
from fast_zero.database import get_session

import factory

from sqlalchemy import create_engine
from fast_zero.models import table_registry,User
from sqlalchemy.orm import Session
from fast_zero.security import get_password_hash

from sqlalchemy.pool import StaticPool
from datetime import datetime


class UserFactory(factory.Factory):
    class Meta: 
        model = User

    username = factory.sequence(lambda n : f'test{n}') 
    email =  factory.LazyAttribute(lambda obj : f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj : f'{obj.username}+senha')
    update_at = datetime.now()

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
    user = UserFactory(
        password=get_password_hash(pwd) ,
    )
    session.add(user)   
    session.commit()
    session.refresh(user)

    user.clean_password = pwd #monkey patch
    return user


@pytest.fixture
def other_user(session:Session):
    pwd = 'testtest'
    user = UserFactory(
        password=get_password_hash(pwd) ,
    )
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