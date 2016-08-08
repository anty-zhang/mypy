# -*- coding: utf-8 -*-
import time
from datetime import datetime
from pytz import timezone
import pytz


def utc2local(local_tz, utc_st):
    local_tz = timezone(local_tz)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    cur_date = datetime.utcnow().strftime("%Y-%m-%d ")

    loc_dt = local_tz.fromutc(datetime.strptime(cur_date + utc_st, "%Y-%m-%d %H:%M"))
    # local_time = local_tz.fromutc(loc_dt)
    # print 'utc to local:', loc_dt.strftime(fmt)
    return loc_dt

def to_UTC_time(local_tz, local_time):
    cur_tz = timezone(local_tz)
    print 'cur_tz:', cur_tz
    cur_date = datetime.now().strftime('%Y-%m-%d ')
    print 'cur_date:', cur_date
    loc_dt = cur_tz.localize(datetime.strptime(cur_date + local_time, "%Y-%m-%d %H:%M"))
    utc_dt = loc_dt.astimezone(pytz.utc)
    return utc_dt.strftime("%H:%M")


if __name__ == '__main__':

    time_zone = 'Asia/Shanghai'
    local_off_time = '16:10'

    utc_time = to_UTC_time(time_zone, local_off_time)
    print utc_time

    utc_str = '08:10'
    time_zone = 'Europe/Copenhagen'
    local_time = utc2local(time_zone, utc_time)
    print local_time


    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    '''
    utc = pytz.utc
    print utc.zone
    asia = timezone('Asia/Shanghai')
    print asia.zone

    # the first way to build a localized time
    loc_dt = asia.localize(datetime(2002, 10, 27, 6, 0, 0))
    print loc_dt.strftime(fmt)

    # the second way to build a localized time
    asia_dt = loc_dt.astimezone(asia)
    print asia_dt.strftime(fmt)

    utc_dt = datetime(2014, 01, 10, 8, 10, 0, tzinfo=pytz.utc)
    print 'utc_dt:', utc_dt
    loc_dt = utc_dt.astimezone(asia)
    print loc_dt.strftime(fmt)
    '''
    res = utc2local('Asia/Shanghai', '08:10')
    print 'res:', res

    utc = pytz.utc
    utc_dt = utc.localize(datetime.utcfromtimestamp(1422856158))
    print 'utc_dt 1:', utc_dt.strftime(fmt)
    asia_tz = timezone('Asia/Shanghai')
    asia_dt = asia_tz.normalize(utc_dt.astimezone(asia_tz))
    print 'asia_dt 1:', asia_dt.strftime(fmt)

    eu_tz = timezone('Europe/Copenhagen')
    eu_dt = eu_tz.normalize(utc_dt.astimezone(eu_tz))
    print 'asia_dt 1:', eu_dt.strftime(fmt)

