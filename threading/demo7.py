from threading import Thread, RLock

lock = RLock()
lock.acquire()
lock.acquire()
lock.acquire()
lock.acquire()

print("over")
lock = RLock()


def task1():
    lock.acquire()
    print('task1')
    # lock.release()


def task2():
    lock.acquire()
    print('task2')


Thread(target=task1).start()
Thread(target=task2).start()
