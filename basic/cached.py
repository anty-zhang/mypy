# -*- coding: utf-8 -*-

import time

import collections
import functools


class cached(object):
    """Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    """
    def __init__(self, func):
        print 'init dir(func): ', dir(func)
        print "enter init func: ", func
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        print "enter call func args: ", args
        print "collections hashable: ", collections.Hashable
        print "enter call cache: ", self.cache
        key = self.func.func_name
        for g in args:
            key += g

        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            # return self.func(*args)
            return self.func(key)
        if key in self.cache:
            return self.cache[key]
        else:
            value = self.func(*args)
            print 'enter call value: ', value, ', args: ', args
            self.cache[key] = value
            return value

    def __repr__(self):
        """Return the function's docstring."""
        print 'enter repr func doc: ', self.func.__doc__
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        print "enter get obj: ", obj, " , objtype: ", objtype
        print "functools partial: ", functools.partial(self.__call__, obj)
        return functools.partial(self.__call__, obj)
 

def test_cached():
    """
    >>> test_cached()
    """
    g_ = 1
    args_ = "zhangsanbeijing"
    print "-----------------1------------------"
    @cached
    def foo():
        return g_

    @cached
    def foo1(name, city):
        return args_
        # return name + city

    print "-----------------2------------------"
    assert foo() == 1
    print "-----------------3------------------"
    assert foo() == 1
    print "-----------------4------------------"
    g_ += 1
    assert foo() == 1
    print "-----------------5------------------"

    assert foo1("zhangsan", "beijing") == "zhangsanbeijing"
    assert foo1("zhangsan", "beijing") == "zhangsanbeijing"
    args_ = "lisibeijing"
    assert foo1("zhangsan", "beijing") == "zhangsanbeijing"
    print foo1("zhangsan", "beijing")
    # assert foo1("zhangsan", "beijing") == "zhangsanbeijing1"


class cached_ttl(object):
    """
    """
    def __init__(self, ttl=300):
        self.ttl = ttl
        self.cache = {}

    def __call__(self, f):
        def wrapped_f(*args):
            now = time.time()
            
            try:
                value, last_update = self.cache[f.__name__]
                if self.ttl > 0 and now - last_update > self.ttl:
                    raise KeyError
            except KeyError:
                value = f(*args)
                self.cache[f.__name__] = (value, now)
            return value

        return wrapped_f

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

def test_cached_ttl():
    """
    >>> test_cached_ttl()
    """
    g_ = 1

    @cached_ttl(1)
    def foo():
        return g_

    assert foo() == 1
    assert foo() == 1
    g_ += 1
    assert foo() == 1
    time.sleep(1)
    assert foo() == 2
    assert foo() == 2


class cached_property(object):
    """Decorator for read-only properties evaluated only once within TTL period.

    It can be used to created a cached property like this::

       import random

       # the class containing the property must be a new-style class
       class MyClass(object):
           # create property whose value is cached for ten minutes
           @cached_property(ttl=600)
           def randint(self):
               # will only be evaluated every 10 min. at maximum.
               return random.randint(0, 100)

    The value is cached  in the '_cache' attribute of the object instance that
    has the property getter method wrapped by this decorator. The '_cache'
    attribute value is a dictionary which has a key for every property of the
    object which is wrapped by this decorator. Each entry in the cache is
    created only when the property is accessed for the first time and is a
    two-element tuple with the last computed property value and the last time
    it was updated in seconds since the epoch.

    The default time-to-live (TTL) is 300 seconds (5 minutes). Set the TTL to
    zero for the cached value to never expire.

    To expire a cached property value manually just do::

       del instance._cache[<property name>]

    """
    def __init__(self, ttl=300):
        self.ttl = ttl

    def __call__(self, fget, doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        return self

    def __get__(self, inst, owner):
        now = time.time()
        try:
           value, last_update = inst._cache[self.__name__]
           if self.ttl > 0 and now - last_update > self.ttl:
               raise AttributeError
        except (KeyError, AttributeError):
           value = self.fget(inst)
           try:
               cache = inst._cache
           except AttributeError:
               cache = inst._cache = {}
           cache[self.__name__] = (value, now)
        return value



def test_cached_property():
    """
    >>> test_cached_ttl()
    """
    g_ = 1

    class foo():
        @cached_property(1)
        def bar(self):
            return g_

    tf = foo()

    assert tf.bar == 1
    assert tf.bar == 1
    g_ += 1
    assert tf.bar == 1
    time.sleep(1)
    assert tf.bar == 2
    assert tf.bar == 2


if __name__ == '__main__':
    test_cached()