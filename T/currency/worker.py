import os
import django
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from django_q.tasks import async_task, schedule

def task():
    tsk = async_task(
        'currency.get_kurs_oop.main'
    )
    print('Task dane!')


def sched():
    schd = schedule(
        'currency.get_kurs_oop.main',
        schedule_type='I',
        minutes=2,
        repeats=10,
        next_run=datetime.now()
    )
    print('Sched in turnOn')

sched()