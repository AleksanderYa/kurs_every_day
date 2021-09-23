from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency/', include('currency.urls')),
    path('', include('log_in.urls')),
]
