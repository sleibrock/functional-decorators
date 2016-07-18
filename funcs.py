#!/usr/bin/env python
#-*- coding: utf-8 -*-

from operator import *
from math import *

# add1, adds 1 to a value (succ in Haskell)
def add1(x):
    return add(x, 1)

# sub1, sub 1 from a value (pred in Haskell)
def sub1(x):
    return sub(x, 1)

# Simple square
def square(x):
    return pow(x, 2)

# Simple cube
def cube(x):
    return pow(x, 3)

# Curry the pow() function to accept a value and return a new function
def power(x):
    return lambda p: pow(p, x)

# Head of a sequence
def head(x):
    return x[0]

# Tail of a sequence
def tail(x):
    return x[1:]

# Test if a function is even or odd
def even(x):
    return not x&1

def odd(x):
    return x&1

# end
