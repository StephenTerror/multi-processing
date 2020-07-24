from concurrent.futures import ThreadPoolExecutor
import time


def task(num):
    time.sleep(0.5)
    print("%s is running....." % num)
    return num ** 2


pool = ThreadPoolExecutor()
ress = []
for i in range(10):
    res = pool.submit(task, i)
    ress.append(res)

pool.shutdown(wait=False)

for i in ress:
    print(i.result())

print('over')
