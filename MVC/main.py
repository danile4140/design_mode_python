# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/21
    @dec: 
"""
from MVC.BpmModel import BpmModel
from MVC.Controller import BpmController

if __name__ == '__main__':
    model = BpmModel()
    controller = BpmController(model)
    controller.start()
    controller.increase_bpm()
    controller.decrease_bpm()
    controller.decrease_bpm()
    controller.set_bpm(100)
    controller.stop()
