# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/16
    @dec:
"""
from abc import ABCMeta, abstractmethod

from FactoryPattern.IngredientFactory import NYPizzaIngredientFactory
from FactoryPattern.Pizza import NYStylePizza


class PizzaStore(metaclass=ABCMeta):

    def order_pizza(self, pizza_type):
        pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def _create_pizza(self, pizza_type):
        pass


class NYPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type):
        pizza = None
        ingredient = NYPizzaIngredientFactory()
        if pizza_type == "cheese":
            pizza = NYStylePizza(ingredient)
        elif pizza_type == "":
            pass
        else:
            pass
        return pizza


class ChicagoStypePizzastore(PizzaStore):
    def _create_pizza(self, pizza_type):
        pass


if __name__ == '__main__':
    store = NYPizzaStore()
    store.order_pizza("cheese")