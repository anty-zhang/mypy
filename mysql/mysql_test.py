# -*- coding: utf-8 -*-
import random
from tornado import web, gen
from tornado.log import gen_log
from base.basehandler import BaseHandler

from util.redis_client import RedisClient
from util.mysql import TornadoMysqlClient, TorMysqlClient, MySQL


class TestHandler(BaseHandler):
    @web.asynchronous
    @gen.coroutine
    def get(self):
        a = self.get_argument("a", "a_default")
        db = self.get_argument("db", "")
        cache = self.get_argument("cache", "")
        key = "%s_%d" % (a, random.randint(1, 10000))
        
        result = ""
        
        # redis-py test
        if cache == "redis":
            redis_client_set = yield RedisClient().get_redis_client()
            
            redis_client_set.set(key, a, 600)
            gen_log.debug("redis set key: %s, value: %s", key, a)
    
            redis_client_get = yield RedisClient().get_redis_client()
            result = "redis: " + redis_client_get.get(key)
            gen_log.debug("redis get key: %s, result: %s", key, result)
        
        # mysql
        if db == "mysql":
            gen_log.debug("===mysql driver test insert before")
            conn = MySQL.create_mysql_master_connect()
            cursor = conn.cursor()
            gen_log.debug("===mysql driver test insert name: %s, value: %s", key, a)
            cursor.execute("""insert into db_test(name, value) values ('%s', '%s')""" % (key, a))
            cursor.execute("""insert into db_test(name, value) values ('%s', '%s')""" % (key, a))
            cursor.execute("""insert into db_test(name, value) values ('%s', '%s')""" % (key, a))
            conn.commit()
            conn.close()
            gen_log.debug("===mysql driver test insert end")

            gen_log.debug("===mysql driver test update before")
            conn = MySQL.create_mysql_master_connect()
            cursor = conn.cursor()
            conn.begin()
            gen_log.debug("===mysql driver test update value: %s, name: %s", key + "_myTest", key)
            cursor.execute("""update db_test set value= '%s' where name='%s'""" %(key + "_myTest", key))
            cursor.execute("""update db_test set value= '%s' where name='%s'""" % (key + "_myTest", key))
            conn.commit()
            conn.close()
            gen_log.debug("===mysql driver test update end")
            
            gen_log.debug("===mysql driver test fetchall before")
            conn = MySQL.create_mysql_connect()
            cursor = conn.cursor()
            gen_log.debug("===mysql driver test select name: %s", key)
            cursor.execute("""select name, value from db_test where name='%s'""" % key)
            msg = cursor.fetchall()
            gen_log.debug("===mysql driver test msg: %s", str(msg))
            result += str(msg)
            conn.close()
            gen_log.debug("===mysql driver test update end")
        
        # tornado driver test
        if db == "tornado":
            gen_log.debug("tornado driver test insert before")
            cur = yield TornadoMysqlClient().execute("""insert into db_test(name, value) values (%s, %s)""", (key, a))
            cur = yield TornadoMysqlClient().execute("""insert into db_test(name, value) values (%s, %s)""", (key, a))
            cur = yield TornadoMysqlClient().execute("""insert into db_test(name, value) values (%s, %s)""", (key, a))
            gen_log.debug("tornado driver test cur: %s", cur)
            gen_log.debug("tornado driver test insert end")

            # gen_log.debug("tornado driver test insert many before")
            # cur = yield TornadoMysqlClient().insert_many("""insert into db_test(name, value) values (%s, %s)""",
            #                                              ((key, a), (key, a)))
            # gen_log.debug("tornado driver test cur: %s", cur)
            # gen_log.debug("tornado driver test insert many end")

            gen_log.debug("tornado driver test update before")
            cur = yield TornadoMysqlClient().execute_by_transaction("""update db_test set value= %s where name=%s""",
                                                         (key + "_myTest", key))
            gen_log.debug("tornado driver test cur: %s", cur)
            gen_log.debug("tornado driver test update end")

            gen_log.debug("tornado driver test select one before")
            msg = yield TornadoMysqlClient().fetchone("""select name, value from db_test where name=%s""", key)
            gen_log.debug("tornado driver test select one cur: %s end", msg)
            result += " ,tornado mysql: %s" % msg

            gen_log.debug("tornado driver test select many before")
            msg = yield TornadoMysqlClient().fetchmany("""select name, value from db_test where name=%s""", key, 2)
            gen_log.debug("tornado driver test select many cur: %s end", msg)
            result += " ,tornado mysql: %s" % msg

            gen_log.debug("tornado driver test select all before")
            msg = yield TornadoMysqlClient().fetchall("""select name, value from db_test where name=%s""", key)
            gen_log.debug("tornado driver test select all cur: %s end", msg)
            result += " ,tornado mysql: %s" % msg
            
        # tormysql driver test
        if db == "tor":
            gen_log.debug("tor driver test insert before")
            gen_log.debug("tor driver test key: %s, value: %s", key, a)
            res = yield TorMysqlClient().execute("""insert into db_test(name, value) values (%s, %s)""", (key, a))
            gen_log.debug("tor driver test insert cur: %s", res)
            res = yield TorMysqlClient().execute_many(
                """insert into db_test(name, value) values (%s, %s)""",
                ((key, a), (key, a)))
            gen_log.debug("tor driver test insert_many cur: %s", res)
            gen_log.debug("tor driver test insert end")

            gen_log.debug("tor driver test update before")
            gen_log.debug("tor driver test key: %s, value: %s", key, a + "_mytest")
            res = yield TorMysqlClient().execute("""update db_test set value = %s where name = %s""", (a + "_mytest", key))
            gen_log.debug("tor driver test update cur: %s", res)
            gen_log.debug("tor driver test update end")
            
            # time.sleep(0.5)
            
            gen_log.debug("tor driver test select before")
            # key = "guog_6666"
            res = yield TorMysqlClient().fetchone(
                """select name,VALUE from db_test where name=%s""", key)
            result += " ,tor mysql: %s" % str(res)
            gen_log.debug("tor driver test select one: %s", res)

            res = yield TorMysqlClient().fetchall(
                """select name, value from db_test where name=%s and value =%s""", (key, a + "_mytest"))
            result += " ,tor mysql: %s" % str(res)
            gen_log.debug("tor driver test select all: %s", res)

            res = yield TorMysqlClient().fetcmany(
                """select name, value from db_test where name=%s and value =%s""", (key, a + "_mytest"), 2)
            result += " ,tor mysql: %s" % str(res)
            gen_log.debug("tor driver test select many: %s", res)
            
            gen_log.debug("tor driver test select end")
        
        # 返回json
        d = {
            "c": 0,
            "r": "a",
            "res": result,
        }

        gen_log.debug("debug test: %s", d)
        gen_log.info("info test: %s", d)

        self.jsonify(d)
