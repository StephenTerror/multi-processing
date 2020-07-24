import time
import random
from multiprocessing import Process


class Run(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s runing' % self.name)
        time.sleep(random.randrange(1, 5))
        print('%s runing end' % self.name)


p1 = Run('anne')
p2 = Run('alex')
p3 = Run('ab')
p4 = Run('hey')
p1.start()  # start会自动调用run
p2.start()
p3.start()
p4.start()
p1.join()  # 等待p1进程停止
p2.join()
p3.join()
p4.join()
print('主线程')

# 注意上面的代码是主进程等待子进程，等待的是主进程，所以等待的总时间是子进程中耗费时间最长的那个进程运行的时间

# 上述启动进程与join进程可以简写为
# p_l=[p1,p2,p3,p4]
#
# for p in p_l:
#     p.start()
#
# for p in p_l:
#     p.join()
