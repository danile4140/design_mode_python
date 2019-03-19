# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2019/3/20
    @dec:
"""
from CommandPattern.Command import Command


class MacroCommand(Command):
    def __init__(self, commands) -> None:
        self.commands = []

    def execute(self):
        for i in self.commands:
            i.execute()

    def undo(self):
        for i in self.commands:
            i.undo()
