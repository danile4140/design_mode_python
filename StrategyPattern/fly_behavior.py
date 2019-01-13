# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec:
"""
from abc import ABCMeta, abstractmethod


class IFlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWing(IFlyBehavior):
    def fly(self):
        print("fly with wing")


class FlyNoWay(IFlyBehavior):
    def fly(self):
        print("can't fly any more")
