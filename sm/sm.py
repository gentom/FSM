#!/usr/bin/env python
# coding: utf-8
from random import randint, random, choice

# Finite State Machine. Work In Progress.

class StateMachine:
    def __init__(self, states, t_matrix, step):
        self.states = states
        self.state_num = len(states)
        self.current_state = states[0]
        self.t_matrix = t_matrix
        self.step = step

    def get_current(self):
        return self.current_state
    
    def transitioner(self):
        pass
    
    def choose_with_w(self, states, weights):
        weights = [sum(weights[:x+1]) for x in range(len(weights))]
        if weights[-1] > 1.0:
            weights = [x/weights[-1] for x in weights]
        rand = random()
        for state, weight in zip(states, weights):
            if rand < weight:
                return state
        return None