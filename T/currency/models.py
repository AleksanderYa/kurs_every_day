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

class Currency(models.Model):
    date = models.DateTimeField(auto_now=True)
    nbu_usd = models.FloatField()
    nbu_eur = models.FloatField()
    privat_usd_sale = models.FloatField()
    privat_usd_bay = models.FloatField()
    privat_eur_sale = models.FloatField()
    privat_eur_bay = models.FloatField()
    a = models.DateField


    def __str__(self):
        return f'Date: {str(self.date)[0:10]} Price: {self.nbu_usd} /{self.nbu_eur} '