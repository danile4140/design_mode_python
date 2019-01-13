# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec:
"""
from abc import ABCMeta, abstractmethod


class IQuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Quack(IQuackBehavior):
    def quack(self):
        print("呱呱叫")


class MuteQuack(IQuackBehavior):
    def quack(self):
        print("silence")
