# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/4/26
    @dec: 定义状态的基类
"""
from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    @abstractmethod
    def insert_quarter(self):
        """投币行为"""
        pass

    @abstractmethod
    def eject_quarter(self):
        """退币"""
        pass

    @abstractmethod
    def turn_crank(self):
        """转动曲柄"""
        pass

    @abstractmethod
    def dispense(self):
        """发放糖果"""
        pass
