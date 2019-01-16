# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/16
    @dec:
"""
from abc import ABCMeta


class Dough(metaclass=ABCMeta):
    def __init__(self):
        self.dough = "unknow"


class ThinCrustDough(Dough):
    def __init__(self):
        Dough.__init__(self)
        self.dough = "ThinCrustDough"