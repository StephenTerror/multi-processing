import random
import time
import threading
from threading import Thread


def task(name):
    print("%s is running..." % name)
    time.sleep(random.randint(1, 3))
    print(threading.enumerate())
    print("%s is over....." % name)


t = Thread(target=task, args=('aaa',))
t.start()

print('main over....')
