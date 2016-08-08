# -*- coding: utf-8 -*-

# threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程

#!/usr/bin/python
#current's number of threads
import threading
import time


def worker():
    print "test"
    time.sleep(1)

if __name__ == '__main__':
    for i in xrange(5):
        t = threading.Thread(target=worker)
        t.start()

    print "current has %d threads" % (threading.activeCount() - 1)