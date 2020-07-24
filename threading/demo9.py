import threading
from threading import Thread
import time


def task1():
    print('thread-1 is running...')
    time.sleep(3)
    print('thread-1 over....')


def task2():
    print('thread-2 is running...')
    time.sleep(1)
    print('thread-2 over....')


if __name__ == '__main__':
    t1 = Thread(target=task1, )
    t2 = Thread(target=task2, )
    t1.setDaemon(True)
    t1.start()
    t2.start()
    print(t1.ident)
    print(threading.enumerate())
    print("main over...")
