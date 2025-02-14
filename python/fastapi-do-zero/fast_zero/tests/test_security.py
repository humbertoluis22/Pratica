from jwt import decode
from http import HTTPStatus
from pytest import mark
from fast_zero.security import settings,create_access_token

def test_jwt():
    data = ({'teste':'teste'})
    token = create_access_token(data)
    result = decode(token,settings.SECRET_KEY,algorithms=settings.ALGORITHM)

    assert  result['teste'] == data['teste']
    assert  result['exp']


def test_jwt_invalid_token(client):
    reponse = client.delete(
        'users/1',headers={'Authorization':'Bearer token-invalido'}
    )

    assert reponse.status_code == HTTPStatus.UNAUTHORIZED
    assert reponse.json() == {'detail':'Could not validate credentials'}



def test_get_current_user_does_empty(client,user):
    data = {'sub': ''}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}



def test_get_current_user_does_not_exists(client):
    data = {'sub': 'test@test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
