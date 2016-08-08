#!/usr/bin/python
import threading
import time


def worker():
    print "worker"
    time.sleep(1)
    return

if __name__ == '__main__':
    start_time = time.time()
    for i in xrange(5):

        t = threading.Thread(target=worker)
        t.start()

    print 'finish time is:', time.time() - start_time