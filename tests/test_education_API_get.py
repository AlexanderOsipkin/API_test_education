import requests


def test_get_pet_by_status():
    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus',
                            data={"status": "available"})

    assert response.status_code == 200

