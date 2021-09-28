from django.urls import path, re_path
from currency.views import ExchangeAllViews
from currency.views import ExchangeNBUView
from currency.views import ExchangeMonoView
from currency.views import ExchangePrivatView
    
app_name = 'currency'
urlpatterns = [
    # re_path(r'^exchangetimesetup/(?P<time>\d+)/', ExchangeRateController.timer),
    # path('bankrates/', ExchangeRateController.bunk_rates),
    # path('exchangetimesetup/', ExchangeRateController.timer),
    # path('test/', ExchangeRateController.test),
    path('rates/', ExchangeAllViews.as_view()),
    path ('rates/nbu/', ExchangeNBUView.as_view(), name='nbu_view'),
    path ('rates/mono/', ExchangeMonoView.as_view(), name='mono_view'),
    path ('rates/privat/', ExchangePrivatView.as_view(), name='privat_view'),
]
