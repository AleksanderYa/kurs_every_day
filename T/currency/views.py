from django.shortcuts import render, HttpResponse
from currency.forms import UserForm

class ExchangeRateController:
    @staticmethod
    def bunk_rates(request):
        return render(request, 'currency/index.html')

    @staticmethod
    def test(request):
        if request.method == "POST":
            name = request.POST.get("name")
            age = request.POST.get("age")     # получение значения поля age
            return HttpResponse(f"<h2>Hello, {name}, - {age}</h2>")
        else:
            userform = UserForm()
            return render(request, "currency/test.html", {"form": userform})