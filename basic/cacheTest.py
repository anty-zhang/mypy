# -*- coding: utf-8 -*-

import re
import time


# import collections
# import functools

# class memoized(object):
#   '''Decorator. Caches a function's return value each time it is called.
#   If called later with the same arguments, the cached value is returned
#   (not reevaluated).
#   '''
#   def __init__(self, func):
#      self.func = func
#      self.cache = {}
#   def __call__(self, *args):
#      if not isinstance(args, collections.Hashable):
#         # uncacheable. a list, for instance.
#         # better to not cache than blow up.
#         return self.func(*args)
#      if args in self.cache:
#         return self.cache[args]
#      else:
#         value = self.func(*args)
#         self.cache[args] = value
#         return value
#   def __repr__(self):
#      '''Return the function's docstring.'''
#      return self.func.__doc__
#   def __get__(self, obj, objtype):
#      '''Support instance methods.'''
#      return functools.partial(self.__call__, obj)

#    @memoized
#    def fibonacci(n):
#       "Return the nth fibonacci number."
#       if n in (0, 1):
#          return n
#       return fibonacci(n-1) + fibonacci(n-2)

#    print fibonacci(12)


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
        print '__init__'
        self.ttl = ttl

    def __call__(self, fget, doc=None):
        print '__call__ start==== fget:', fget, ', fget.__name__: ', fget.__name__
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        print '__call__ end===='
        return self

    def __get__(self, inst, owner):
        print '__get__   start', ', inst:', inst, ', owner:', owner
        now = time.time()
        try:
            value, last_update = inst._cache[self.__name__]
            if self.ttl > 0 and (now - last_update > self.ttl):
                print 'time out raise AttributeError'
                raise AttributeError
            print 'cache success'
        except (KeyError, AttributeError):
            print 'execpte self.fget: ', self.fget
            value = self.fget(inst)
            print 'value : ', value
            try:
                cache = inst._cache
                print 'try cache: ', cache
            except AttributeError:
                cache = inst._cache = {}
                print 'execpt cache: ', cache

            cache[self.__name__] = (value, now)
            print 'last cache: ', cache
        print '__get__   end'
        return value

    def test(self):
        print 'test'


class CacheTest(object):
    print 'CacheTest start'
    @cached_property(2)
    def all_regs(self):
        print '=======all_regs start========'
        ret = []
        """
        for obj in Regular.objects.all():
            ret.append( (obj.cate.pk, re.compile(obj.re)) )
        """
        ret.append((200, re.compile(r".*错误：\(-1200:\){1}")))
        print '=======all_regs end========'
        return ret

    def check(self, desc):
        # print self.all_regs
        self.all_regs
        """
        for obj in self.all_regs:
            if obj[1].match(desc):
                return obj[0]
            else:
                return 3
        """
    print 'CacheTest end'


if __name__ == '__main__':
    print '====main start======='
    v = CacheTest()
    print '-------------------------'
    v.check('sfsfs错误：(-1200:)sdfsdf')

    print '--------------------------------------'
    time.sleep(3)

    print v.check('sfsfs错误：(-1200:)sdfsdf')
    print '====main end======='


