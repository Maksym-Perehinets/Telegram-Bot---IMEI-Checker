import requests
from config import API_KEY
test = f'http://api-client.imei.org/api/services?apikey={API_KEY}'

services_id = 0

#test_array[3] = {API_KEY, services_id, imei} #хулі тестовий ерей словником опинився
prices = []


class ImeiRequests:

    def output(req): # to tak nepracuie
        for item in req["response"]["services"]:
            prices.append(item)
        for item in prices:
            print(item)

    def apple_advanced_check(imei):
        services_id = 50
        req = requests.get(f"http://api-client.imei.org/api/submit?apikey={API_KEY}&service_id={services_id}&input={imei}").json
        return

    def apple_basic_check(imei):
        services_id = 3
        return

    def apple_carrier_check(imei):
        services_id = 17
        return

    def apple_fms_check(imei):
        services_id = 2
        return

    def apple_mdm_check(imei):
        services_id = 28
        return

    def apple_mdmpro_check(imei):
        services_id = 155
        return

    def apple_warranty_status_check(imei):
        services_id = 4
        return

    def apple_simlock_check(imei):
        services_id = 16
        return

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
