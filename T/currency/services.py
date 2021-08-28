import os
import django
import requests
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()

from django_q.tasks import Chain
from django_q.tasks import schedule
from currency.parametrs import TELEGRAM_BOT_TOKEN
from currency.parametrs import TELEGRAM_URL
from currency.parametrs import TELEGRAM_CHAT_IP
from currency.models import Currency


class ExchangeRateService:
    @staticmethod
    def task_group_send_mess():
        obj = Currency.objects.all()[:1].get()
        messsage = f'_Курс валют \n{str(obj.date)[:16]}_\n\n*НБУ*\n*USD {obj.nbu_usd}*\n*EURO {obj.nbu_eur}*\n\n' \
                   f'*ПриватБанк*\n*USD  {obj.privat_usd_buy} / {obj.privat_usd_sale}*\n' \
                   f'*EURO  {obj.privat_eur_buy} / {obj.privat_eur_sale}*\n\n' \
                   f'*MonoBank*\n*USD {obj.mono_usd_buy} / {obj.mono_usd_sale}*\n*EURO {obj.mono_eur_buy} / {obj.mono_eur_sale}*'
        chain = Chain(cached=True, sync=True)
        # chain.append('currency.repositories.ExchangeRateRepository.create_db_obj')
        chain.append('currency.services.TelegramBotService.send_message', messsage)
        chain.run()

    @staticmethod
    def sched(minute=1):
        schedule(
            'currency.services.ExchangeRateService.task_group_send_mess',
            name='Schedule kurs',
            schedule_type='I',
            minutes=minute,
            repeats=-1,
            next_run=datetime.now()
        )
        print ('Sched in turnOn')

class TelegramBotService:
    @staticmethod
    def send_message(bot_message):
        send_text = TELEGRAM_URL.replace('TOKEN', TELEGRAM_BOT_TOKEN)
        send_text = send_text.replace('CHATID', TELEGRAM_CHAT_IP)
        send_text = send_text + bot_message
        print(send_text)
        response = requests.get(send_text)
        print()
        return response.json()

if __name__ == '__main__':
    ExchangeRateService.sched()
