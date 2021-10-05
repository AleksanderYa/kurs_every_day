from django.shortcuts import render
from django.http import request
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

from currency.controllers import ExchangeRateController
from django.contrib.auth.models import User


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
        print(request.user.groups.all())
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










