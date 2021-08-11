from abc import ABCMeta, abstractmethod
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

class BaseBankWorker(metaclass=ABCMeta): # Not need to use metaclass
    def privat_exchangeRate_list(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)['exchangeRate']
            except TypeError:
                return func(*args, **kwargs)
        return inner

    @privat_exchangeRate_list
    def get_currency_json(self):
        try:
            url = requests.get(self.SITE)
            url = url.json()
            return url
        except Exception as e:
            print(e)

class PrivatWorker(BaseBankWorker):
    date = ChangeDate()
    date = date.date_to_privat()
    SITE = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'


class NbuWorkers(BaseBankWorker):
    date = ChangeDate()
    date = date.date_to_nbu()
    SITE = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=' \
           f'{date}&json'


class MonoWorker(BaseBankWorker):
    SITE = 'https://api.monobank.ua/bank/currency'




if __name__ == '__main__':
    a = MonoWorker()
    aa = a.get_currency_json()
    print(type(aa))
    print(aa)

    b = PrivatWorker()
    bb = b.get_currency_json()
    print(type(bb))
    print(bb)

    c = NbuWorkers()
    cc = c.get_currency_json()
    print(type(cc))
    print(cc)

