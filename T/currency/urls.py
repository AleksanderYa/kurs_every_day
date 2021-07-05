"""T URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *
    

urlpatterns = [
    path('', button, name='currency-button'),
    path('to_base/', button_to_base, name='currency-button-to-base'),
    path('send_telega/', send_mess_telega, name='send-telega'),
    path('get_to_base/', get_currency_to_base, name='get_base'),
    path('mirror/', mirror, name='mirror'),
    path('tested/', tested, name='tested'),

]
