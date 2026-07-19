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
def test_get_products(client_with_api):
    response = client_with_api.get("/collections/products/records?project_id=17222")
    assert response.status_code == 200

    body = response.json()
    print(body)
    assert "data" in body