# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/16
    @dec: 利用MVC控制节拍
"""
from abc import ABCMeta, abstractmethod


class IBpmModel(metaclass=ABCMeta):
    """管理节拍"""

    def __init__(self):
        self._bpm = 0

    @abstractmethod
    def on(self):
        """开启节拍"""
        pass

    @abstractmethod
    def off(self):
        """关闭节拍"""
        pass

    @abstractmethod
    def initialize(self):
        """初始化"""
        pass

    @abstractmethod
    def register_observer_by_bpm(self, ob):
        """注册观察者，每次bpm变化都通知"""
        pass

    @abstractmethod
    def remove_observer_by_bpm(self, ob): pass


class IBpmObserver(metaclass=ABCMeta):
    """bpm 观察者"""

    @abstractmethod
    def update_bpm(self): pass


class IController(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def increase_bpm(self):
        pass

    @abstractmethod
    def decrease_bpm(self):
        pass

    @abstractmethod
    def set_bpm(self, value):
        pass
