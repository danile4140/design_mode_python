# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/16
    @dec:
"""
from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):
    def __init__(self):
        self.name = "unknown"
        self.dough = "unknown"
        self.sauce = "unknown"
        self.toopings = []

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("bake for 25~50 min")

    def cut(self):
        print("cutting into diagonal slices")

    def box(self):
        print("place pizza in official pizza store box")


class NYStylePizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self)
        self.ingredient_factory = ingredient_factory
        self.name = "NY style Sauce and Cheese Pizza"
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.toopings= self.ingredient_factory.create_veggies()

    def prepare(self):
        print("prepare %s" % self.name)
        print("Tossing dough %s" % self.dough)
        print("Adding sauce %s" % self.sauce)
        print("adding topping %s " % "  ".join(self.toopings))

    def cut(self):
        print("this NYStylePizza special cut")

