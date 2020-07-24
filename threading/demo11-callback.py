import requests
from concurrent.futures import ThreadPoolExecutor
import threading


def product_data(url):
    data = requests.get(url)
    return data.text, url


def parser_data(f):
    res = f.result()
    print(len(res[0]), res[1], "当前线程", threading.current_thread())


if __name__ == '__main__':
    urls = ['http://www.baidu.com', 'https://www.cnblogs.com/ywsun/', 'https://www.processon.com/']
    pool = ThreadPoolExecutor()
    for url in urls:
        f = pool.submit(product_data, url)
        f.add_done_callback(parser_data)
