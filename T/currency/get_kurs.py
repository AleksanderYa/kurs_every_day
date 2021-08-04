from typing import Dict, Any

import requests
import json


from pprint import pprint
from datetime import datetime



def fucken_datetime(month):
    month = str(month)
    if len(month) < 2:
        return '0' + month
    else:
        return str(month)


date = datetime.now()
site = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date.year}{fucken_datetime(date.month)}{date.day}&json' # 20210609
site2 = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date.day}.{fucken_datetime(date.month)}.{date.year}'   # 01.07.2021
# site2 = f'https://api.privatbank.ua/p24api/exchange_rates?date={date.day}.{fucken_datetime(date.month)}.{date.year}'

url = requests.get(site)
url2 = requests.get(site2)


htmltext = url.text
htmltext2 = url2.text
text = json.loads(htmltext)
text2 = json.loads(htmltext2)

def get_gov_currency(text=text):
    try:
        currency_base = {}
        for i in text:
            # {'r030': 840, 'txt': 'Долар США', 'rate': 26.8411, 'cc': 'USD', 'exchangedate': '04.08.2021'}
            # {'r030': 978, 'txt': 'Євро', 'rate': 31.8913, 'cc': 'EUR', 'exchangedate': '04.08.2021'}
            if i['cc'] == 'EUR':
                euro_base = {}
                euro_base['currency_name'] = i['cc']
                euro_base['sale'] = i['rate']
                euro_base['bay'] = None
                currency_base['EUR'] = euro_base
            elif i['cc'] == 'USD':
                usd_base = {}
                usd_base['currency_name'] = i['cc']
                usd_base['sale'] = i['rate']
                usd_base['bay'] = None
                currency_base['USD'] = usd_base

        return currency_base
    except Exception as e:
        print(e)

def get_privat_currency(text=text2):
    try:
        carrency_base = {}
        ex_text = text['exchangeRate']
        ex_text.pop(0)
        for i in ex_text:
            try:
                if i['currency'] == 'EUR':
                    euro_base = {}
                    euro_base['currency_name'] = i['currency']
                    euro_base['sale'] = i['saleRate']
                    euro_base['bay'] = i['purchaseRate']
                    carrency_base['EUR'] = euro_base
                elif i['currency'] == 'USD':
                    usd_base = {}
                    usd_base['currency_name'] = i['currency']
                    usd_base['sale'] = i['saleRate']
                    usd_base['bay'] = i['purchaseRate']
                    carrency_base['USD'] = usd_base
            except KeyError:
                print('KeyError')
        return carrency_base
    except Exception as e:
        print(e)



if __name__ == '__main__':
    a = get_gov_currency()
    c = get_privat_currency()

    print(a)
    # print(b)
    print(c)

