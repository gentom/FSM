#!/usr/bin/env python
# coding: utf-8
from random import randint, random, choice

# Finite State Machine. Work In Progress.

class State:
    def __init__(self, state):
        self.state = state


class Machine():
    def __init__(self, states):
        self.states = states
        self.state_num = len(states)
        self.current_state = states[0]

    def get_current(self):
        return self.current_state

    def simulator(self):
        pass

    def state_changer(self, trigger):
        pass