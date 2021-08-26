from django.shortcuts import render, HttpResponse
from currency.forms import UserForm
from currency.models import Currency

class ExchangeRateController:
    @staticmethod
    def get_all_banks(request):
        base = Currency.objects.all()
        enum =  enumerate(base)
        return render(
            request,
            'currency/table_all_banks.html',
            {'enum': enum}
        )

    @staticmethod
    def bunk_rates(request):
        return render(request, 'currency/index.html')

    @staticmethod
    def test(request):
        if request.method == "POST":
            name = request.POST.get("name")
            age = request.POST.get("age")     # получение значения поля age
            return HttpResponse(f"<h2>Hello, {name}, - {age} </h2>")
        else:
            userform = UserForm()
            return render(request, "currency/test.html", {"form": userform})

    @staticmethod
    def timer(request):
        req = request.POST.get('timer_time') == 'Select work time'
        if request.method == "POST":
            time = request.POST.get('timer_time')
            text = {
                'text': f'Установлено...\nЧерез каждые {time} минут будет сделано дело!'
            }
            return render(request, "currency/timer.html", text)
        elif req:
            return render (request, "currency/timer.html", {'text': 'Выберите время из списка выше'})
        else:
            text = {
                'text': 'Время работы бота не установленно'
            }
            return render(request, "currency/timer.html", text)














