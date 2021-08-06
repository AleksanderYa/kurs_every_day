import os
import django
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from django_q.tasks import async_task, schedule, async_chain, result_group, Chain
from currency.models import Currency

# def task():
#     async_task(
#         'currency.get_kurs_oop.main'
#     )
#     print('Task dane!')
#
#
# def task_send_mess():
#     obj = Currency.objects.all()[:1].get()
#     messsage = f'_Курс валют \n{str(obj.date)[:10]}_\n\n*НБУ*\n*USD {obj.nbu_usd}*\n*EURO {obj.nbu_eur}*\n\n' \
#                f'*ПриватБанк*\n*USD  {obj.privat_usd_bay} / {obj.privat_usd_sale}*\n' \
#                f'*EURO  {obj.privat_eur_bay} / {obj.privat_eur_sale}*'
#     async_task(
#         'currency.telegram_bot.send_message',
#         messsage
#     )
#     print('Task to telega dane!')


def task_group_send_mess():
    obj = Currency.objects.all()[:1].get()
    messsage = f'_Курс валют \n{str(obj.date)[:10]}_\n\n*НБУ*\n*USD {obj.nbu_usd}*\n*EURO {obj.nbu_eur}*\n\n' \
               f'*ПриватБанк*\n*USD  {obj.privat_usd_bay} / {obj.privat_usd_sale}*\n' \
               f'*EURO  {obj.privat_eur_bay} / {obj.privat_eur_sale}*'
    chain = Chain(cached=True)
    chain.append('currency.get_kurs_oop.main')
    chain.append('currency.telegram_bot.send_message', messsage)
    chain.run()


def sched():
    schedule(
        'currency.worker.task_group_send_mess',
        name='Schedule kurs',
        schedule_type='I',
        minutes=1,
        repeats=-1,
        next_run=datetime.now()
    )
    print('Sched in turnOn')



