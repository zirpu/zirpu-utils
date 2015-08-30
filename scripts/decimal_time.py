#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Decimal time.
"""

from __future__ import print_function

import os
#default to UTC.
os.environ['TZ'] = 'UTC'

import argparse
import logging

import datetime
import time

from zirpu.time import return_time_list, color_time_list

header = ['yy', 'm', 'w', 'd', 'h', 'mn', 'sc']

def main(args):
    """main(args)

    :param argparse.Namespace args:  CLI options.
    """
    ts = args.ts
    iso = datetime.datetime.fromtimestamp(ts).isoformat()
    a = return_time_list(ts, base=args.base)
    if args.color:
        a = color_time_list(a)
    a = ':'.join(a[:-3]) + ' ' + ':'.join(a[-3:])
    print(a)


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
