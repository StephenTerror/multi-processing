from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

maxsize = 10
timeout = 1000
wait = False  # ，立即返回，并不会等待池内的任务执行完毕
wait = True  # ， 等待池内所有任务执行完毕后回收资源才继续
step = 0


def task(name):
    global step
    step += 1
    print(step, name)
    time.sleep(1)


pool = ProcessPoolExecutor(maxsize)  # 创建进程池，maxsize为最大进程个数
# pool = ThreadPoolExecutor  # 创建线程池，maxsize为最大进程个数

for i in range(100):
    res = pool.submit(task, i)  # , 提交任务

res.result(timeout)  # ，接收调用的返回值，timeout为超时时间，超时报错# 该函数是阻塞函数，会一直等待任务执行完毕

pool.shutdown(wait)  # ,所有任务执行完毕，阻塞函数
