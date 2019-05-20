# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/20
    @dec: 
"""
from MVC.Base import IBpmModel


class BpmModel(IBpmModel):

    def __init__(self) -> None:
        super().__init__()
        self.bpm_observers = []

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, value):
        self._bpm = value
        self.notify_bpm_observers()

    def on(self):
        self.bpm = 90

    def off(self):
        self.bpm = 0

    def initialize(self):
        pass

    def register_observer_by_bpm(self, ob):
        self.bpm_observers.append(ob)

    def remove_observer_by_bpm(self, ob):
        self.bpm_observers.remove(ob)

    def notify_bpm_observers(self):
        """通知所有观察者更新bpm"""
        for ob in self.bpm_observers:
            ob.update_bpm()
