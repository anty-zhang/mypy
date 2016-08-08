# -*- coding: utf-8 -*-
#!/usr/bin/python
# current's number of threads

# 设置后台进程

#create a daemon
import threading
import time


def worker():
    time.sleep(3)
    print "worker"

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()
print "haha"