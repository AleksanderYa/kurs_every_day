from abc import ABC

from currency.parametrs import CURRENCY_CODE_EUR
from currency.parametrs import CURRENCY_CODE_USD
from currency.parametrs import CURRENCY_CODE_SOMESHIT
from currency.parametrs import USD
from currency.parametrs import EUR


class BaseHelper(ABC):
#####
    def __init__(self):
        self.create_obj = CreateObj()

    def if_el(self, obj):
        raise NotImplementedError

    def create_currency_obj(self, obj):
        obj = obj
        try:
            for i in obj:
                try:
                    self.if_el(i)
                except Exception as e:
                    print(e)
        finally:
            return self.create_obj

class CreateObj:
#####
    def __init__(self):
        self.usd_sale = float()
        self.usd_buy = float()
        self.euro_sale = float()
        self.euro_buy = float()

class PrivatHelper(BaseHelper):
#####
    def if_el(self, i):
        if i['currency'] == USD:
            self.create_obj.usd_buy = float(i['saleRate'])
            self.create_obj.usd_sale = float(i['purchaseRate'])
        elif i['currency'] == EUR:
            self.create_obj.euro_buy = float(i['saleRate'])
            self.create_obj.euro_sale = float(i['purchaseRate'])

class MonoHelper(BaseHelper):
#####
    def if_el(self, i):
        try:
            if i['currencyCodeA'] == CURRENCY_CODE_USD and i['currencyCodeB'] == CURRENCY_CODE_SOMESHIT:
                self.create_obj.usd_buy = float(i['rateSell'])
                self.create_obj.usd_sale = float(i['rateBuy'])
            elif i['currencyCodeA'] == CURRENCY_CODE_EUR and i['currencyCodeB'] == CURRENCY_CODE_SOMESHIT:
                self.create_obj.euro_buy = float(i['rateSell'])
                self.create_obj.euro_sale = float(i['rateBuy'])
        except Exception as e:
            print(e)

class NbuHelper(BaseHelper):
#####
    def if_el(self, i):
        if i['cc'] == USD:
            self.create_obj.usd_sale = i['rate']
        elif i['cc'] == EUR:
            self.create_obj.euro_sale = i['rate']





