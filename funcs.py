#!/usr/bin/env python
#-*- coding: utf-8 -*-

from operator import *
from math import *

def log_value(x):
    print("Current value is: {}".format(x))
    return x

def add1(x):
    return add(x, 1)

def sub1(x):
    return sub(x, 1)

def square(x):
    return pow(x, 2)

def cube(x):
    return pow(x, 3)

def power(x):
    return lambda p: pow(p, x)

def head(x):
    return x[0]

def tail(x):
    return x[1:]


