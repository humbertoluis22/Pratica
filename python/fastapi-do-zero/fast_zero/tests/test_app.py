from http import HTTPStatus
from pytest import mark
from fast_zero.schemas import UserPublic

@mark.primeiro_teste
def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get("/")  # ação

    assert response.status_code == HTTPStatus.OK  # assrrt (garanta)
    assert response.json() == {"message": "Hello world"}


@mark.segundo_teste
def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "user": "humberto",
            "email": "humberto@hotmail.com",
            "password": "hipytest",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "user": "humberto",
        "email": "humberto@hotmail.com",
        "id": 1,
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

def test_read_users_id(client):
    response = client.get("/users/1")
    assert response.json() == {
        "user": "humberto",
        "email": "humberto@hotmail.com",
        "id": 1,
    }


@mark.xfail
def test_read_users_id_error(client):
    response = client.get("/users/3")
    assert response.json() == {
        "user": "humberto",
        "email": "humberto@hotmail.com",
        "id": 1,
    }


def test_update_users(client):
    response = client.put(
        "/users/1",
        json={
            "user": "doisberto",
            "email": "Doishumberto@hotmail.com",
            "password": "123",
        },
    )

    assert response.json() == {
        "user": "doisberto",
        "email": "Doishumberto@hotmail.com",
        "id": 1,
    }


@mark.teste_erro
@mark.xfail
def test_update_users_erro(client):
    response = client.put(
        "/users/2",
        json={
            "user": "doisberto",
            "email": "Doishumberto@hotmail.com",
            "password": "123",
        },
    )

    assert response.json() == {
        "user": "doisberto",
        "email": "Doishumberto@hotmail.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.json() == {"message": "User deletado"}


@mark.xfail
def test_delete_user_error(client):
    response = client.delete("/users/2")
    assert response.json() == {"message": "User deletado"}
