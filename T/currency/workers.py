import requests
from datetime import datetime

from currency.parametrs import PRIBAT_BANK_URL
from currency.parametrs import NBU_BANK_URL
from currency.parametrs import MONO_BANK_URL
from currency.helpers import PrivatHelper
from currency.helpers import NbuHelper
from currency.helpers import MonoHelper


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
            pass
            print(e)

class PrivatWorker(BaseBankWorker):
    def __init__(self):
        self.helper = PrivatHelper()
        self.date = ChangeDate()
        self.date = self.date.date_to_privat()
        self.SITE = PRIBAT_BANK_URL + self.date


class NbuWorker(BaseBankWorker):
    def __init__(self):
        self.date = ChangeDate()
        self.helper = NbuHelper()
        self.date = self.date.date_to_nbu()
        self.SITE = NBU_BANK_URL + self.date + '&json'

class MonoWorker(BaseBankWorker):
    def __init__(self):
        self.helper = MonoHelper()
        self.SITE = MONO_BANK_URL




if __name__ == '__main__':
    a = MonoWorker()
    aa = a.get()
    print(f'USD {aa.usd_sale}/{aa.usd_buy}\nEURO {aa.euro_sale}/{aa.euro_buy}')

    print('------------------------------')
    b = PrivatWorker()
    bb = b.get()
    print(f'USD {bb.usd_sale}/{bb.usd_buy}\nEURO {bb.euro_sale}/{bb.euro_buy}')

    print('------------------------------')
    c = NbuWorker()
    cc = c.get()
    print(f'USD {cc.usd_sale}/{cc.usd_buy}\nEURO {cc.euro_sale}/{cc.euro_buy}')

#