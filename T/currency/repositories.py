import os
import django
from currency.workers import PrivatWorker, MonoWorker, NbuWorker
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from currency.models import Currency


class SetterBase:
#####
    def __init__(self):
        self.model = Currency()
        self.privat_w = PrivatWorker()
        self.privat = self.privat_w.get()
        self.mono_w = MonoWorker()
        self.mono = self.mono_w.get()
        self.nbu_w = NbuWorker()
        self.nbu = self.nbu_w.get()

    def create_db_obj(self):
        self.model.privat_usd_bay = self.privat.usd_buy
        self.model.privat_usd_sale = self.privat.usd_sale
        self.model.privat_eur_bay = self.privat.euro_buy
        self.model.privat_eur_sale = self.privat.euro_sale
        self.model.mono_usd_bay = self.mono.usd_buy
        self.model.mono_usd_sale = self.mono.usd_sale
        self.model.mono_eur_bay = self.mono.euro_buy
        self.model.mono_eur_sale = self.mono.euro_sale
        self.model.nbu_usd = self.nbu.usd_sale
        self.model.nbu_eur = self.nbu.euro_sale
        self.model.save()
        print('Dane!')


if __name__ == '__main__':
    a = SetterBase()
    a.create_db_obj()


























