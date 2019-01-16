# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/16
    @dec:
"""
from abc import ABCMeta, abstractmethod

from FactoryPattern.Dough import ThinCrustDough


class PizzaIngredientFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough().dough

    def create_sauce(self):
        return "sauce"

    def create_cheese(self):
        return "cheese"

    def create_veggies(self):
        return ["veggies"]

    def create_clam(self):
        return "clam"
