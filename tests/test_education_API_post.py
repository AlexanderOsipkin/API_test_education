import json

import requests
from jsonschema import validate


def test_create_user():
    request_body_data = {
        "id": 157893627,
        "username": "testuser157",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "test@testmail.com",
        "password": "test157",
        "phone": "+79273774254",
        "userStatus": 0
    }
    response = requests.post('https://petstore.swagger.io/v2/user', json=request_body_data)
    body = response.json()

    assert response.status_code == 200
    with open('tests/education_schema.json') as file:
        validate(body, schema=json.loads(file.read()))
