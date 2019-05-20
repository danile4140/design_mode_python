# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/21
    @dec: 
"""
from MVC.Base import IController
from MVC.Views import DJView


class BpmController(IController):

    def __init__(self, model):
        self.model = model
        self.view = DJView(self, model)
        self.view.create_view()

    def start(self):
        self.model.on()

    def stop(self):
        self.model.off()
        self.view.disable_view()

    def increase_bpm(self):
        self.model.bpm += 1

    def decrease_bpm(self):
        self.model.bpm -= 1

    def set_bpm(self, value):
        self.model.bpm = value
