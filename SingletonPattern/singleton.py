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
    instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        # 双重检查加锁，避免多线程异常
        if not hasattr(cls, "_instance"):
            with cls.instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls)
        return cls._instance


def SingleWrap(cls):
    _instance = {}
    instance_lock = threading.Lock()

    def _singleton(*args, **kargs):
        # 双重检查加锁，避免多线程异常
        if cls not in _instance:
            with instance_lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@SingleWrap
class A:
    a = 1

    def __init__(self, x=0):
        time.sleep(3)
        self.x = x


def task():
    obj = A()
    obj_1 = Singleton()
    print(obj)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task)
        t.start()
