import requests
from constants import API_URL
from logger_config import api_logger


class makeRequest:
    url = API_URL
    headers = {
        'Content-Type': 'application/json'
    }

    def get(self):
        try:
            api_logger.info(f"GET request to {self.url} returned status code")
            return requests.get(url=self.url, headers=self.headers).content
        except Exception as err:
            return err

    def post(self, body):
        return requests.post(self.url)
