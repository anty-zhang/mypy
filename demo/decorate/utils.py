# -*- coding: utf8 -*-
from functools import wraps
import uuid
import time
import logging


logger = logging.getLogger(__name__)


def get_merge_order_id():
    return hex(uuid.uuid4().time)[2:-1]


def jsonify(fn):
    """json化"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        rv = fn(*args, **kwargs)
        safe = True if isinstance(rv, dict) else False
        # return JsonResponse(rv, safe=safe, encoder=OBJEncoder)
    return wrapper


class lockit:
    """
        类lockit中__enter__ 和__exit__是为了配合with来使用
    """
    def __init__(self, cache, key, expire):
        self._cache = cache
        self._key = key
        self._expire = expire

    def __enter__(self):  
        # return not self._cache.add(self._key, 1, self._expire)
        print "__enter__"
        return "__enter__"

    def __exit__(self, *args):  
        # return self._cache.delete(self._key)
        print "__exit__"
        return "__exit__"

def cached_result(key_func, timeout, prevent_snowslide=True):
    print '===1===', key_func, timeout, prevent_snowslide

    def wrapper(func):
        print '===2===', func

        def inner_func(*args):
            print '===3===', args
            if callable(key_func):
                key = key_func(*args)
            else:
                key = key_func
            # cache = caches['credit']
            # result = cache.get(key)
            result = False
            if not result:
                load_from_db = True
                cache = 'test'
                if prevent_snowslide:
                    with lockit(cache, 'lock:%s' %(key), 60) as has_lock:
                        if has_lock:
                            load_from_db = False
                            time.sleep(0.5)
                            # result = cache.get(key)
                            result = 'test result'

                if load_from_db:
                    result = func(*args)
                    # cache.set(key, result, timeout=timeout)
            return result
        return inner_func
    return wrapper


class DecorateTest:
    USER_CURRENCY_IDS = 'currency:user:%(uid)s'

    @cached_result(lambda o, uid: DecorateTest.USER_CURRENCY_IDS % ({'uid': uid}), 3600*24)
    def get_usercurrency_ids(self, uid):
        print "get_usercurrency uid: ", uid
        return [1, 2, 3]

if __name__ == '__main__':
    d = DecorateTest()
    print d.get_usercurrency_ids('123')