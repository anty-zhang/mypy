# -*- coding: utf-8 -*-

import time
import datetime

if __name__ == '__main__':
    start_time = time.time()
    print 'start_time:', start_time

    time.sleep(3)

    print 'load time is :', round(time.time() - start_time)
