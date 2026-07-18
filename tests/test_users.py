from client.client import APIClient
from dotenv import load_dotenv
import os

load_dotenv()
reqres_api_key = os.getenv('reqres_api_key')
x_api_key=f"{reqres_api_key}"
client = APIClient(x_api_key, "prod")
#headers= {"x-api-key": x_api_key, "X-Reqres-Env":"prod"}
def test_get_users():
    response = client.get("/collections/products/records?project_id=17222")
    assert response.status_code == 200

    body = response.json()

    assert "data" in body

