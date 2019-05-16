# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/16
    @dec: 
"""
from MultiPattern.Base import Observer


class Quackologist(Observer):
    """观察者"""

    def update(self, duck):
        print("Quackologist: " + duck.__class__.__name__ + " just quacked")
