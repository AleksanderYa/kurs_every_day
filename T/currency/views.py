from django.shortcuts import render
from currency.models import Currency as c
from currency.get_kurs import get_privat_currency

dic = get_privat_currency()

# Currency.objects.all()



def button_to_base(request):
    nbu = c.objects.all()
    nbu = nbu[0]
    dictt = {
        'nbu_price_usd': nbu.nbu_usd,
        'nbu_price_eur': nbu.nbu_eur
    }
    c.objects.create(
        nbu_usd=dic['nbu_price_usd'],
        nbu_eur = dic['nbu_price_eur'],
        privat_usd_sale = dic[ 'privat_price_usd_sale'],
        privat_usd_bay =  dic['privat_price_usd_bay'],
        privat_eur_sale =  dic['privat_price_eur_sale'],
        privat_eur_bay =  dic['privat_price_eur_bay']
    )
    return render(request, 'currency/button_to_base.html', dictt)

def button(request):
    return render(request, 'currency/button.html')