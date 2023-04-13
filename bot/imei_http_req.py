import requests
from config import API_KEY
api_requests = f'http://api-client.imei.org/api/services?apikey={API_KEY}'

services = {}
prices = []


class ImeiRequests:

    def output(self, req):  # to tak nepracuie
        for item in req["response"]["services"]:
            prices.append(item)
        for item in prices:
            return item

    # Geting valid pricec and services id`s
    def geting_valid_price_information():
        response = requests.get(api_requests).json()
        for item in response['response']['services']:  # Loop wich converts api answer json file to
            services.update({item.get('name'): [item.get('id'), item.get('price')]})  #adding new item with valua of key==to name in json and array [a<--Id, b<--price]
        #print(services)<--Test print

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
        result = requests.get(api_requests).json()
        print(result)
        return result
