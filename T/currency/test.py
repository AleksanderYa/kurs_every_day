import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from currency.models import Currency

bases = {
    'base': Currency.objects.all()
}

