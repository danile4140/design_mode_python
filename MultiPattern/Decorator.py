# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/12
    @dec: 为鸭子类添加quack的计数，通过装饰器
"""

quacks_num = 0


def count_quacks(aClass):
    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            global quacks_num
            if attrname == 'quack':
                quacks_num += 1
            return getattr(self.wrapped, attrname)

    return Wrapper
