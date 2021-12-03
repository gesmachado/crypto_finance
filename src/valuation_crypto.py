import json
import project_path


def bitcoin_reference():
    # Opening JSON file
    f = open(project_path.get_path_file())

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()

    with open(project_path.get_root_path() + '/files/btc_refe.csv', 'w') as w:
        w.write('Name;Symbol;Coin Market Cap;Price;Volume;max_supply;total_supply\n')

        for i in data['data']:
            if i['name'] == 'Bitcoin':
                btc_coin_name = i['name']
                btc_symbol = i['symbol']
                btc_coin_mkt_cap = str(i['quote']['USD']['market_cap'])
                btc_coin_price = str(i['quote']['USD']['price'])
                btc_coin_volume = str(i['quote']['USD']['volume_24h'])
                btc_coin_max_supply = str(i['max_supply'])
                btc_coin_total_supply = str(i['total_supply'])

                btc_coin_mkt_cap = btc_coin_mkt_cap.replace(".", ",")
                btc_coin_price = btc_coin_price.replace(".", ",")
                btc_coin_max_supply = btc_coin_max_supply.replace(".", ",")
                btc_coin_total_supply = btc_coin_total_supply.replace(".", ",")

                if btc_coin_mkt_cap != '0':
                    coin = f'{btc_coin_name}; {btc_symbol}; {btc_coin_mkt_cap}; {btc_coin_price};{btc_coin_volume};{btc_coin_max_supply};{btc_coin_total_supply}\n'

                    w.write(coin)

                print(coin)

        w.close()
        # Closing file


def open_json_file():
    # Opening JSON file
    f = open(project_path.get_path_file())

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()

    with open(project_path.get_root_path() + '/files/coin_info.csv', 'w') as w:
        w.write('Name;Symbol;Coin Market Cap;Price;Volume;max_supply;total_supply\n')

        for i in data['data']:
            coin_name = i['name']
            coin_symbol = i['symbol']
            coin_mkt_cap = str(i['quote']['USD']['market_cap'])
            coin_price = str(i['quote']['USD']['price'])
            coin_volume = str(i['quote']['USD']['volume_24h'])
            coin_max_supply = str(i['max_supply'])
            coin_total_supply = str(i['total_supply'])

            coin_mkt_cap = coin_mkt_cap.replace(".", ",")
            coin_price = coin_price.replace(".", ",")
            coin_max_supply = coin_max_supply.replace(".", ",")
            coin_total_supply = coin_total_supply.replace(".", ",")

            if coin_mkt_cap != '0':
                if coin_max_supply == '0':
                    coin_max_supply = None

                coin = f'{coin_name}; {coin_symbol}; {coin_mkt_cap}; {coin_price};{coin_volume};{coin_max_supply};{coin_total_supply}\n'

                print('SAVING Coin on CSV -> ' + coin_symbol)
                w.write(coin)
                # print(coin_symbol)

    w.close()
    # Closing file
