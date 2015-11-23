#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Decimal time alerts.

Runs from cron every minute.  Uses Redis priority-queue for storing alerts at timestamp.

"""

from __future__ import print_function

import os
import io

import argparse
import logging

import datetime
import time
import redis

from subprocess import Popen, PIPE

from zirpu.time import time_string

header = ['yy', 'm', 'w', 'd', 'h', 'mn', 'sc']

def main(args):
    """main(args)

    :param argparse.Namespace args:  CLI options.
    """

    Q = 'dectime.queue'
    now = int(time.time())
    r = redis.StrictRedis()
    # check z.queue 'dectime.queue', if empty generate.
    bloop = r.zrange(Q, 0, 0)
    if bloop:
        bloop = int(bloop[0])
        delta = bloop - now
        if delta < 60:
            time.sleep(delta)
            r.zremrangebyrank(Q, 0, 0)
            a = time_string(bloop, color=args.color, base=args.base)
            # send alert.  email for now.
            print(a)   # using cron.
            send_mail(a)
        else:
            return
    else:
        for i in range(0, 10001):  # dec.hourly checks.
            if check(now + i):
                temp = now + i
                r.zadd(Q, temp, str(temp))
                print('added: {}'.format(temp))

def check(ts):
    "checks the string for yy:m:w:d rollovers."

    # yy, m, w, d
    ts = str(ts)
    for i in range(8, 4, -1):
        if ts.endswith('0'*i):
            return True

def send_mail(msg):
    p = Popen("mail -s'{}' zirpubolci@gmail.com".format(msg), shell=True,
              stdin=PIPE, stdout=PIPE, stderr=PIPE)

    msg += ' ' + datetime.datetime.now().isoformat()
    (stdout, stderr) = p.communicate(memoryview(msg.encode()))

    if stdout or stderr:
        print(stdout)
        print(stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='template cli script')

    parser.add_argument('--debug', default=False, action='store_true', help="debug flag.")

    parser.add_argument('--ts', default=int(time.time()), action='store', help="timestamp. default now().")
    parser.add_argument('--base', default=10, action='store', type=int, help="base from 2-64. default 10.")
    parser.add_argument('--color', default=False, action='store_true', help="colorize time positions.")
    args = parser.parse_args()

    main(args)

# yy m w d h mm ss
# 14 3 8 4 8 51 47

#yy 100,000,000  =~ 3.1709 old years.
#m   10,000,000  =~ 4.1336 old months.
#w    1,000,000  =~ 1.6534 old weeks.
#d      100,000  =~ 1.1574 old days.
#h       10,000  =~ 2.7777 old hours.
#mm       1,000  =~ 16.6666 old minutes.
#ss         100  == same old second.
# 100 sec to a minute.  100minutes to an hour. then 10s. until yy.


# yy m w d h mm ss
# 14 3 8 4 8 51 47
# 14/3/8/4/8:51:47
# 14:3:8:4/8:51:47
# 14:3:8:4 8:51:47
# mega years.  keeps 'century' unit.
# mm yy m w d h mm ss
# 00:14:3:8:4 8:51:47

# mm 1,000,000,000 =~ 11,574.074 days, 385.80 months, 32.15 years.


#  y m w d h mn sc
# 14 1 6 7 0 75 32
# 1 dec.hour = 2.7777 old.hours.
# 1 dec.day  = 27.7777 old.hours = 1.1574 old.days.
# 1 dec.week = 277.7777 old.hours = 11.5740 old.days = 1.6534 old.weeks
# 1 dec.month= 2,777.7777 old.hours = 115.7407 old.days = 16.5343 old.weeks = 3.8580 old.months
# 1 dec.year = 27,777.7777 old.hours = 1,157.4074 ood.days = 165.3439 old.weeks = 38.5802 old. months
#            = 3.170979 old.years
