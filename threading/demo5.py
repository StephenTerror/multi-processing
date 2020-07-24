from threading import Thread, Lock
import time

num = 10


def task(lock):
    global num
    lock.acquire()
    a = num
    time.sleep(0.5)
    num = a - 1
    lock.release()


ts = []
lock = Lock()
for i in range(10):
    t = Thread(target=task, args=(lock,))
    t.start()
    ts.append(t)
for t in ts:
    t.join()
print(num)
