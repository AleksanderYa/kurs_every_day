from django.shortcuts import render, HttpResponse
from bf.go_parse import main
from schedule import every, repeat, run_pending
from bf.go_parse import main
import time


# def start(request):
#     # start()
#     main()
#     return HttpResponse(request, 'All work!')
START = False


def index(request):
    global START
    res = {
        'start':START
    }
    return render(request, 'bf/index.html', res)

def start(request):
    global START
    START = True
    res = {
        'start': START
    }
    @repeat(every(1).minutes)
    def job():
        print('Start shedule')
        main()
        print("I am all dane")
    while START:
        run_pending()
        time.sleep(10)
    return render(request, 'bf/index.html', res)

def stop(request):
    global START
    START = False
    res = {
        'start': START
    }
    return render(request,'bf/index.html', res)