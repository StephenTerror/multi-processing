from threading import Thread, Lock
import time


def task1(name, locka, lockb):
    locka.acquire()
    print("%s拿到a锁" % name)
    time.sleep(0.3)
    lockb.acquire()
    print('%s拿到b锁' % name)
    lockb.release()
    locka.release()


def task2(name, locka, lockb):
    lockb.acquire()
    print("%s拿到b锁" % name)
    time.sleep(0.3)
    locka.acquire()
    print('%s拿到a锁' % name)
    locka.release()
    lockb.release()


locka = Lock()
lockb = Lock()
t1 = Thread(target=task1, args=('t1', locka, lockb))
t2 = Thread(target=task2, args=('t2', locka, lockb))
t1.start()
t2.start()
