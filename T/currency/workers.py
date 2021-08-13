from abc import ABCMeta, abstractmethod
from currency.helpers import PrivatHelper, NbuHelper, MonoHelper
from datetime import datetime
import requests


class ChangeDate:
    def __init__(self):
        self.date = datetime.now()

    def correct_month(self):
        date_month= str(self.date.month)
        if len(date_month) < 2:
            self.month = '0' + date_month
            return self.month
        else:
            return date_month

    def date_to_privat(self):
        res = f'{self.date.day}.{self.correct_month()}.{self.date.year}'
        return res

    def date_to_nbu(self):
        res = f'{self.date.year}{self.correct_month()}{self.date.day}'
        return res

class BaseBankWorker:
    def privat_exchangeRate_list(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)['exchangeRate']
            except Exception:
                return func(*args, **kwargs)
        return inner

    def get(self):
        res = self.get_currency_json()
        res = self.helper.create_currency_obj(res)
        return res

    @privat_exchangeRate_list
    def get_currency_json(self):
        try:
            url = requests.get(self.SITE)
            url = url.json()
            return url
        except Exception as e:
            print(e)

class PrivatWorker(BaseBankWorker):
    def __init__(self):
        self.helper = PrivatHelper()
        self.date = ChangeDate()
        self.date = self.date.date_to_privat()
        self.SITE = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={self.date}'

class NbuWorker(BaseBankWorker):
    def __init__(self):
        self.date = ChangeDate()
        self.helper = NbuHelper()
        self.date = self.date.date_to_nbu()
        self.SITE = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=' \
           f'{self.date}&json'

class MonoWorker(BaseBankWorker):
    def __init__(self):
        self.helper = MonoHelper()
        self.SITE = 'https://api.monobank.ua/bank/currency'




if __name__ == '__main__':
    a = MonoWorker()
    a.get()
    print('------------------------------')
    b = PrivatWorker()
    b.get()
    print('------------------------------')
    c = NbuWorker()
    c.get()
#