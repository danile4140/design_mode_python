# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/12
    @dec: 
"""
from MultiPattern.Base import Quackable
from MultiPattern.Observable import Observable


class GooseAdapter(Quackable):
    """鹅的适配器，将鹅适配成鸭子"""

    def __init__(self, goose):
        self.goose = goose
        self.observable = Observable(self)

    def quack(self):
        # 这里调用quack，会委托为goose的honk方法
        self.goose.honk()
        self.notifyObservers()

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()
