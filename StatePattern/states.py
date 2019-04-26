# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/4/27
    @dec: 定义各种状态
"""
from StatePattern.base_state import State


class SoldOutState(State):
    """糖果售罄"""

    def insert_quarter(self):
        print("卖完了,不能投币了")

    def eject_quarter(self):
        print("你还没投币呢")

    def turn_crank(self):
        print("虽然你转了，但是没糖果了")

    def dispense(self):
        print("没有糖果可以给你了")


class NoQuarterState(State):
    """没有币"""

    def insert_quarter(self):
        print("你已投币")
        self.gumball_machine.state = self.gumball_machine.has_quarter

    def eject_quarter(self):
        print("你还没投币呢")

    def turn_crank(self):
        print("虽然你转了，但是你还没投币呢")

    def dispense(self):
        print("你还没投币呢，不能给你糖果")


class HasQuarterState(State):
    """有币"""

    def insert_quarter(self):
        print("你已经投过币了")

    def eject_quarter(self):
        print("好了，币退你")
        self.gumball_machine.state = self.gumball_machine.no_quarter

    def turn_crank(self):
        print("哗啦啦，拿糖果")
        self.gumball_machine.state = self.gumball_machine.sold

    def dispense(self):
        print("你还没转呢")


class SoldState(State):
    """已出售"""

    def insert_quarter(self):
        print("等等先啦，还在出货")

    def eject_quarter(self):
        print("你都转了，还想退钱？")

    def turn_crank(self):
        print("你已经转了，请耐心等候")

    def dispense(self):
        print("来，给你一个糖果")
        self.gumball_machine.count -= 1

        self.gumball_machine.state = self.gumball_machine.no_quarter if self.gumball_machine.count else \
            self.gumball_machine.sold_out
