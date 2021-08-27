from django.shortcuts import render, HttpResponse
from django.views.generic.base import View

from currency.controllers import ExchangeRateController


class ExchangeRateViews(View):
    def __init__(self):
        self.enum = ExchangeRateController()
        self.enum = self.enum.get()

class ExchangeAllViews(ExchangeRateViews):
    def get(self, request):
        return render(
            request,
            'currency/table_all_banks.html',
            {'enum': self.enum}
        )

class ExchangeNBUView(ExchangeRateViews):
    def get(self, request):
        return render (
            request,
            'currency/table_nbu_bank.html',
            {'enum': self.enum}
        )

class ExchangeMonoView(ExchangeRateViews):
    def get(self, request):
        return render(
            request,
            'currency/table_mono_bank.html',
            {'enum': self.enum}
        )

class ExchangePrivatView(ExchangeRateViews):
    def get(self, request):
        return render(
            request,
            'currency/table_privat_bank.html',
            {'enum': self.enum}
        )










