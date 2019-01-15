# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/15
    @dec:
"""
from abc import ABCMeta, abstractmethod

from DecoratorPattern.Decorator import Mocha


class Beverage(metaclass=ABCMeta):
    def __init__(self, capacity, des="unknown beverage"):
        self.__description = [des]
        self.capacity = capacity

    def get_description(self):
        return self.__description

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):

    def __init__(self, capacity):
        Beverage.__init__(self, capacity, "HouseBlend")

    def cost(self):
        return .89


class DarkRoast(Beverage):
    def __init__(self, capacity):
        Beverage.__init__(self, capacity, "DarkRoast")

    def cost(self):
        return 1.89


class Decaf(Beverage):
    def __init__(self, capacity):
        Beverage.__init__(self, capacity, "Decaf")

    def cost(self):
        return 2.89

class Espresso(Beverage):
    def __init__(self, capacity):
        Beverage.__init__(self, capacity, "Espresso")

    def cost(self):
        return 3.89
