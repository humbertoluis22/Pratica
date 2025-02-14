from http import HTTPStatus
from pytest import mark

@mark.primeiro_teste
def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get("/")  # ação

    assert response.status_code == HTTPStatus.OK  # assrrt (garanta)
    assert response.json() == {"message": "Hello world"}

