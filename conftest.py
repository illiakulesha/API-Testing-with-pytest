import pytest
from client.client import APIClient
import os
from dotenv import load_dotenv
load_dotenv()
api = os.getenv("reqres_api_key")
@pytest.fixture
def client_with_api():
    client = APIClient(api, "prod")
    return client
@pytest.mark.parametrize("endpoint,expected", [("/collections/products/records?project_id=17222", 200)])
def test_get_collection(client_with_api, endpoint, expected):
    response = client_with_api.get(endpoint)
    assert response.status_code == expected
