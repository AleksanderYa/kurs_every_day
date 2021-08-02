from django.contrib import admin
from django.urls import path, re_path, include
from .views import index, shed, cancel_shed, start_bf

urlpatterns = [
    path('', index),
    path('start/', shed),
    path('stop/', cancel_shed),
    path('bf/', start_bf),
]
