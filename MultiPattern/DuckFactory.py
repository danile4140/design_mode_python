# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/12
    @dec: 鸭子工厂
"""
from MultiPattern.Base import AbstractDuckFactory, Quackable
from MultiPattern.Duck import *
from MultiPattern.Goose import Goose
from MultiPattern.GooseAdapter import GooseAdapter


class DuckFactory(AbstractDuckFactory):
    def create_mallarduck(self) -> Quackable:
        return MallardDuck()

    def create_redheadduck(self) -> Quackable:
        return RedheadDuck()

    def create_duckcall(self) -> Quackable:
        return DuckCall()

    def create_rubberduck(self) -> Quackable:
        return RedheadDuck()

    def create_gooseduck(self) -> Quackable:
        return GooseAdapter(Goose())
