from django.urls import path, re_path
from currency.views import ExchangeAllViews
from currency.views import ExchangeNBUView
from currency.views import ExchangeMonoView
from currency.views import ExchangePrivatView
    

urlpatterns = [

    # re_path(r'^exchangetimesetup/(?P<time>\d+)/', ExchangeRateController.timer),
    # path('bankrates/', ExchangeRateController.bunk_rates),
    # path('exchangetimesetup/', ExchangeRateController.timer),
    # path('test/', ExchangeRateController.test),
<<<<<<< HEAD
    path('rates/', ExchangeAllRate.as_view()),
    path ('rates/nbu', ExchangeNBURate.as_view())

=======
    path('rates/', ExchangeAllViews.as_view()),
    path ('rates/nbu/', ExchangeNBUView.as_view()),
    path ('rates/mono/', ExchangeMonoView.as_view()),
    path ('rates/privat/', ExchangePrivatView.as_view()),
>>>>>>> 3de27a1e88e07c5b9b7c368ffff3f44b649d02c2
]
