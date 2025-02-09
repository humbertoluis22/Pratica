from http import HTTPStatus
from fast_zero.settings import Settings
from pytest import mark
from fast_zero.schemas import UserPublic,Message
from datetime import datetime

@mark.primeiro_teste
def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get("/")  # ação

    assert response.status_code == HTTPStatus.OK  # assrrt (garanta)
    assert response.json() == {"message": "Hello world"}


@mark.creat
def test_create_user(client):
    update_at = str(datetime.now())
    response = client.post(
        "/users/",
        json={
            "user": "humberto",
            "email": "humberto@hotmail.com",
            "password": "hipytest",
            "update_at" : update_at,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "humberto",
        "email": "humberto@hotmail.com",
        "id": 1,
    }


@mark.creat
@mark.xfail
def test_create_user_erro_email(client,user):
    update_at = str(datetime.now())
    response = client.post(
        "/users/",
        json={
            "user": "humberto",
            "email": "teste@test.com",
            "password": "hipytest",
            "update_at" : update_at,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "humberto",
        "email": "teste@test.com",
        "id": 2,
    }


@mark.creat
@mark.xfail
def test_create_user_erro_user(client,user):
    update_at = str(datetime.now())
    response = client.post(
        "/users/",
        json={
            "user": "Teste",
            "email": "humberto@test.com",
            "password": "hipytest",
            "update_at" : update_at,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "Teste",
        "email": "humberto@hotmail.com",
        "id": 2,
    }


@mark.user
def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": []
    }

@mark.user
def test_read_users_with_user(client,user):
    response = client.get("/users/")
    user_schema = UserPublic.model_validate(user).model_dump()
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users":  [user_schema]
    }

@mark.read
def test_read_users_id(client,user):
    response = client.get("/users/1")
    user_schema = UserPublic.model_validate(user).model_dump()

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema



@mark.xfail
def test_read_users_id_error(client,user):
    response = client.get("/users/2")
    user_schema = UserPublic.model_validate(user).model_dump()

    assert response.json() == user_schema


@mark.update
def test_update_users(client,user):
    update_at = str(datetime.now()) 
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.put(
        "/users/1",
        json={
            "user": "doisberto",
            "email": "teste@test.com",
            "password": "123",
            "update_at" : update_at,

        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


@mark.teste_erro
@mark.xfail
def test_update_users_erro(client,user):
    update_at = str(datetime.now())
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.put(
        "/users/2",
        json={
            "user": "doisberto",
            "email": "teste@test.com",
            "password": "123",
            "update_at" : update_at,

        },
    )

    assert response.json() == user_schema


@mark.delet
def test_delete_user(client,user):
    response = client.delete("/users/1")
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() ==  {'message':'User deleted'}


@mark.xfail
def test_delete_user_error(client,user):
    response = client.delete("/users/2")
    assert response.json() == {'message':'User deleted'}
