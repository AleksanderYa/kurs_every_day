from django.contrib import admin
from .models import Currency
from .models import GovBank


admin.site.register(GovBank)
admin.site.register(Currency)