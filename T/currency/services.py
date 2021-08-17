import os
import django
import requests
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from currency.models import Currency
from django_q.tasks import Chain
from django_q.tasks import schedule




class ExchangeRateService:
    @staticmethod
    def task_group_send_mess():
        obj = Currency.objects.all()[:1].get()
        messsage = f'_Курс валют \n{str(obj.date)[:16]}_\n\n*НБУ*\n*USD {obj.nbu_usd}*\n*EURO {obj.nbu_eur}*\n\n' \
                   f'*ПриватБанк*\n*USD  {obj.privat_usd_bay} / {obj.privat_usd_sale}*\n' \
                   f'*EURO  {obj.privat_eur_bay} / {obj.privat_eur_sale}*\n\n' \
                   f'*MonoBank*\n*USD {obj.mono_usd_bay} / {obj.mono_usd_sale}*\n*EURO {obj.mono_eur_bay} / {obj.mono_eur_sale}*'
        chain = Chain(cached=True, sync=True)
        chain.append('currency.repositories.ExchangeRateRepository.create_db_obj')
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
        bot_token = '1841807907:AAElQcKWBvFg8JRMJilil0kqi6nJ5b_TSKM'
        bot_chatID = '1075097936'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?' \
                    'chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

if __name__ == '__main__':
    ExchangeRateService.sched()