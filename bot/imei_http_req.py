import requests
from config import API_KEY
test = f'http://api-client.imei.org/api/services?apikey={API_KEY}'


prices = []


class ImeiRequests:

    def get_price():
        # getting a json with prices and other data
        req = requests.get(test).json()
        # creating a list with item id`s name and prices
        for item in req["response"]["services"]:
            prices.append(item)
        for item in prices:
            print(item)

    def test_request():
        # getting a json with prices and other data
        result = requests.get(test).json()
        print(result)
        return result


ImeiRequests.get_price()