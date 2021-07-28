from django.shortcuts import render, HttpResponse
from bf.go_parse import main
from schedule import every, repeat, run_pending
from bf.go_parse import main
import time


def start(request):
    # start()
    main()
    return HttpResponse(request, 'All work!')


def shedullers(request):
    @repeat(every(5).minutes)
    def job():
        print('Start shedule')
        main()
        print("I am all dane")

    while True:
        run_pending()
        time.sleep(10)