from django.shortcuts import render
from django.http import HttpResponse
from django_q.tasks import async_task, schedule
from django_q.models import Schedule
from .todo import do
from datetime import timedelta, timezone
# from bf.go_parse import main
# 

def index(request):
    async_task(do, 'Alex')
    hi = '<h1>Hi men, all good work!</h1>'
    return HttpResponse(hi)

def shed(request):
    a = 'Sasha'
    schedule(
        'tasker.hello',2,
             schedule_type=Schedule.MINUTES, minutes=1)
    hi = '<h1>Shed in work!</h1>'
    return HttpResponse(hi)

def cancel_shed(request):
    schedule('django_q.tasks.clear_sessions_command', schedule_type='O')
    schedule('django_q.tasks.clear_sessions_command', schedule_type='M')
    schedule('django_q.tasks.clear_sessions_command', schedule_type='H')
    hi = '<h1>Shed is cancell!</h1>'
    return HttpResponse(hi)

def start_bf(request):
    a = 'Sasha'
    # schedule(
    #     'bf.go_parse.main',
    #     schedule_type=Schedule.ONCE,
    #     next_run=timezone.now() + timedelta(minutes=5)
    # )
    hi = '<h1>Shed in work!</h1>'
    return HttpResponse(hi)

def hello():
    print('Hello')

