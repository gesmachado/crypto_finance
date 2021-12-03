import requests
import json
import api_interaction
import valuation_crypto

key = 'COLOCAR UMA KEY'


def main(update_json):
    if update_json:
        api_interaction.get_coinmarketcap_api(key)

    elif not update_json:
        print('Não será atualizado o JSON de Cryptos')
        api_interaction.last_update_day_r()

    valuation_crypto.bitcoin_reference()
    valuation_crypto.open_json_file()


if __name__ == '__main__':
    main(False)
