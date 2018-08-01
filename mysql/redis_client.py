# -*- coding: utf-8 -*-

import redis
from tornado import gen
from tornado.log import gen_log

from base.config import Config
CONNECTION_POOL = None


class InitConnectionPool(object):
    def __init__(self):
        global CONNECTION_POOL
        if not CONNECTION_POOL:
            CONNECTION_POOL = redis.ConnectionPool(
                host=Config["redis.host"],
                port=Config["redis.port"],
                db=Config["redis.db"],
                password="%s" % Config["redis.password"],
                # password='',
                socket_keepalive=True,
                max_connections=int(Config["redis.max_connections"]))
            gen_log.debug("init REDIS_CONNECTION_POOL: %s", CONNECTION_POOL)
    

class RedisClient(InitConnectionPool):
    @gen.coroutine
    def get_redis_client(self):
        client = redis.Redis(connection_pool=CONNECTION_POOL)
        gen_log.debug("get_redis_client: %s", client)
        raise gen.Return(client)

