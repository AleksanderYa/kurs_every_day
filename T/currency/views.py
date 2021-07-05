from django.shortcuts import render, redirect
from currency.models import Currency as c
from currency.get_kurs import get_privat_currency
from currency.telega2 import telegram_bot_sendtext


dic = get_privat_currency()
# nbu = c.objects.all()
# Currency.objects.all()

nbu = c.objects.all()
nbu = nbu[::-1]
nbu = nbu[0]

def button_to_base(request):
    # nbu = c.objects.get(pk=1)

    dictt = {
        'nbu_price_usd': nbu.nbu_usd,
        'nbu_price_eur': nbu.nbu_eur
    }
    return render(request, 'currency/button_to_base.html', dictt)

def get_currency_to_base(request):
    return redirect(request, 'currency/button_to_base.html')

def button(request):
    return render(request, 'currency/button.html')

def send_mess_telega(request):
    base_dict = dic.copy()
    base_dict['title'] = 'KURS'
    message = f'USD{nbu.nbu_usd}\nEUR{nbu.nbu_eur}'
    telegram_bot_sendtext(bot_message=message)
    return render(request, 'currency/button_to_base.html', base_dict)

def mirror(request):
    base_dict = dic.copy()
    base_dict['title'] = 'Mirror'
    base_dict['all_kurs'] = c.objects.all()
    message = f'USD{nbu.nbu_usd}\nEUR{nbu.nbu_eur}'
    telegram_bot_sendtext(bot_message=message)
    return render(request, 'currency/mirror.html', base_dict)

def tested(request):
    return render(request, 'currency/tested.html')