from django.conf import settings
from django.db import models
from django.utils import timezone


class GovBank(models.Model):
    currencys = [
        ('USD', 'USD'),
        ('EUR', 'EUR')
    ]
    id_currency = models.IntegerField() 
    name_currency = models.CharField(max_length=3, choices=currencys)
    value_currency = models.FloatField()
    date_carrency = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f'{self.name_currency}-{self.value_currency}      Date create: {self.date_carrency.date()}'