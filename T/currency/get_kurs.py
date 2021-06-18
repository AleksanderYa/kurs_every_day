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
# site = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
url = requests.get(site)
htmltext = url.text
text = json.loads(htmltext)

def get_price(text=text, currency_name='USD'):
    for i in text:
        if currency_name == 'USD' and i['cc'] == 'USD':
            print(i['txt'], i['rate'])
            return i['rate']
        elif currency_name == 'EUR' and i['cc'] == 'EUR':
            print(i['txt'], i['rate'])
            return i['rate']
        else:
            print('Not have current name in list')
            return None

