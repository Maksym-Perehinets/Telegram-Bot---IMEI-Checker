import requests
from config import API_KEY
api_requests = f'http://api-client.imei.org/api/services?apikey={API_KEY}'

services = {}
prices = []


class InvalidImeiServerResponse(Exception):
    """Raised when http request return status==0"""
    pass


class NotEnoughMoneyInBalance(Exception):
    """Raised when balance on lower then 1$"""
    pass


class ImeiRequests:

    def output(self):  # to tak nepracuie
        return self['id']

    # Geting valid pricec and services id`s
    def geting_valid_price_information():
        response = requests.get(api_requests).json()
        # checks if server is reachable and input data correct else
        if response['status'] != 1:
            raise InvalidImeiServerResponse
        for item in response['response']['services']:  # Loop which converts api answer json file to
            # Adding new item with valua of key==to name in json and array [a<--Id, b<--price]
            services.update({item.get('name'): [item.get('id'), item.get('price')]})
        return services
        # print(services)<--Test print

    def test_request():
        # getting a json with prices and other data
        result = requests.get(api_requests).json()
        print(result)
        return result
