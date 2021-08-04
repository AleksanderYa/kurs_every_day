import requests
import json
from datetime import datetime


class GetKurs():
    date = datetime.now()
    def fucken_datetime(self):
        month = str(self.date.month)
        if len(month) < 2:
            self.month = '0' + month
            return self.month
        else:
            return self.month

    def get_privat(self):
        site = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={self.date.day}.{self.fucken_datetime()}.{self.date.year}'  # 01.07.2021
        url = requests.get(site)
        return url

    def get_nbu(self):
        site = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={self.date.year}{self.fucken_datetime()}{self.date.day}&json'  # 20210609
        url = requests.get(site)
        return url

    def get_privat_json(self):
        url = self.get_privat()
        htmltext = url.text
        self.privat_json = json.loads(htmltext)
        return self.privat_json

    def get_nbu_json(self):
        url = self.get_nbu()
        htmltext = url.text
        self.nbu_json = json.loads(htmltext)
        return self.nbu_json

    def get_nbu_currency(self):
        try:
            currency_base = {}
            for i in self.get_nbu_json():
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

    def get_privat_currency(self):
        try:
            carrency_base = {}
            ex_text = self.get_privat_json()
            ex_text = ex_text['exchangeRate']
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
    a = GetKurs()
    print(a.get_nbu_currency())
    print(a.get_privat_currency())

