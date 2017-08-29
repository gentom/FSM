#!/usr/bin/env python
# coding: utf-8
def state1():
    print('State1: state1() is called')

def state2():
    print('State2: state2() is called')

def state3():
    print('State3: state3() is called')


states = ['state1','state2','state3']
t_matrix = [0.6,0.2,0.2]
sm = StateMachine(states,t_matrix)
for i in range(10):
    eval(sm.transitioner())()