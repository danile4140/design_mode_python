# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/3/19
    @dec:
"""
from typing import Iterable

from CommandPattern.Command import Command


class GarageDoor:
    def up(self):
        print('garage up')

    def down(self):
        print('garage down')

    def stop(self):
        print("stop")

    def light_on(self):
        print("light on")

    def light_off(self):
        print(__name__)


class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door) -> None:
        super().__init__()
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorLightOnCommand(Command):
    def __init__(self, garage_door) -> None:
        super().__init__()
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.light_on()

    def undo(self):
        self.garage_door.light_off()


