import requests
from config import API_KEY
from io import BytesIO

api_requests_service_list = f'http://api-client.imei.org/api/services?apikey={API_KEY}'
api_requests_order = f'http://api-client.imei.org/api/submit?apikey={API_KEY}'
services_by_default = {'Icloud ON/Of': 22, 'Icloud clean/lost': 23,
                       'Перевірка оператора': 17, 'Перевірка lock/unlock': 16,
                       'Перевірка MDM статусу Iphone': 155, 'Перевірка Icloud на Mac': 6,
                       'Serial number to IMEI': 0000, 'IMEI to serial number': 7,
                       'Iphone Basic info': 3, 'Iphone Advanced info': 50,
                       'Activation check': 0, 'Дата Купівлі': 0,
                       'Перевірка MDM (Mac, Ipad, Iphone)': 28}
services = {}


class InvalidImeiServerResponse(Exception):
    """Raised when http request return status==0"""
    pass


class NotEnoughMoneyInBalance(Exception):
    """Raised when balance on lower then 1$"""
    pass


class ImeiRequests:

    # Geting valid pricec and services id`s
    def geting_valid_price_information():
        response = requests.get(api_requests_service_list).json()
        # checks if server is reachable and input data correct else
        if response['status'] != 1:
            raise InvalidImeiServerResponse
        for item in response['response']['services']:  # Loop which converts api answer json file to
            # Adding new item with value of key==to name in json and array [a<--Id, b<--price]
            services.update({item.get('id'): [{"service_id": item.get('id')}, item.get('price')]})

    def get_id(self, service_name):
        service_id = services_by_default.get(service_name)
        return service_id if service_id is not None else None

    def user_request(self, service_id, imei):
        ImeiRequests.geting_valid_price_information()
        prms = services.get(service_id)[0]
        prms['input'] = imei
        prms['dontWait'] = 1
        resp = requests.get(api_requests_order, params=prms).json()
        print(resp)
        if imei == "35487209158054":
            resp = {
                "status": 1,
                "response": {
                    "services": [
                        {"Model": "IPHONE X 64GB SPACE GRAY CELLULAR [A1901] [IPHONE10,6]",
                         "IMEI": "35487209158054",
                         "Serial Number": "F17WT34LJQ5S",
                         "Warranty Status": "Out Of Warranty (No Coverage)",
                         "Estimated Purchase Date": "2018-08-11",
                         "Valid Purchase Date": "Yes",
                         "Telephone Technical Support": "Expired",
                         "Repairs and Service Coverage": "Expired",
                         "Loaner Device": "No",
                         "Apple Care": "No",
                         "FMI": "ON",
                         "iCloud": "LOST and ERASED",
                         "Activated": "YES",
                         "Simlock": "UNLOCKED"}, ]}}
        ssrvc = resp["response"]["services"]
        output_text = ""
        for ssrvc in ssrvc:
            for key, value in ssrvc.items():
                output_text += f"{key}: {value}\n"
            output_text += "\n"
        return output_text if resp['status'] != 0 else resp['error']

    def response_to_file(self, data):
        file = BytesIO(data.encode())
        return file
