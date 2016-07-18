Functional Decorators
=====================

Writing code is overrated - decorators is the new code.

# What is Functional Decorators?

Functional Decorators is a project based on the concept of decorators in Python.
A wrapper is a function that accepts a function and returns a new function that
performs a task around the given function. Python has syntax to easily craft new
functions from old ones via the syntax of

``` python
@decorator_function
def my_function(x):
    # code goes here
    ...
```

You've probably used it to route paths in web frameworks or some other kind of
function manipulation. But what if instead of writing code, we wrote code that
generated a function for us?

``` python
@_foldl(add)
@_fmap(cube)
@_range
def fold_cubes(x): return x
```

Looks like a real dumb function definition. But guess what - it does exactly what
the decorators say! It applies a _foldl_ of the built-in _add_ function, over a
list of numbers with the function _cube_ applied to each number.

How does one run this? Simply call it afterwards!

```
>>> fold_cubes(100)
24502500.0
```

Neat, right? We really didn't do anything at all to create this function.

# The Downside

You have to right it in an order *backwards* of what you want to do. Naturally
the function we wrote, we would have verbally said "create a list of numbers, 
apply a function to them, and sum them up". However the decorator defintion is
completely the opposite. It's "Add up a list of numbers that have an operation 
mapped over them".

So the order that which we write these functions may be considered confusing at
first, but it's not as bad as you might think initially. The formal definition
of this code block would have looked like:

```
def fold_cubes(x):
    return sum([cube(x) for z in range(x)])
```

Obviously easier to write, but the modularity of it is glued in place. We can't
take functions apart and put them in other places like we can with these decorators.
In the Functional Decorators, we layer decorators slowly on top of eachother to
compose new functions without having to do much work at all. This is akin to
writing point-free expressions in functional languages like Haskell where the
variables aren't important, but the functions we compose are.

Note that the function definition at the bottom of the decorator chain isn't
very important. So long as it returns x, it will do as the decorators say.
But you can modify the bottom function to execute one last expression in the chain,
so you can do whatever the heck you want with it! But mostly it's just there so you
can name the final product function.

# Should I ever use this?

Bottom-line answer: *NO*. But if you want to have some fun, yes!

# Give me something crazy

Okay, here's a function that will return to you a sum of the list of absolute
values of a function sin(x**2) where x is a radian-value converted from
degrees.

``` python
@_foldl(add)
@_fmap(abs)
@_fmap(sin)
@_fmap(square)
@_fmap(radians)
@_range
def something(x): return x
```

Let's test it just to make sure it works.

```
>>> something(360)
215.36402018499368
```

Let's prove it works just to be sure.

```
>>> x = range(360)
>>> rads = map(radians, x)
>>> sqs = map(square, rads)
>>> sins = map(sin, sqs)
>>> abss = map(abs, sins)
>>> sum(abss)
215.36402018499368
```

Seems to work! The only downside is that we did several maps of individual
functions where we can possibly just compose them all together into one big
function. Unfortunately the list comprehension just looks a little bit worse for
wear...

```
def something(x):
    return sum([abs(sin(square(radians(z)))) for z in range(x)])
```

# Closing Remarks

This was a project inspired by functional programming, and since Python is trying
it's hardest *not* to be a functional language by any means, I thought I would
adhere to Python rules and try something unconventional. It's funny to write an
entire function without actually writing any meaningful code _inside_ the function
definition. But the performance surely takes a hit when not using list comps
due to CPython's list comp internals.

