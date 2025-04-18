from http import HTTPStatus
from pytest import mark
from fast_zero.schemas import UserPublic
from datetime import datetime


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
def test_update_users(client,user,token):
    update_at = str(datetime.now()) 
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.put(
        f"/users/{user.id}",
        headers={'Authorization':f'Bearer {token}'},
        json={
            "user": "doisberto",
            "email": "teste@test.com",
            "password": "123",
            "id":1,
            "update_at" : update_at,

        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema



def test_update_users_erro(client,user,token):
    update_at = str(datetime.now()) 
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.put(
        f"/users/{user.id+1}",
        headers={'Authorization':f'Bearer {token}'},
        json={
            "user": "doisberto",
            "email": "teste@test.com",
            "password": "123",
            "id":1,
            "update_at" : update_at,

        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail':"Not enough permission"}



@mark.delet
def test_delete_user(client,other_user,token):
    response = client.delete(
         f"/users/{other_user.id}",
        headers={'Authorization':f'Bearer {token}'}
        )
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() ==  {'message':'User deleted'}


def test_delete_wrong_user(client,other_user,token):
    response = client.delete(
        f"/users/{other_user.id}",
        headers={'Authorization':f'Bearer {token}'}
        )
    
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail':"Not enough permission"}


