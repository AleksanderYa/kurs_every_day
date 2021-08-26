import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from currency.models import Currency


class CurrencyController():
    def __init__(self):
        self.base = Currency.objects.all()

class GetAllRates(CurrencyController):
    def get(self):
        res = type(self.base)
        print(res)


if __name__ == '__main__':
    a = GetAllRates()
    a.get()




