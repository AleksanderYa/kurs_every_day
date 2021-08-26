from django.urls import path, re_path
from currency.views import ExchangeRateController
    

urlpatterns = [

    re_path(r'^exchangetimesetup/(?P<time>\d+)/', ExchangeRateController.timer),
    path('bankrates/', ExchangeRateController.bunk_rates),
    path('exchangetimesetup/', ExchangeRateController.timer),
    path('test/', ExchangeRateController.test),
    path('rates/', ExchangeRateController.get_all_banks)

]
