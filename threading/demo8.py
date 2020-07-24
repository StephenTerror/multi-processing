from threading import Semaphore, Thread
import time

s_lock = Semaphore(200)

num = 0


def task():
    s_lock.acquire()
    # time.sleep(1)
    global num
    num = num + 1
    # print("run.....")
    s_lock.release()


for i in range(4000000):
    t = Thread(target=task)
    t.start()
