from abc import ABC, abstractmethod

class BaseHelper(ABC):
#####
    def __init__(self):
        self.create_obj = CreateObj()

    @abstractmethod
    def create_currency_obj(self, obj):
        raise NotImplementedError

class CreateObj:
#####
    def __init__(self):
        self.usd_sale = 0
        self.usd_buy = 0
        self.euro_sale = 0
        self.euro_buy = 0

class PrivatHelper(BaseHelper):
#####
    def create_currency_obj(self, obj):
        try:
            for i in obj:
                try:
                    if i['currency'] == 'USD':
                        self.create_obj.usd_buy = i['saleRate']
                        self.create_obj.usd_sale = i['purchaseRate']
                    elif i['currency'] == 'EUR':
                        self.create_obj.euro_buy = i['saleRate']
                        self.create_obj.euro_sale = i['purchaseRate']
                except:
                    pass
        finally:
            return self.create_obj

class MonoHelper(BaseHelper):
#####
    def create_currency_obj(self, obj):
        try:
            for i in obj:
                # try:
                if i['currencyCodeA'] == 840 and i['currencyCodeB'] == 980:
                    self.create_obj.usd_buy = i['rateSell']
                    self.create_obj.usd_sale = i['rateBuy']
                elif i['currencyCodeA'] == 978 and i['currencyCodeB'] == 980:
                    self.create_obj.euro_buy = i['rateSell']
                    self.create_obj.euro_sale = i['rateBuy']
                # except:
                #     pass
        finally:
            return self.create_obj

class NbuHelper(BaseHelper):
#####
    def create_currency_obj(self, obj):
        try:
            for i in obj:
                try:
                    if i['cc'] == 'USD':
                        self.create_obj.usd_sale = i['rate']
                        # self.create_obj.usd_sale = i['purchaseRate']
                    elif i['cc'] == 'EUR':
                        # self.create_obj.euro_buy = i['saleRate']
                        self.create_obj.euro_sale = i['rate']
                except:
                    pass
        finally:
            return self.create_obj

if __name__ == '__main__':
    a = PrivatHelper()
    b = MonoHelper()
    c = NbuHelper()



