from threading import Thread, Event
import time
import random

boot = Event()


def server():
    print('启动服务器。。。。')
    time.sleep(random.randint(1, 3))
    print('服务器运行。。。。。')
    boot.set()


def connect():
    print('开始尝试连接')
    boot.wait()
    print('连接成功')


t1 = Thread(target=server)
t1.start()

t2 = Thread(target=connect)
t2.start()
