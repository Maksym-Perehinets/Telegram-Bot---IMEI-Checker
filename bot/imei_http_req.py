import requests
from credentials.config import api_requests_service_list, api_requests_order
from io import BytesIO
from sheets_api import SheetApi

services_by_default = {'Icloud ON/Of': 22, 'Icloud clean/lost': 23,
                       'Перевірка оператора': 17, 'Перевірка lock/unlock': 16,
                       'Перевірка MDM статусу Iphone': 155, 'Перевірка Icloud на Mac': 6,
                       'Serial number to IMEI': 0000, 'IMEI to serial number': 7,
                       'Iphone Basic info': 3, 'Iphone Advanced info': 50,
                       'Activation check': 0, 'Дата Купівлі': 0,
                       'Перевірка MDM (Mac, Ipad, Iphone)': 28,
                       'Мій аккаунт': 78564}
services = {}

sh_api = SheetApi()


class InvalidImeiServerResponse(Exception):
    """Raised when http request return status==0"""
    pass


class ImeiRequests:

    def geting_valid_price_information(self):
        response = requests.get(api_requests_service_list).json()
        # checks if server is reachable and input data correct else
        if response['status'] != 1:
            raise InvalidImeiServerResponse
        for item in response['response']['services']:  # Loop which converts api answer json file to
            # Adding new item with value of key==to name in json and array [a<--Id, b<--price]
            services.update({item.get('id'): [{"service_id": item.get('id')}, item.get('price')]})

    # Chek balamce
    def chek_balance(self):
        result = requests.get(
            "http://api-client.imei.org/api/balance?apikey=OjjlfRQBVoMdJMs9bO8QUGM6YKkWuVKIi91WdssIEhHCMQF8aMeM0g0VtaNa"
        ).json()
        return 0 if result['response']['credits'] < 0.10 else 1

    # Geting valid pricec and services id`s
    def price_inf(self, service_id):
        price = requests.get(api_requests_service_list).json()

        for i in price['response']['services']:
            if service_id == i['id']:
                return i['price']

    def get_id(self, service_name):
        service_id = services_by_default.get(service_name)
        return service_id if service_id is not None else None

    def user_request(self, service_id, imei, user_id):
        self.geting_valid_price_information()

        if self.chek_balance() == 1 and float(sh_api.get_balance(user_id)) >= self.price_inf(service_id):

            prms = services.get(service_id)[0]  # Preparing input parameters id
            prms['input'] = imei  # Preparing input parameters imei
            resp = requests.get(api_requests_order, params=prms).json()  # Getting server response

            if resp["status"] == 1:
                answ = resp["response"]
                output_text = ""
                for key, value in answ.items():
                    output_text += f"{key}: {value}\n"
                output_text += "\n"
                sh_api.chek_out(user_id, self.price_inf(service_id))
                return output_text

            else:
                print('error occurred')
                return "error contact @Maksym_Per"

        else:
            return 'Not enough money' if sh_api.get_balance(user_id) < self.price_inf(
                service_id) else 'Contact @Maksym_Per'

    def response_to_file(self, data):
        return BytesIO(data.encode()) if len(data.split()) > 1 else data
