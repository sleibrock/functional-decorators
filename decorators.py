#!/usr/bin/env python
#-*- coding: utf-8 -*-

from funcs import *

# Create an anonymous function applying the function given
# Curry it so we can take in the current state and wrap it
# around the function taken in
def craft(fun):
    return lambda s: lambda x: s(fun(x))

# Classic ID function
def _id(f):
    return craft(f)(lambda x: x)

# Logging function to output the current state
# Note that if functions have multiple logs in
# their chains, we will get weird-looking log messages
def _puts(f):
    def inner(x):
        print("Current state is {}".format(f(x)))
        return f(x)
    return inner

# Numeric functions (add1/sub1 from racket)
def _add1(f):
    return craft(f)(add1)

def _sub1(f):
    return craft(f)(sub1)

# Head and tail of lists
def _head(f):
    return craft(f)(head)

def _tail(f):
    return craft(f)(tail)

# Functor mapping - only functor is List thus far
def _fmap(func):
    def wrap(f):
        def inner(x):
            return map(func, f(x))
        return inner
    return wrap

# Create a list using range(x)
def _range(f):
    return craft(f)(range)

# Fold-left over an iterable of items
def _foldl(func):
    def wrap(f):
        def inner(x):
            res = f(x) # store the results so we don't apply f twice
            z = head(res)
            for y in tail(res):
                z = func(z, y)
            return z
        return inner
    return wrap

# end
