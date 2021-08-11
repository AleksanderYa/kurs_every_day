from currency.workers import PrivatWorker, MonoWorker, NbuWorker
from abc import ABC, abstractmethod

class BaseHelper(ABC):

    def for_in(func):
        def inner(*args, **kwargs):
            ii = func(*args, **kwargs)
            for i in ii:
                print(i)
        return inner

    @abstractmethod
    def create_currency_obj(self):
        raise NotImplementedError

class PrivatHelper(BaseHelper):
    @BaseHelper.for_in
    def create_currency_obj(self):
        privat = PrivatWorker()
        res = privat.get_currency_json()
        return res

class MonoHelper(BaseHelper):
    @BaseHelper.for_in
    def create_currency_obj(self):
        mono = MonoWorker()
        res = mono.get_currency_json()
        return res

class NbuHelper(BaseHelper):
    @BaseHelper.for_in
    def create_currency_obj(self):
        nbu = NbuWorker()
        res = nbu.get_currency_json()
        return res


if __name__ == '__main__':

    a = PrivatHelper()
    a.create_currency_obj()

    # b = MonoHelper()
    # b.create_currency_obj()

    c = NbuWorker()
    c.get_currency_json()


