from django.shortcuts import render, HttpResponse, redirect
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
    @repeat(every(5).minutes)
    def job():
        print('Start shedule')
        main()
        print("I am all dane")

    while START:
        run_pending()
        time.sleep(10)
    return redirect('/index/')

def stop(request):
    global START
    START = False
 
    return redirect('/index/')