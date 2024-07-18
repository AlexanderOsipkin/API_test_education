import json

import requests
from jsonschema import validate


def test():
    response = requests.post('https://reqres.in/api/users', data={'name':'morpheus', 'job':'leader'})
    body = response.json()
    assert response.status_code == 201
    with open('post_users.json') as file:
        validate(body, schema=json.loads(file.read()))
