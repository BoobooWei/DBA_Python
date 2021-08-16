# -*- coding:UTF-8 -*-
# 批量执行

import threading
import time


def job(i):
    print(i)


def single_thread():
    print("single_thread begin")
    for i in range(10):
        job(i)
    print("single_thread end")


def multi_thread():
    print("multi_thread begin")
    threads = []
    for i in range(10):
        threads.append(
            threading.Thread(target=job, args=(i,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread end")


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")
