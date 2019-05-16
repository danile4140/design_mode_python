# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/14
    @dec: 
"""
from MultiPattern.Base import QuackObserveable, Observer


class Observable(QuackObserveable):
    """主题类"""

    def __init__(self, duck):
        self.observers = []
        self.duck = duck

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for ob in self.observers:
            ob.update(self.duck)

    def removeObserver(self, observer):
        self.observers.remove(observer)
