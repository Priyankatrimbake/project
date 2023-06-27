import schedule
import time

def ourfun():
    print("Hello World")
    
schedule.every(10).seconds.do(ourfun)
while 1:
    schedule.run_pending()
    time.sleep(1)
    