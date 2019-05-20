# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/15
    @dec: 
"""
from ObserverPattern.board_observer import *

if __name__ == '__main__':
    wd = WeatherData()
    b1 = Board1(wd)
    b2 = Board2(wd)
    wd.set_measurements_changed(1, 2, 3)
    wd.set_measurements_changed(11, 22, 33.5)