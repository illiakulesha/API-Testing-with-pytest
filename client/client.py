import requests
from dotenv import load_dotenv
import os
BASE_URL = "https://reqres.in/api"
load_dotenv()
x_api_key = os.getenv('reqres_api_key')
class APIClient:
    
    def __init__(self, api_key, env):
        self.headers = {
            "x-api-key":api_key, 
            "X-Reqres-Env":env
        }

    def get(self, endpoint):
        return requests.get(BASE_URL + endpoint, headers=self.headers)

    def post(self, endpoint, payload, headers):
        return requests.post(BASE_URL + endpoint, json=payload, headers=headers)