# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec:
"""
from abc import abstractmethod, ABCMeta

from ObserverPattern.DisplayElement import DisplayElement
from ObserverPattern.Subject import WeatherData


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, subject, obj):
        """
        :param subject:
        :param obj: 任意数据对象
        :return:
        """
        pass


class Board1(Observer, DisplayElement):
    def __init__(self, sb):
        self.subject = sb
        self.subject.register_observer(self)
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 0.0

    def update(self, subject, obj):
        if isinstance(obj, WeatherData):
            self.__temperature = obj.get_temperature()
            self.__humidity = obj.get_humidity()
            self.__pressure = obj.get_pressure()
            self.display()
        else:
            self.__temperature, self.__humidity, self.__pressure = obj
            self.display()

    def display(self):
        print("board1: {} 温度， {} 湿度，{} 气压".format(self.__temperature, self.__humidity, self.__pressure))


class Board2(Observer, DisplayElement):
    def __init__(self, sb):
        self.subject = sb
        self.subject.register_observer(self)
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 0.0

    def update(self, subject, obj):
        if isinstance(obj, WeatherData):
            self.__temperature = obj.get_temperature()
            self.__humidity = obj.get_humidity()
            self.__pressure = obj.get_pressure()
            self.display()
        else:
            self.__temperature, self.__humidity, self.__pressure = obj
            self.display()

    def display(self):
        print("board2 : {} 温度， {} 湿度，{} 气压".format(self.__temperature, self.__humidity, self.__pressure))


if __name__ == '__main__':
    wd = WeatherData()
    b1 = Board1(wd)
    b2 = Board2(wd)
    wd.set_mesurements_changed(1, 2, 3)
    wd.set_mesurements_changed(11, 22, 33)
