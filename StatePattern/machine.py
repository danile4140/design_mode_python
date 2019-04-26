# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/4/27
    @dec: 定义糖果机
"""
from StatePattern.states import *


class GumballMachine:

    def __init__(self, gumball_num) -> None:
        self.count = gumball_num
        self.sold_out = SoldOutState(self)
        self.no_quarter = NoQuarterState(self)
        self.has_quarter = HasQuarterState(self)
        self.sold = SoldState(self)
        self.state = self.no_quarter if self.count else self.sold_out

    def insert_quarter(self):
        """投币"""
        self.state.insert_quarter()

    def eject_quarter(self):
        """退币"""
        self.state.eject_quarter()

    def turn_crank(self):
        """转"""
        self.state.turn_crank()

    def dispense(self):
        """发糖果"""
        self.state.dispense()


if __name__ == '__main__':
    gum = GumballMachine(2)
    gum.dispense()
    gum.turn_crank()
    gum.insert_quarter()
    gum.turn_crank()
    gum.dispense()
    gum.insert_quarter()
    gum.eject_quarter()
    gum.dispense()
    gum.insert_quarter()
    gum.dispense()
    gum.insert_quarter()
    gum.turn_crank()
    gum.insert_quarter()
    gum.dispense()
    gum.insert_quarter()