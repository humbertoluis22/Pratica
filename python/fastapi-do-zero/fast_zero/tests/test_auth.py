from http import HTTPStatus


def test_get_token(client,user):
    response  = client.post(
        '/auth/token',
        data = {
            'username':user.email,
            'password':user.clean_password
            }
    )
    token = response.json()

    assert response.status_code == 200
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token 


def test_get_token_not_user(client,user):
    response  = client.post(
        '/auth/token',
        data = {
            'username':'',
            'password':user.clean_password
            }
    )
    token = response.json()

    assert response.status_code == 400
    assert response.json() == {'detail':"Incorrect email or password"}
     

