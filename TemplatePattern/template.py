# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/4/21
    @dec: 
"""
from abc import ABCMeta, abstractmethod


class TemplateBase(metaclass=ABCMeta):

    @abstractmethod
    def method1(self): pass

    @abstractmethod
    def method2(self): pass

    def __method3(self):
        print("method3...")

    def template_method(self):
        self.method1()
        self.method2()
        if self.method_hook():
            self.__method3()

    def method_hook(self): return True


class T1(TemplateBase):
    def method1(self):
        print("method1...")

    def method2(self):
        print("method2...")

    def method_hook(self):
        return False


if __name__ == '__main__':
    t1 = T1()
    t1.template_method()
