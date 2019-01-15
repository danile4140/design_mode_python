# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/15
    @dec:
"""
from DecoratorPattern.Beverage import *


class CondimentDecorator(Beverage):

    @abstractmethod
    def get_description(self):
        pass


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage
        self.des = ["Mocha"]
        self.price = {"tall": .2, "grande": .3, "venti": .4}

    def get_description(self):
        return self.beverage.get_description() + self.des

    def cost(self):
        return self.price.get(self.beverage.capacity) + self.beverage.cost()


if __name__ == '__main__':
    bev1 = Espresso("grande")
    print(str(bev1.get_description()) + " $" + str(bev1.cost()))

    bev2 = DarkRoast("tall")
    bev2 = Mocha(bev2)
    print(str(bev2.get_description()) + " $" + str(bev2.cost()))
    bev3 = DarkRoast("venti")
    bev3 = Mocha(bev3)
    print(str(bev3.get_description()) + " $" + str(bev3.cost()))
