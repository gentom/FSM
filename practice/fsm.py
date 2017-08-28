#!/usr/bin/env python
# coding: utf-8
import sys

class State:
    def __init__(self):
        print('Current State: {}'.format(str(self)))
    def onEvent(self, event):
        pass
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.__class__.__name__

class State1(State):
    def onEvent(self, event):
        if event == 'next':
            return State2()
        elif event == 'end':
            return END()
        return self

class State2(State):
    def onEvent(self, event):
        if event == 'next':
            return State1()
        elif event == 'end':
            return END()
        return self

class END(State):
    def onEvent(self, event):
        sys.exit()

class TestFSM:
    def __init__(self):
        self.state = State1()
    
    def onEvent(self, event):
        self.state = self.state.onEvent(event)

if __name__ == '__main__':
    fsm = TestFSM()
    events = ["next", "stay", "stay", "next", "stay", "next", "end", "next"]
    for event in events:
        fsm.onEvent(event)