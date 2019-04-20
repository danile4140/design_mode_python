# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/4/20
    @dec:
"""
from abc import abstractmethod, ABCMeta


class Duck(metaclass=ABCMeta):

    @abstractmethod
    def quack(self): pass

    @abstractmethod
    def fly(self): pass


class Turkey(metaclass=ABCMeta):

    @abstractmethod
    def gobble(self): pass

    @abstractmethod
    def fly(self): pass


class MallardDuck(Duck):
    def quack(self):
        print("quack...")

    def fly(self):
        print("fly 5h...")


class WildTurkey(Turkey):
    def gobble(self):
        print("gobble...")

    def fly(self):
        print("fly 1h...")


class TurkeyAdapter(Duck):
    """这是火鸡适配器，用来使用Duck的方法"""

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


if __name__ == '__main__':
    turkey = WildTurkey()
    ta = TurkeyAdapter(turkey)
    ta.quack()
    ta.fly()
