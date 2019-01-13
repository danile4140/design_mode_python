# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec: 展示组件
"""
from abc import ABCMeta, abstractmethod


class DisplayElement(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass