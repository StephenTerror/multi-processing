from threading import Thread
import time


def task():
    global num
    time.sleep(1)
    num -= 1


num = 10
t = Thread(target=task, )
t.start()
t.join()
print(num)
