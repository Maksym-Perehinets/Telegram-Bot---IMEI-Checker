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

    def output(self):    # Function that outputs data from http response
        pass

    # Geting valid pricec and services id`s
    def valid_price_and_balance_check(self):
        response = requests.get(api_requests).json()
        # checks if server is reachable and input data correct else
        if response['status'] != 1:
            raise InvalidImeiServerResponse
        for item in response['response']['services']:    # Loop which converts api answer json file to
            # Adding new item with value of key==to name in json and array [a<--Id, b<--price]
            services.update({item.get('name'): [item.get('id'), item.get('price')]})
        return services

    def test_request(self):
        # getting a json with prices and other data
        result = requests.get(api_requests).json()
        return result
