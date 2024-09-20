import requests


def test_delete_user():
    username = "testuser15790033"
    response = requests.delete(f'https://petstore.swagger.io/v2/user/{username}')

    assert response.status_code == 200