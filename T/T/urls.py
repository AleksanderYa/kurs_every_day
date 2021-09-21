from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('currency.urls')), 
    path('test/', include('testing.urls')),
]
