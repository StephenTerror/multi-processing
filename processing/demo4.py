from multiprocessing import Process
import time
import random


class Run(Process):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def run(self):
        print('%s is piaoing' % self.name)
        time.sleep(random.randrange(1, 3))
        print('%s is piao end' % self.name)


p = Run('anne')
p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
p.start()
print('主')

'''
主进程创建守护进程

1）守护进程会在主进程代码执行结束后就终止

2）守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children

注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止
'''
