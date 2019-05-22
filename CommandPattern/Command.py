# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/3/19
    @dec:
"""
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
