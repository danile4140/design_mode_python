# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/13
    @dec: 组合模式
"""
from MultiPattern.Base import Quackable


class Flock(Quackable):
    """鸭子集群"""
    def __init__(self):
        self.quackers = []

    def add(self, quacker) -> None:
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def registerObserver(self, observer):
        for duck in self.quackers:
            duck.registerObserver(observer)

    def notifyObservers(self):
        for duck in self.quackers:
            duck.notifyObservers()

    def removeObserver(self, observer):
        for duck in self.quackers:
            duck.removeObserver(duck)
