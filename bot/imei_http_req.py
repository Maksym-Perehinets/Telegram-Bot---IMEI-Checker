import requests
from config import API_KEY
test = f'http://api-client.imei.org/api/services?apikey={API_KEY}'


class ImeiRequests:
    def test_request():
        result = requests.get(test).json()
        print(result)
        return result