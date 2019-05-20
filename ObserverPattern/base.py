# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/15
    @dec: 
"""

from abc import ABCMeta, abstractmethod


class DisplayElement(metaclass=ABCMeta):
    """天气展示组件的基类"""

    @abstractmethod
    def display(self): pass


class Observer(metaclass=ABCMeta):
    """观察者接口"""

    @abstractmethod
    def update(self, subject, obj):
        """
        主题数据改变时调用
        :param subject: 传入是哪个主题改变了，用于注册了多个观察者的情况
        :param obj: 改变的值是啥
        :return: None
        """
        pass


class Subject(metaclass=ABCMeta):
    """
    主题接口，作为数据到提供者，对象使用此接口将自己注册为观察者，或者把自己从观察中删除
    """

    @abstractmethod
    def register_observer(self, ob):
        """
        注册成为观察者
        :param ob: observer对象的实例
        :return: None
        """
        pass

    @abstractmethod
    def remove_observer(self, ob):
        """
        移除观察者
        :param ob: observer对象的实例
        :return: None
        """
        pass

    def notify_observer_push(self):
        """
        主动push，通知所有观察者
        :return: None
        """
        pass

    def notify_observer_pull(self, obj):
        """
        被动pull，观察者自己取
        :param obj:
        :return: None
        """
        pass
