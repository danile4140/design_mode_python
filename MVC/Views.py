# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/21
    @dec: 
"""
from MVC.Base import IBpmObserver


class DJView(IBpmObserver):

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        self.model.register_observer_by_bpm(self)

    def update_bpm(self):
        self.bpm = self.model.bpm

        if self.bpm:
            print("current bpm: {}".format(self.bpm))
        else:
            print("offline")

    def create_view(self):
        print("create views")

    def disable_view(self):
        print("disable views")
