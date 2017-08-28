#!/usr/bin/env python
# coding: utf-8
from random import randint, random, choice

# Finite State Machine. Work In Progress.
class FSM():
    def __init__(self, state):
        self.state = state
        self.state_num = len(state)
        self.current_state = state[0]

    def get_current(self):
        return self.current_state

    def simulator(self):
        pass

    def state_changer(self, trigger):
        pass