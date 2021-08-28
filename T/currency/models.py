from django.conf import settings
from django.db import models
from django.utils import timezone


class Currency(models.Model):
    date = models.DateTimeField(auto_created=True, auto_now=True)
    nbu_usd = models.FloatField()
    nbu_eur = models.FloatField()
    privat_usd_sale = models.FloatField()
    privat_usd_buy = models.FloatField()
    privat_eur_sale = models.FloatField()
    privat_eur_buy = models.FloatField()
    mono_usd_sale = models.FloatField()
    mono_usd_buy = models.FloatField()
    mono_eur_sale = models.FloatField()
    mono_eur_buy = models.FloatField()

    def __str__(self):
        return f'Date: {str(self.date)[0:10]} Price: {self.nbu_usd} /{self.nbu_eur} '

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'
        ordering = ['-date']



