import os
import django
from currency.workers import PrivatWorker, MonoWorker, NbuWorker
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from currency.models import Currency


class ExchangeRateRepository:
#####
    # # @staticmethod
    # def __init__(self):
    #     self.model = Currency()
    #     self.privat_w = PrivatWorker()
    #     self.privat = self.privat_w.get()
    #     self.mono_w = MonoWorker()
    #     self.mono = self.mono_w.get()
    #     self.nbu_w = NbuWorker()
    #     self.nbu = self.nbu_w.get()

    # # @staticmethod
    # def create_db_obj(self):
    #     self.model.privat_usd_bay = self.privat.usd_buy
    #     self.model.privat_usd_sale = self.privat.usd_sale
    #     self.model.privat_eur_bay = self.privat.euro_buy
    #     self.model.privat_eur_sale = self.privat.euro_sale
    #     self.model.mono_usd_bay = self.mono.usd_buy
    #     self.model.mono_usd_sale = self.mono.usd_sale
    #     self.model.mono_eur_bay = self.mono.euro_buy
    #     self.model.mono_eur_sale = self.mono.euro_sale
    #     self.model.nbu_usd = self.nbu.usd_sale
    #     self.model.nbu_eur = self.nbu.euro_sale
    #     self.model.save()
    #     print('Dane!')
    @staticmethod
    def create_db_obj():
        model = Currency ()
        privat_w = PrivatWorker ()
        privat = privat_w.get ()
        mono_w = MonoWorker ()
        mono = mono_w.get ()
        nbu_w = NbuWorker ()
        nbu = nbu_w.get ()
        model.privat_usd_bay = privat.usd_buy
        model.privat_usd_sale = privat.usd_sale
        model.privat_eur_bay = privat.euro_buy
        model.privat_eur_sale = privat.euro_sale
        model.mono_usd_bay = mono.usd_buy
        model.mono_usd_sale = mono.usd_sale
        model.mono_eur_bay = mono.euro_buy
        model.mono_eur_sale = mono.euro_sale
        model.nbu_usd = nbu.usd_sale
        model.nbu_eur = nbu.euro_sale
        model.save()
        print('Dane!')


def main():
    # reposit = ExchangeRateRepository()
    # reposit.create_db_obj()
    ExchangeRateRepository.create_db_obj()


if __name__ == '__main__':
    main()





















