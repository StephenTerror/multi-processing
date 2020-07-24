from threading import Thread


def task():
    print("subthread is running....")


t = Thread(target=task)
t.start()
print('main is over....')

# ------------------------------------
from threading import Thread


class MyThread(Thread):
    def run(self):
        print("subthread is running....")

mythread = MyThread()
mythread.start()
