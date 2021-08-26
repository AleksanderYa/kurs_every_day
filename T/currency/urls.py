from django.urls import path, re_path
from currency.views import ExchangeAllRate
from currency.views import ExchangeNBURate
    

urlpatterns = [

    # re_path(r'^exchangetimesetup/(?P<time>\d+)/', ExchangeRateController.timer),
    # path('bankrates/', ExchangeRateController.bunk_rates),
    # path('exchangetimesetup/', ExchangeRateController.timer),
    # path('test/', ExchangeRateController.test),
    path('rates/', ExchangeAllRate.as_view()),
    path ('rates/nbu/', ExchangeNBURate.as_view())

]
