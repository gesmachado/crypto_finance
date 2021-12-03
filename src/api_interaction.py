from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import project_path
from datetime import datetime

key = 'UTILIZAR UM KEY'


def get_coinmarketcap_api(key):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '3000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    with open(project_path.get_path_file(), 'w') as json_file:
        json.dump(response.json(), json_file)

    last_update_day_w()


def last_update_day_w():
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = str(dt_string)
    dt_string = 'Last update: ' + dt_string
    print(dt_string)

    with open(project_path.get_root_path() + '/files/last_update.txt', 'w') as f:
        f.write(dt_string)

    f.close()


def last_update_day_r():
    with open(project_path.get_root_path() + '/files/last_update.txt') as f:
        lines = f.readlines()
        for i in lines:
            print(i)
    f.close()


if __name__ == '__main__':
    # get_coinmarketcap_api(key)
    # last_update_day_w()
    # last_update_day_r()
    pass
