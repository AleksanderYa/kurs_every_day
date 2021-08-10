import os
import django
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from django_q.tasks import async_task, schedule
from T.currency.models import Currency


obj = Currency.objects.all()[:1].get()
print(obj.date)
print(obj.nbu_usd)

print(obj)