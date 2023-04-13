import requests
from config import API_KEY
api_requests = f'http://api-client.imei.org/api/services?apikey={API_KEY}'

services = {}
prices = []


class ImeiRequests:

    def output(req):  # to tak nepracuie
        for item in req["response"]["services"]:
            prices.append(item)
        for item in prices:
            return item


    #Geting
    def geting_valid_price_information():
        response = requests.get(api_requests).json()
        for item in response['response']['services']:
            services





    # def get_price():
    #    # getting a json with prices and other data
    #     req = requests.get(test).json()
    #     # creating a list with item id`s name and prices
    #     for item in req["response"]["services"]:
    #         prices.append(item)
    #     for item in prices:
    #         print(item)

    def test_request():
        # getting a json with prices and other data
        result = requests.get(test).json()
        print(result)
        return result

ImeiRequests.geting_valid_price_information()