# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec:
"""
from StrategyPattern.quack_behavior import *


class DuckCall:
    def __init__(self, quackparam):
        self.quack_behavior = quackparam

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb


if __name__ == '__main__':
    dc = DuckCall(Quack())
    dc.perform_quack()

    dc.set_quack_behavior(MuteQuack())
    dc.perform_quack()
