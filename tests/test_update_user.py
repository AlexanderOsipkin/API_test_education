import json

import requests
from jsonschema import validate


def test_update_user():
    username = "testuser157900"
    request_body_data = {
        "id": 157893627,
        "username": "testuser157900",
        "firstName": "Ivan12",
        "lastName": "Ivanov",
        "email": "test@testmail.com",
        "password": "test1579",
        "phone": "+79999999999",
        "userStatus": 0
    }

    response = requests.put(f'https://petstore.swagger.io/v2/user/{username}', json=request_body_data)
    body = response.json()

    assert response.status_code == 200
    with open('education_schema.json') as file:
        validate(body, schema=json.loads(file.read()))