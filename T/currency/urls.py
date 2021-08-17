from django.urls import path
from currency.views import ExchangeRateController
    

urlpatterns = [
    path('bankrates/', ExchangeRateController.bunk_rates)
]
