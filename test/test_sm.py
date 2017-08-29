#!/usr/bin/env python
# coding: utf-8
import sys
import os
sys.path.append(os.pardir)
from sm import sm
import my_states

states = ['my_states.state1','my_states.state2','my_states.state3']
t_matrix = [0.6,0.2,0.2]
sm = sm.StateMachine(states, t_matrix)
for i in range(10):
    eval(sm.transitioner())()