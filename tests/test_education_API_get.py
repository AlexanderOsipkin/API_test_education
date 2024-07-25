import requests


def test_get_pet_by_status():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'
    status = {"status": "available"}
    result = requests.get(
        url,
        status
    )
    assert result.status_code == 200

