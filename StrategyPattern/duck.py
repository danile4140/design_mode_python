# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec: 策略模式，多用组合，少用继承
"""
from abc import ABCMeta, abstractmethod

from StrategyPattern.fly_behavior import FlyWithWing, FlyNoWay
from StrategyPattern.quack_behavior import Quack, MuteQuack


class Duck(metaclass=ABCMeta):
    def __init__(self, flyparam, quackparam):
        self.fly_behavior = flyparam
        self.quack_behavior = quackparam

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    def swim(self):
        print("所有的鸭子都可以游泳，即使你是橡皮鸭子")

    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self, flyparam, quackparam):
        Duck.__init__(self, flyparam, quackparam)

    def display(self):
        print("this is a mallard duck")


class ModelDuck(Duck):
    def __init__(self, flyparam, quackparam):
        Duck.__init__(self, flyparam, quackparam)

    def display(self):
        print("this is a model duck")


if __name__ == '__main__':
    mallard_duck = MallardDuck(FlyWithWing(), Quack())
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    mallard_duck.swim()
    mallard_duck.display()

    model_duck = ModelDuck(FlyNoWay(), MuteQuack())
    model_duck.perform_fly()
    model_duck.perform_quack()
    model_duck.swim()
    model_duck.display()
    model_duck.set_fly_behavior(FlyWithWing())
    model_duck.perform_fly()
