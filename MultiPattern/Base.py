# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/12
    @dec: 
"""
from abc import abstractmethod, ABCMeta


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, duck): pass


class QuackObserveable(metaclass=ABCMeta):
    """主题类"""

    @abstractmethod
    def registerObserver(self, observer): pass

    @abstractmethod
    def notifyObservers(self): pass

    # @abstractmethod
    def removeObserver(self, observer): pass

    def notifyTheObserver(self, observer): pass


class Quackable(QuackObserveable, metaclass=ABCMeta):
    """鸭子叫基类"""

    @abstractmethod
    def quack(self) -> None: pass


class AbstractDuckFactory(metaclass=ABCMeta):
    """鸭子工厂基类"""

    @abstractmethod
    def create_mallarduck(self) -> Quackable: pass

    @abstractmethod
    def create_redheadduck(self) -> Quackable: pass

    @abstractmethod
    def create_duckcall(self) -> Quackable: pass

    @abstractmethod
    def create_rubberduck(self) -> Quackable: pass

    @abstractmethod
    def create_gooseduck(self) -> Quackable: pass
