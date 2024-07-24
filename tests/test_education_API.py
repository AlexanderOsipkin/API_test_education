import json

import requests
from jsonschema import validate


def test_create_user():
    request_body_data = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
    response = requests.post('https://petstore.swagger.io/v2/user', json=request_body_data)
    body = response.json()

    assert response.status_code == 200
    with open('education_schema.json') as file:
        validate(body, schema=json.loads(file.read()))
