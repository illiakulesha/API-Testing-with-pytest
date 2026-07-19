from client.client import APIClient
import pytest
@pytest.mark.parametrize(
    "client,env,expected", 
    [
        (None, "prod",401),
        ("1234", "prod",403),
        ("", "prod",401)
    ],
)
def test_get_users(client,env,expected):
    client = APIClient(client,env)
    response = client.get("/collections/products/records?project_id=17222")
    assert response.status_code == expected