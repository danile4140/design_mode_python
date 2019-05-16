# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec: 布告板
"""
from ObserverPattern.Subject import WeatherData
from ObserverPattern.base import Observer, DisplayElement


class Board1(Observer, DisplayElement):
    def __init__(self, sb):
        self.subject = sb
        self.subject.register_observer(self)
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 0.0

    def update(self, subject, obj):
        """更新观察者"""
        if isinstance(subject, WeatherData):
            self.__temperature = subject.get_temperature()
            self.__humidity = subject.get_humidity()
            self.__pressure = subject.get_pressure()
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
        if isinstance(subject, WeatherData):
            self.__temperature = subject.get_temperature()
            self.__humidity = subject.get_humidity()
            self.__pressure = subject.get_pressure()
            self.display()

    def display(self):
        print("board2 : {} 温度， {} 湿度，{} 气压".format(self.__temperature, self.__humidity, self.__pressure))



