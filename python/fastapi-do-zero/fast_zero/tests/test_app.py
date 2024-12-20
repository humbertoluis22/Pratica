from http  import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) # organizacao
    response = client.get('/') # ação

    assert response.status_code ==  HTTPStatus.OK  #assrrt (garanta)
    assert response.json() == {"message": "Hello world"}
