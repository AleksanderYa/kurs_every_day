import os
import django
from currency.workers import PrivatWorker, MonoWorker, NbuWorker
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from currency.models import Currency


class ExchangeRateRepository:
#####
    @staticmethod
    def create_db_obj():
        model = Currency()
        privat_w = PrivatWorker()
        privat = privat_w.get()
        mono_w = MonoWorker()
        mono = mono_w.get()
        nbu_w = NbuWorker()
        nbu = nbu_w.get()
        model.privat_usd_buy = privat.usd_buy
        model.privat_usd_sale = privat.usd_sale
        model.privat_eur_buy = privat.euro_buy
        model.privat_eur_sale = privat.euro_sale
        model.mono_usd_buy = mono.usd_buy
        model.mono_usd_sale = mono.usd_sale
        model.mono_eur_buy = mono.euro_buy
        model.mono_eur_sale = mono.euro_sale
        model.nbu_usd = nbu.usd_sale
        model.nbu_eur = nbu.euro_sale
        model.save()
        print('Dane!')

class GetterExchangeRate:
    @staticmethod
    def get():
        obj = Currency.objects.all()
        return obj

if __name__ == '__main__':
    ExchangeRateRepository.create_db_obj()





















