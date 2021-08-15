from django.shortcuts import render, HttpResponse
# from currency.services import ExchangeRateService


class ExchangeRateController:
    @staticmethod
    def bunk_rates(request):
        # rates = ExchangeRateService()
        # rates.sched()
        return render(request, 'currency/index.html')