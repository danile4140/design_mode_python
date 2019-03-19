# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/3/19
    @dec:
"""
from CommandPattern.GarageDoorCommand import GarageDoorOpenCommand, GarageDoor, GarageDoorLightOnCommand
from CommandPattern.LightCommand import LightOnCommand, Light


class SimpleRemoteControl:
    def __init__(self):
        self.slot = None

    def set_command(self, cmd):
        self.slot = cmd

    def button_pressed(self):
        self.slot.execute()


if __name__ == '__main__':
    src = SimpleRemoteControl()
    src.set_command(LightOnCommand(Light()))
    src.button_pressed()

    src.set_command(GarageDoorOpenCommand(GarageDoor()))
    src.button_pressed()

    src.set_command(GarageDoorLightOnCommand(GarageDoor()))
    src.button_pressed()