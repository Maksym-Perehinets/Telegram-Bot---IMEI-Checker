import requests
from config import API_KEY
api_requests = f'http://api-client.imei.org/api/services?apikey={API_KEY}'

services = {}
prices = []


class InvalidImeiServerResponse(Exception):    # Server response error exception
    """Raised when http request return status==0 or not enough money in balance"""
    pass


class ImeiRequests:

    def output(self):    # Function that outputs data from http response
        return self

    # Getting valid prices and services id`s
    def valid_price_and_balance_check():
        response = requests.get(api_requests).json()
        balance_check = requests.get(f'https://api-client.imei.org/api/balance?apikey={API_KEY}').json()
        # checks if server is reachable and input data correct else
        if response['status'] != 1 or balance_check['response']['credits'] > 1:
            raise InvalidImeiServerResponse
        for item in response['response']['services']:    # Loop which converts api answer json file to
            # Adding new item with value of key==to name in json and array [a<--Id, b<--price]
            services.update({item.get('name'): [item.get('id'), item.get('price')]})
        return ImeiRequests.output(services)

    def test_request(self):
        # getting a json with prices and other data
        result = requests.get(api_requests).json()
        return result
