# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/1/13
    @dec:
"""
from ObserverPattern.base import Subject


class WeatherData(Subject):
    """气象数据类，数据提供者，继承主题类"""

    def __init__(self):
        self.__observer_list = []
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 0.0
        self.__changed = False

    def register_observer(self, ob):
        self.__observer_list.append(ob)

    def remove_observer(self, ob):
        self.__observer_list.remove(ob)

    def notify_observer_push(self):
        print("push")
        if self.__changed:
            for ob in self.__observer_list:
                ob.update(self, (self.__temperature, self.__humidity, self.__pressure))
            self.__changed = False

    def notify_observer_pull(self, obj):
        """带参数，表示由观察者自己来取数据"""
        print("pull")
        if self.__changed:
            for ob in self.__observer_list:
                ob.update(self, obj)
            self.__changed = False

    def set_changed(self):
        """设置当前的更新状态，主要用于通知控制"""
        self.__changed = True

    def measurements_changed(self):
        """数据改变时触发"""
        self.set_changed()
        self.notify_observer_push()

    def set_measurements_changed(self, *args):
        self.__temperature, self.__humidity, self.__pressure = args
        self.measurements_changed()

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

    def get_pressure(self):
        return self.__pressure
