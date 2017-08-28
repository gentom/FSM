#!/usr/bin/env python
# coding: utf-8
import sys

# For learning Finite State Machine.
def Start():
    return State0

def State0(event):
    if event == "next":
        return State1
    elif event == "previous":
        return State2
    elif event == "end":
        return END
    else:
        return State0

def State1(event):
    if event == "next":
        return State2
    elif event == "previous":
        return State0
    elif event == "end":
        return END
    else:
        return State1

def State2(event):
    if event == "next":
        return State0
    elif event == "previous":
        return State1
    elif event == "end":
        return END
    else:
        return State2

def END():
    sys.exit()


state = Start()
events = ["stay", "next", "previous", "next", "next", "stay", "stay", "next", "end"]
for event in events:
    print(event, ">>>", state)
    state = state(event)