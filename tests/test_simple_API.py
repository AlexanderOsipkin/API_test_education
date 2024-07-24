import json

import requests
from jsonschema import validate


def test_json_schema_in_response():
    response = requests.post('https://reqres.in/api/users', data={'name': 'morpheus', 'job': 'leader'})
    body = response.json()

    assert response.status_code == 201
    with open('tests/post_users.json') as file:
        validate(body, schema=json.loads(file.read()))


def test_job_name_from_request_returns_in_response():
    job = "leader"
    name = "morpheus"

    response = requests.post('https://reqres.in/api/users', data={'name': name, 'job': job})
    body = response.json()

    assert body['name'] == name
    assert body['job'] == job
