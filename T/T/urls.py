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
from django.contrib import admin
from django.urls import path, re_path, include
#from testy import  views    

urlpatterns = [
    # path('one/',  include('currency.urls')),
#    path('show/',  views.show),  
    path('admin/', admin.site.urls),
    path('', include('bf.urls')),
    path('tasker/', include('tasker.urls')),
# #    path('index/', views.index),
#     path('testy/', include('testy.urls')),
#     path('', include('quickstart.urls')),
#     path('api/', include('rest_framework.urls')),
#     re_path(r'^', include('polls.urls')),
]
