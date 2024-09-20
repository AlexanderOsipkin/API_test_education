import requests


def test_delete_user():
    response = requests.delete('https://petstore.swagger.io/v2/user/testuser15790033')

    assert response.status_code == 200