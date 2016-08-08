#!/usr/bin/python
#compare for multi threads
import time


def worker():
    print "worker"
    time.sleep(1)
    return
 
if __name__ == "__main__":
    start_time = time.time()
    for i in xrange(5):
        worker()

    print 'finish time is:', time.time() - start_time