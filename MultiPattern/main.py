# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/12
    @dec: 
"""
from MultiPattern import Decorator
from MultiPattern.Duck import *
from MultiPattern.DuckFactory import DuckFactory
from MultiPattern.Flock import Flock
from MultiPattern.Goose import Goose
from MultiPattern.GooseAdapter import GooseAdapter
from MultiPattern.Observer import Quackologist


class DuckSimulator:

    def simulate(self, duck_factory):
        redhead_duck = duck_factory.create_redheadduck()
        duck_call = duck_factory.create_duckcall()
        rubber_duck = duck_factory.create_rubberduck()
        goose_duck = duck_factory.create_gooseduck()

        flock_ducks = Flock()
        flock_ducks.add(redhead_duck)
        flock_ducks.add(duck_call)
        flock_ducks.add(rubber_duck)
        flock_ducks.add(goose_duck)

        mallard_duck_one = duck_factory.create_mallarduck()
        mallard_duck_two = duck_factory.create_mallarduck()
        mallard_duck_three = duck_factory.create_mallarduck()
        mallard_duck_four = duck_factory.create_mallarduck()

        flock_mallardducks = Flock()
        flock_mallardducks.add(mallard_duck_one)
        flock_mallardducks.add(mallard_duck_two)
        flock_mallardducks.add(mallard_duck_three)
        flock_mallardducks.add(mallard_duck_four)
        #
        flock_ducks.add(flock_mallardducks)
        print('\nDuck Simulator: With Observer')
        quackologist = Quackologist()
        flock_ducks.registerObserver(quackologist)
        self.simulate_quack(flock_ducks)
        # self.simulate_quack(mallard_duck)
        # self.simulate_quack(readhead_duck)
        # self.simulate_quack(duck_call)
        # self.simulate_quack(rubber_duck)
        # self.simulate_quack(goose_duck)
        # self.simulate_quack(flock_mallardducks)
        print("鸭子叫了%d次" % Decorator.quacks_num)
        # self.simulate_quack(flock_ducks)

    def simulate_quack(self, duck):
        duck.quack()


if __name__ == '__main__':
    simulator = DuckSimulator()
    simulator.simulate(DuckFactory())
