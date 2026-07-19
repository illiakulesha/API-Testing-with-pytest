from client.client import APIClient
import pytest
import os
from dotenv import load_dotenv
load_dotenv()
api = os.getenv("reqres_api_key")
@pytest.fixture
def client_with_api():
    client = APIClient(api, "prod")
    return client
@pytest.mark.parametrize("id,expected", ([99999999,404],[0,404],["abc",404]))
def test_get_products(client_with_api, id, expected):
    url = f"/collections/products/records/id={id}"
    response = client_with_api.get(url)
    body = response.json()
    print(url)
    assert response.status_code == expected
