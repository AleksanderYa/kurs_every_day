# from django.shortcuts import render
# from currency.models import Currency as c
# # from currency.get_kurs import get_privat_currency
# from currency.telega2 import telegram_bot_sendtext
#
#
# def button_to_base(request):
#     # nbu = c.objects.get(pk=1)
#
#     dictt = {
#         'nbu_price_usd': '',
#         'nbu_price_eur': ''
#     }
#     return render(request, 'currency/button_to_base.html', dictt)
#
# def button(request):
#     return render(request, 'currency/button.html')
#
# def send_mess_telega(request):
#     base_dict = dic.copy()
#     base_dict['title'] = 'KURS'
#     message = f'USD{nbu.nbu_usd}\nEUR{nbu.nbu_eur}'
#     telegram_bot_sendtext(bot_message=message)
#     return render(request, 'currency/button_to_base.html', base_dict)
#
# def mirror(request):
#     base_dict = dic.copy()
#     base_dict['title'] = 'Mirror'
#     cobject = c.objects.all()[::-1]
#     base_dict['all_kurs'] = c.objects.all()
#     message = f'USD{nbu.nbu_usd}\nEUR{nbu.nbu_eur}'
#     telegram_bot_sendtext(bot_message=message)
#     return render(request, 'currency/mirror.html', base_dict)
#
# def tested(request):
#     return render(request, 'currency/tested.html')
#
# def get_currency_to_base(request):
#     base_dict = dic.copy()
#     c.objects.create(
#         nbu_usd=dic['nbu_price_usd'],
#         nbu_eur = dic['nbu_price_eur'],
#         privat_usd_sale = dic[ 'privat_price_usd_sale'],
#         privat_usd_bay =  dic['privat_price_usd_bay'],
#         privat_eur_sale =  dic['privat_price_eur_sale'],
#         privat_eur_bay =  dic['privat_price_eur_bay']
#     )
#     return render(request, 'currency/button_to_base.html', base_dict)