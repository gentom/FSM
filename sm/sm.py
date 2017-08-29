#!/usr/bin/env python
# coding: utf-8
from random import randint, random, choice

# Finite State Machine. Work In Progress.

class StateMachine:
    def __init__(self, states, t_matrix):
        self.states = states
        self.t_matrix = t_matrix
    
    def transitioner(self):
        return self.choose_with_w(self.states, self.t_matrix)
    
    def choose_with_w(self, states, weights):
        weights = [sum(weights[:x+1]) for x in range(len(weights))]
        if weights[-1] > 1.0:
            weights = [x/weights[-1] for x in weights]
        rand = random()
        for state, weight in zip(states, weights):
            if rand < weight:
                return state
        return None

if __name__ == '__main__':
    states = ['state1','state2','state3']
    t_matrix = [0.6,0.2,0.2]
    sm = StateMachine(states,t_matrix)
    for i in range(10):
        print(sm.transitioner())