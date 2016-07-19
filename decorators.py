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
        data = f(x)
        print("Current state is {}".format(data))
        return data 
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

# Create a list using range(x)
def _range(f):
    return craft(f)(range)

# Creates a range of nums from x to y inclusive
def _to(y):
    def wrap(f):
        def inner(x):
            return range(f(x), y+1)
        return inner
    return wrap

# Enumerate a list of items [(0,a), (1,b), ...]
def _enum(f):
    return craft(f)(enumerate)

# Apply an any() to the object
def _any(f):
    return craft(f)(any)

# Apply an all() to the object
def _all(f):
    return craft(f)(all)

# Apply a list function to the result (useful for Python3)
# Functions in Py3 return generators as opposed to raw lists
def _list(f):
    return craft(f)(list)

# Functor mapping - only functor is List thus far
def _fmap(func):
    def wrap(f):
        def inner(x):
            return list(map(func, f(x)))
        return inner
    return wrap

# Filter - apply a filter over an iterable
def _filter(func):
    def wrap(f):
        def inner(x):
            return list(filter(func, f(x)))
        return inner
    return wrap

# Fold-left over an iterable of items
# Should only work when a list contains only one type
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
