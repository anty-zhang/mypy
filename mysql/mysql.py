# coding=utf-8
import urlparse
from random import choice
from tornado import gen
import MySQLdb
import tornado_mysql.pools
import tormysql

from base.config import Config
from tornado.log import gen_log

MASTER_TORNADO_MYSQL_POOL = []
MASTER_TOR_MYSQL_POOL = []
MASTER_MYSQL_POOL = []

SLAVE_TORNADO_MYSQL_POOL = []
SLAVE_TOR_MYSQL_POOL = []
SLAVE_MYSQL_POOL = []


class MySQL(object):
    @staticmethod
    def create_mysql_connect():
        host = choice(Config["mysql.hosts_s"].split(","))  # 随机选择一个host
        connect = MySQLdb.connect(host=host,
                                  user=Config["mysql.user"],
                                  passwd=Config["mysql.password"],
                                  db=Config["mysql.db"],
                                  port=int(Config["mysql.port"]),
                                  charset="utf8")
        return connect

    @staticmethod
    def create_mysql_master_connect():
        connect = MySQLdb.connect(host=Config["mysql.host_m"],
                                  user=Config["mysql.user"],
                                  passwd=Config["mysql.password"],
                                  db=Config["mysql.db"],
                                  port=int(Config["mysql.port"]),
                                  charset="utf8")
        return connect
    
    
class InitTornadoMysqlConnectPool(object):
    def __init__(self):
        global MASTER_TORNADO_MYSQL_POOL
        global SLAVE_TORNADO_MYSQL_POOL
        if not MASTER_TORNADO_MYSQL_POOL:
            master_urls = Config["mysql.master"]
            gen_log.debug("===master_urls: %s", master_urls)
            gen_log.debug("===master_max_idle_connections: %s", Config["mysql.master_max_idle_connections"])
            gen_log.debug("===master_max_open_connections: %s", Config["mysql.master_max_open_connections"])
            gen_log.debug("===master_max_recycle_sec: %s", Config["mysql.master_max_recycle_sec"])
            if master_urls:
                for url in master_urls.split(";"):
                    pool = self.init_mysql_pool(url, Config["mysql.master_max_idle_connections"], Config["mysql.master_max_open_connections"],
                                                Config["mysql.master_max_recycle_sec"])
                    MASTER_TORNADO_MYSQL_POOL.append(pool)
            gen_log.debug("MASTER_TORNADO_MYSQL_POOL is: %s", MASTER_TORNADO_MYSQL_POOL)
                    
        if not SLAVE_TORNADO_MYSQL_POOL:
            slave_urls = Config["mysql.slave"]
            gen_log.debug("===slave_urls: %s", slave_urls)
            gen_log.debug("===slave_max_idle_connections: %s", Config["mysql.slave_max_idle_connections"])
            gen_log.debug("===slave_max_open_connections: %s", Config["mysql.slave_max_open_connections"])
            gen_log.debug("===slave_max_recycle_sec: %s", Config["mysql.slave_max_recycle_sec"])
            if slave_urls:
                for url in slave_urls.split(";"):
                    pool = self.init_mysql_pool(url, Config["mysql.slave_max_idle_connections"], Config["mysql.slave_max_open_connections"],
                                                Config["mysql.slave_max_recycle_sec"])
                    SLAVE_TORNADO_MYSQL_POOL.append(pool)
            gen_log.debug("SLAVE_TORNADO_MYSQL_POOL is: %s", SLAVE_TORNADO_MYSQL_POOL)
                
    def init_mysql_pool(self, jdbc_url, max_idle_conn=1, max_open_conn=10, max_recycle_sec=60):
        """
        :param jdbc_url: mysql://root:xxx@xiaoqiang-zdm:3306/mysql
        :return:
        """
        if not jdbc_url:
            return
    
        gen_log.debug("jdbc_url: %s", jdbc_url)
        conf = urlparse.urlparse(jdbc_url)
        gen_log.debug("hostname: %s, db: %s, user: %s, passwd: %s, port: %s",
                      conf.hostname, conf.path, conf.username, conf.password, conf.port)
    
        db = ''
        if len(conf.path) > 1:
            db = conf.path[1:]
    
        return tornado_mysql.pools.Pool(
            dict(
                host=conf.hostname, port=conf.port, db=db,
                user=conf.username, passwd=conf.password,
                charset='utf8',
                cursorclass=tornado_mysql.cursors.DictCursor
            ),
            max_idle_connections=max_idle_conn,
            max_open_connections=max_open_conn,
            max_recycle_sec=max_recycle_sec
        )
    
    
class TornadoMysqlClient(InitTornadoMysqlConnectPool):
    @gen.coroutine
    def execute(self, sql, args=None):
        """
        desc: 插入／更新／删除操作
        :param sql:
        :param args:
        :return:
        """
        pool = choice(MASTER_TORNADO_MYSQL_POOL)
        res = yield pool.execute(sql, args)
        gen_log.debug("TornadoMysqlClient insert res: %s", res)
        raise gen.Return(res)
    
    @gen.coroutine
    def execute_by_transaction(self, sql, args=None):
        """
        desc: 插入／更新／删除操作，加入事务操作
        :param sql:
        :param args:
        :return:
        """
        pool = choice(MASTER_TORNADO_MYSQL_POOL)
        transaction = yield pool.begin()
        res = -1
        try:
            gen_log.debug("TornadoMysqlClient update sql: %s, args: %s", sql, str(args))
            res = yield transaction.execute(sql, args)
        except Exception as e:
            gen_log.debug("TornadoMysqlClient update exception msg: %s", str(e.message))
            yield transaction.rollback()
        finally:
            gen_log.debug("TornadoMysqlClient update commit success!")
            yield transaction.commit()
        raise gen.Return(res)

    @gen.coroutine
    def _execute(self, sql, args=None):
        pool = choice(SLAVE_TORNADO_MYSQL_POOL)
        cur = yield pool.execute(sql, args)
        raise gen.Return(cur)
    
    @gen.coroutine
    def fetchone(self, sql, args=None):
        """
        desc: 获取一条数据
        :param sql:
        :param args:
        :return:
        """
        cur = yield self._execute(sql, args)
        msg = cur.fetchone()
        raise gen.Return(msg)

    @gen.coroutine
    def fetchmany(self, sql, args=None, size=1):
        """
        desc： 获取size条数据
        :param sql:
        :param args:
        :param size:
        :return:
        """
        cur = yield self._execute(sql, args)
        msg = cur.fetchmany(size=size)
        raise gen.Return(msg)

    @gen.coroutine
    def fetchall(self, sql, args=None):
        """
        desc: 获取全部数据
        :param sql:
        :param args:
        :return:
        """
        cur = yield self._execute(sql, args)
        msg = cur.fetchall()
        raise gen.Return(msg)
        

class TorMysqlConnectPool(object):
    def __init__(self):
        global MASTER_TOR_MYSQL_POOL
        global SLAVE_TOR_MYSQL_POOL
        if not MASTER_TOR_MYSQL_POOL:
            master_urls = Config["mysql.master"]
            gen_log.debug("===master_urls: %s", master_urls)
            gen_log.debug("===master_max_connections: %s", Config["mysql.master_max_connections"])
            gen_log.debug("===master_idle_seconds: %s", Config["mysql.master_idle_seconds"])
            gen_log.debug("===master_wait_connection_timeout: %s", Config["mysql.master_wait_connection_timeout"])
            self.parse_jdbc_urls_and_init_pool(master_urls, MASTER_TOR_MYSQL_POOL,
                                               Config["mysql.master_max_connections"],
                                               Config["mysql.master_idle_seconds"],
                                               Config["mysql.master_wait_connection_timeout"])

            gen_log.debug("MASTER_TOR_MYSQL_POOL is: %s", MASTER_TOR_MYSQL_POOL)
            
        if not SLAVE_TOR_MYSQL_POOL:
            slave_urls = Config["mysql.slave"]
            gen_log.debug("===slave_urls: %s", slave_urls)
            gen_log.debug("===slave_max_connections: %s", Config["mysql.slave_max_connections"])
            gen_log.debug("===slave_idle_seconds: %s", Config["mysql.slave_idle_seconds"])
            gen_log.debug("===slave_wait_connection_timeout: %s", Config["mysql.slave_wait_connection_timeout"])
            self.parse_jdbc_urls_and_init_pool(slave_urls, SLAVE_TOR_MYSQL_POOL,
                                               Config["mysql.slave_max_connections"],
                                               Config["mysql.slave_idle_seconds"],
                                               Config["mysql.slave_wait_connection_timeout"])
    
            gen_log.debug("SLAVE_TOR_MYSQL_POOL is: %s", SLAVE_TOR_MYSQL_POOL)
                
    def parse_jdbc_urls_and_init_pool(self, urls, pool_list, max_connections, idle_seconds, wait_connection_timeout):
        if urls:
            for url in urls.split(";"):
                pool = self.init_mysql_pool(url, max_connections, idle_seconds, wait_connection_timeout)
                pool_list.append(pool)

    def init_mysql_pool(self, jdbc_url, max_connections=10, idle_seconds=60, wait_connection_timeout=3):
        """
        :param jdbc_url: mysql://root:xxx@xiaoqiang-zdm:3306/mysql
        :return:
        """
        if not jdbc_url:
            return
    
        gen_log.debug("jdbc_url: %s", jdbc_url)
        conf = urlparse.urlparse(jdbc_url)
        gen_log.debug("hostname: %s, db: %s, user: %s, passwd: %s, port: %s",
                      conf.hostname, conf.path, conf.username, conf.password, conf.port)
    
        db = ''
        if len(conf.path) > 1:
            db = conf.path[1:]

        return tormysql.ConnectionPool(
            max_connections=int(max_connections),  # max open connections
            idle_seconds=int(idle_seconds),  # conntion idle timeout time, 0 is not timeout
            wait_connection_timeout=int(wait_connection_timeout),  # wait connection timeout
            host=conf.hostname,
            user=conf.username,
            passwd=conf.password,
            db=db,
            charset="utf8"
        )


class TorMysqlClient(TorMysqlConnectPool):
    @gen.coroutine
    def execute(self, sql, args=None):
        """
        desc: 插入／删除／修改，均可使用此函数
        :param sql: sql语句
        :param args: sql语句中的参数
        :return:
        """
        pool = choice(MASTER_TOR_MYSQL_POOL)
        res = -1
        with (yield pool.Connection()) as conn:
            try:
                with conn.cursor() as cursor:
                    res = yield cursor.execute(sql, args)
                    gen_log.debug("update res: %s", res)
            except Exception as e:
                gen_log.debug("update Exception msg: %s", e.message)
                yield conn.rollback()
            finally:
                yield conn.commit()
        raise gen.Return(res)
    
    @gen.coroutine
    def execute_many(self, sql, args):
        """
        desc: 插入／删除／修改，均可使用此函数，可以写入多个值
        :param sql: sql语句
        :param args: sql语句中的参数
        :return:
        """
        pool = choice(MASTER_TOR_MYSQL_POOL)
        res = -1
        with (yield pool.Connection()) as conn:
            try:
                with conn.cursor() as cursor:
                    res = yield cursor.executemany(sql, args)
                    gen_log.debug("update_many res: %s", res)
            except Exception as e:
                gen_log.debug("update_many Exception msg: %s", e.message)
                yield conn.rollback()
            finally:
                yield conn.commit()
        raise gen.Return(res)

    @gen.coroutine
    def fetchone(self, sql, args=None):
        """
        desc: 获取一条数据
        :param sql:
        :param args:
        :return:
        """
        with (yield self._execute(sql, args)) as cursor:
            msg = cursor.fetchone()
            gen_log.debug("TorMysqlClient fetchone msg: %s", msg)
            raise gen.Return(msg)

    @gen.coroutine
    def fetchall(self, sql, args=None):
        """
        desc: 获取所有的数据
        :param sql:
        :param args:
        :return:
        """
        with (yield self._execute(sql, args)) as cursor:
            msg = cursor.fetchall()
            gen_log.debug("TorMysqlClient fetchall msg: %s", msg)
            raise gen.Return(msg)

    @gen.coroutine
    def fetcmany(self, sql, args=None, size=1):
        """
        desc: 获取指定条数数据
        :param sql:
        :param args:
        :param size:
        :return:
        """
        with (yield self._execute(sql, args)) as cursor:
            msg = cursor.fetchmany(size=size)
            gen_log.debug("TorMysqlClient fetchmany msg: %s", msg)
            raise gen.Return(msg)
            
    @gen.coroutine
    def _execute(self, sql, args=None):
        pool = choice(SLAVE_TOR_MYSQL_POOL)
        gen_log.debug("TorMysqlClient _execute sql: %s, args: %s, pool: %s", sql, str(args), pool)
        with (yield pool.Connection()) as conn:
            with conn.cursor() as cursor:
                res = yield cursor.execute(sql, args)
                yield conn.commit()
                gen_log.debug("TorMysqlClient _execute res: %s", res)
                raise gen.Return(cursor)
