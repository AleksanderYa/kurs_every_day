from django.shortcuts import render, HttpResponse


class ExchangeRateController:
    @staticmethod
    def bunk_rates(request):
        return render(request, 'currency/index.html')