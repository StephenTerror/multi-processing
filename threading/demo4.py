from multiprocessing import Process
from threading import Thread
import time


def task():
    pass


def expense(cls):
    """用来测试线程或进程创建开销"""
    lis = []
    start = time.time()
    for i in range(50):
        p = cls(target=task, )
        p.start()
        lis.append(p)
    for p in lis:
        p.join()
    return time.time() - start


print(expense(Thread))
print(expense(Process))
