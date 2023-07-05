import requests
from credentials.config import api_requests_service_list, api_requests_order
from io import BytesIO


services_by_default = {'Icloud ON/Of': 22, 'Icloud clean/lost': 23,
                       'Перевірка оператора': 17, 'Перевірка lock/unlock': 16,
                       'Перевірка MDM статусу Iphone': 155, 'Перевірка Icloud на Mac': 6,
                       'Serial number to IMEI': 0000, 'IMEI to serial number': 7,
                       'Iphone Basic info': 3, 'Iphone Advanced info': 50,
                       'Activation check': 0, 'Дата Купівлі': 0,
                       'Перевірка MDM (Mac, Ipad, Iphone)': 28,
                       'Мій аккаунт': 78564}
services = {}


class InvalidImeiServerResponse(Exception):
    """Raised when http request return status==0"""
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
        ImeiRequests.geting_valid_price_information()  # Getting valid information about prices

        prms = services.get(service_id)[0]  # Preparing input parameters id
        prms['input'] = imei  # Preparing input parameters imei
        print(prms)

        resp = requests.get(api_requests_order, params=prms).json()  # Getting server response
        print(resp)

        if resp["status"] != -1:
            answ = resp["response"]
            output_text = ""
            for key, value in answ.items():
                output_text += f"{key}: {value}\n"
            output_text += "\n"
            return output_text
        else:
            return resp["error"]

    def response_to_file(self, data):
        return BytesIO(data.encode()) if len(data.split()) > 1 else data
