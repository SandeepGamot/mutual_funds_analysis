import json
import requests
import logging
import datetime

try:
    with open('config.json') as config:
        cfg = json.loads(config.read())
except FileNotFoundError:
    logging.exception("ERROR: File Not Found -'config.json'")


class ApiHandler:

    def test_api(self):
        response = requests.get(cfg["lmf"]["current_url"], headers=cfg["lmf"]["headers"])
        status_code = response.status_code

        if status_code != 200:
            print(status_code)

    def get_current_nav(self, scheme_code, full_details=False):
        if scheme_code is not None:
            querystring = {"SchemeType": "All", "SchemeCode": scheme_code}
            response = requests.get(cfg["lmf"]["current_url"], headers=cfg["lmf"]["headers"], params=querystring)
            data = json.loads(response.text)
            if full_details is True:
                return json.dumps(data,indent=4)
            else:
                return data[0]['Net Asset Value']
    def get_historical_nav(self, date, scheme_code=None, full_details=False):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Enter date in 'DD-MM-YYYY' format")
        if scheme_code is not None:
            querystring = {"SchemeType": "All", "SchemeCode": scheme_code, "Date": date}
        else:
            querystring = {"SchemeType": "All", "Date": date}

        response = requests.get(cfg["lmf"]["historical_url"], headers=cfg["lmf"]["headers"], params=querystring)
        data = json.loads(response.text)
        if full_details is True:
            return json.dumps(data, indent=4)
        else:
            return data[0]['Net Asset Value']
