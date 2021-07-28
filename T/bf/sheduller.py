from schedule import every, repeat, run_pending
from bf.go_parse import main
import time

def start():
    @repeat(every(1).minutes)
    def job():
        print('Start shedule')
        main()
        print("I am all dane")

    while True:
        run_pending()
        time.sleep(10)