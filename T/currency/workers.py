from abc import ABCMeta, abstractmethod
from datetime import datetime
import requests


class ChangeDate:
    def correct_data(self):
        date = datetime.now()
        month = str(date.month)
        if len(month) < 2:
            month = '0' + month
            res = f'{date.day}.{month}.{date.year}'
            return res
        else:
            return f'{date.day}.{date.month}.{date.year}'
#



class BaseBankWorker(metaclass=ABCMeta):
    def get_currency_json(self):
        try:
            url = requests.get(self.SITE)
            url = url.json()
            return url
        except Exception as e:
            print(e)

    # @abstractmethod
    # def get_currency_info(self):
    #     raise NotImplementedError("check_ripeness method not implemented!")

class PrivatWorker(BaseBankWorker):
    date = ChangeDate()
    SITE = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date.correct_data()}'


class NbuWorkers(BaseBankWorker):
    pass

class MonoWorker(BaseBankWorker):
    pass

a = PrivatWorker()
print(a.get_currency_json())