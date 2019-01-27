# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/27
    @dec:
"""
import threading
import time


class Singleton:
    def __init__(self):
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        # 双重检查加锁，避免多线程异常
        if not hasattr(cls, "_instance"):
            with threading.Lock():
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls)
        return cls._instance


def task():
    obj = Singleton()
    print(obj)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task)
        t.start()
