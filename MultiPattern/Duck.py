# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/12
    @dec: 
"""
from MultiPattern.Base import Quackable
from MultiPattern.Decorator import count_quacks
from MultiPattern.Observable import Observable


@count_quacks
class MallardDuck(Quackable):
    """绿头鸭"""

    def __init__(self):
        self.observable = Observable(self)

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def removeObserver(self, observer):
        self.observers.remvoe(observer)

    def quack(self):
        print("Quack")
        self.notifyObservers()


@count_quacks
class RedheadDuck(Quackable):
    """红头鸭"""
    def __init__(self):
        self.observable = Observable(self)

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def quack(self):
        print("Quack")
        self.notifyObservers()




@count_quacks
class DuckCall(Quackable):
    """鸭鸣器"""
    def __init__(self):
        self.observable = Observable(self)

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def quack(self):
        print("Kwak")
        self.notifyObservers()

@count_quacks
class RubberDuck(Quackable):
    """橡皮鸭"""
    def __init__(self):
        self.observable = Observable(self)

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def quack(self):
        print("Squeak")
        self.notifyObservers()