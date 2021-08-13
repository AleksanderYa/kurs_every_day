from abc import ABC, abstractmethod

class BaseHelper(ABC):

    @abstractmethod
    def create_currency_obj(self, res):
        raise NotImplementedError


class PrivatHelper(BaseHelper):
    def create_currency_obj(self, res):
        pass

class MonoHelper(BaseHelper):
    def create_currency_obj(self, res):
        pass

class NbuHelper(BaseHelper):
    def create_currency_obj(self, res):
        pass

if __name__ == '__main__':

    a = PrivatHelper()
    b = MonoHelper()
    c = NbuHelper()



