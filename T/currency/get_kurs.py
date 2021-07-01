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
print()
def get_gov_usd(text):
    try:
        for i in text:
            if i['cc'] == 'USD':
                print(i['txt'], i['rate'])
                return [i['txt'], i['rate']]
    except Exception as e:
        print(e)
        return None


def get_nbu_currency(text):
    try:
        currency_base = {}
        for i in text:
            if i['cc'] == 'USD':
                print(i['txt'], i['rate'])
                currency_base['currency_name'] = i['cc']

            elif i['cc'] == 'EUR':
                print(i['txt'], i['rate'])

    except Exception as e:
        print(e)
        return None

def get_gov_eur(text):
    try:
        for i in text:
            if i['cc'] == 'EUR':
                print(i['txt'], i['rate'])
                return [i['txt'], i['rate']]
    except Exception as e:
        print(e)
        return None

# def try_exept():


def get_privat_currency(text):
    try:
        currency_base = {}
        ex_text = text['exchangeRate']
        ex_text.pop(0)
        for i in ex_text:
            try:
                if i['currency'] == 'USD':
                    currency_base['currency_name_usd'] = i['currency']
                    currency_base['nbu_price_usd'] = i['saleRateNB']
                    currency_base['privat_price_usd_sale'] = i['saleRate']
                    currency_base['privat_price_usd_bay'] = i['purchaseRate']
                    print(
                        f"Курс {currency_base['currency_name_usd']} на {date.day}.{fucken_datetime(date.month)}:" \
                        f"\nНБУ - {currency_base['nbu_price_usd']} грн\nPrivatBank покупка - {currency_base['privat_price_usd_sale']}грн\nPrivatBank продажа - {currency_base['privat_price_usd_bay']}грн\n"
                    )
                elif i['currency'] == 'EUR':
                    currency_base['currency_name_eur'] = i['currency']
                    currency_base['nbu_price_eur'] = i['saleRateNB']
                    currency_base['privat_price_eur_sale'] = i['saleRate']
                    currency_base['privat_price_eur_bay'] = i['purchaseRate']
                    print(
                        f"\nКурс {currency_base['currency_name_eur']} на {date.day}.{fucken_datetime(date.month)}:" \
                        f"\nНБУ - {currency_base['nbu_price_eur']} грн\nPrivatBank покупка - {currency_base['privat_price_eur_sale']}грн\nPrivatBank продажа - {currency_base['privat_price_eur_bay']}грн\n"
                    )
            except KeyError:
                print('KeyError')
        return currency_base
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    get_gov_usd(text=text)
    get_gov_eur(text=text)

    get_privat_currency(text=text2)