#!/usr/bin/env python
# coding: utf-8
import sys
import os
sys.path.append(os.pardir)
from sm import sm
import my_states

'''
def state1():
    print('State1: state1() is called')

def state2():
    print('State2: state2() is called')

def state3():
    print('State3: state3() is called')
'''

states = ['my_states.state1','my_states.state2','my_states.state3']
t_matrix = [0.6,0.2,0.2]
sm = sm.StateMachine(states, t_matrix)
for i in range(10):
    eval(sm.transitioner())()