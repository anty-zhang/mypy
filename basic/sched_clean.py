#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sched
import sys,time
import os


delay_time = 24*60*60

def mk_del_list():
    lines = os.popen("hadoop dfs -du -h /user/hive/warehouse/streaming_user_to_article").readlines()
    today_date = time.strftime('%Y%m%d',time.localtime(time.time()))
    lines = filter(lambda x: x[-3:-1] != "00" and x[-11:-3] != today_date, lines)
    lines = map(lambda x: "/user" + x.split("/user")[1][:-1], lines)
    return lines
    
def clean_data(lines):
    for line in lines:
        # print "hadoop dfs -rm -r " + line
        os.system("hadoop dfs -rm -r " + line)

# action function, and add another event to queue.
def event(action_time):
    print "action_time:%s" % (action_time)
    lines = mk_del_list()
    clean_data(lines)
    scheduler.enterabs(action_time + delay_time, 1, event, (action_time + delay_time,))

# 初始化scheduler
scheduler = sched.scheduler(time.time, time.sleep)

# 获得执行调度的初始时间
inittime = time.time()


# 设定调度 使用enterabs设定真实执行时间
# 参数：1 执行时间（time.time格式）2 优先级 3 执行的函数 4 函数参数
scheduler.enterabs(inittime, 1, event, (inittime,))

# 执行调度，会一直阻塞在这里，直到函数执行结束
scheduler.run()
