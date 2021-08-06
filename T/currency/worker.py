import os
import django
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from django_q.tasks import async_task, schedule
from currency.models import Currency

def task():
    async_task(
        'currency.get_kurs_oop.main'
    )
    print('Task dane!')


def task_send_mess():
    obj = Currency.objects.all()[:1].get()
    messsage = f'_Курс валют \n{str(obj.date)[:10]}_\n\n*НБУ*\n*USD {obj.nbu_usd}*\n*EURO {obj.nbu_eur}*\n\n' \
               f'*ПриватБанк*\n*USD  {obj.privat_usd_bay} / {obj.privat_usd_sale}*\n' \
               f'*EURO  {obj.privat_eur_bay} / {obj.privat_eur_sale}*'

    async_task(
        'currency.telegram_bot.send_message',
        messsage
    )
    print('Task to telega dane!')


def sched():
    obj = Currency.objects.all()[:1].get()
    messsage = f'_Курс валют \n{str(obj.date)[:10]}_\n\n*НБУ*\n*USD {obj.nbu_usd}*\n*EURO {obj.nbu_eur}*\n\n' \
               f'*ПриватБанк*\n*USD  {obj.privat_usd_bay} / {obj.privat_usd_sale}*\n' \
               f'*EURO  {obj.privat_eur_bay} / {obj.privat_eur_sale}*'
    schedule(
        'currency.telegram_bot.send_message',
        messsage,
        schedule_type='I',
        minutes=2,
        repeats=10,
        next_run=datetime.now()
    )
    print('Sched in turnOn')

sched()