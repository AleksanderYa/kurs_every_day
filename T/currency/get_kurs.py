import requests
import json

from datetime import datetime


def fucken_datetime(month):
    month = str(month)
    if len(month) < 2:
        return '0' + month 
    else:
        return str(month)


def text_privat():
    date = datetime.now()
    site = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date.day}.{fucken_datetime(date.month)}.{date.year}'   # 01.07.2021
    url = requests.get(site)
    htmltext = url.text
    text = json.loads(htmltext)
    return text



def text_nbu():
    date = datetime.now()
    site = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date.year}{fucken_datetime(date.month)}{date.day}&json'  # 20210609
    url = requests.get(site)
    htmltext = url.text
    text = json.loads(htmltext)
    return text


def get_nbu_currency():
    try:
        text = text_nbu()
        currency_base = {}
        for i in text:
            if i['cc'] == 'USD':
                print(i['txt'], i['rate'])
                currency_base['name_usd_true'] = i['cc']
                currency_base['nbu_price_usd_true'] = i['rate']
            elif i['cc'] == 'EUR':
                print(i['txt'], i['rate'])
                currency_base['name_eur_true'] = i['cc']
                currency_base['nbu_price_eur_true'] = i['rate']
        return currency_base
    except Exception as e:
        print(e)
        return None

def get_privat_currency():
    try:
        text = text_privat()
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
    get_nbu_currency()

    get_privat_currency()