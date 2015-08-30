#!/usr/bin/env python
# -*- mode: python; encoding: utf-8 -*-

# check_mk python script template.

# check_mk output format:
# return-code name-of-check perf-data(k-v,..) (OK|WARNING|CRITICAL|UNKNOWN) msg
# 0: ok, 1: warning, 2: critical, 3: unknown.
# perf is:  key=val[;warn;crit;min;max][|key2=val2...]


"""template
"""

import sys
# modify path here before other imports if needed.

# the rest of the imports should be in alphabetical order.
import argparse
from os.path import basename, splitext

NAME = splitext(basename(sys.argv[0]))[0]
CODE = ["OK", "WARN", "CRITICAL", "UNKNOWN"]


def check_mk_out(msg, rc, **kw):
    """print check_mk expected local check output.

    :param msg: string
    :param rc: int
    :param kw: hash of performance data to send to check_mk
    """

    # check_mk local client output format:
    # return-code name-of-check perf-data(k-v,...) (CRITICAL|WARNING|OK) msg
    # perf is:  key=val[;warn;crit;min;max][|key2=val2...]
    perf = "-"
    if kw:
        perf = '|'.join(['%s=%s' % (i, kw[i]) for i in kw])

    if '\n' in msg:
        msg = ' '.join(msg.split('\n'))  # in case of newlines.
    print "%d %s %s %s %s" % (rc, NAME, perf, CODE[rc], msg)
    sys.exit(0)  # doesn't use exit code like nrpe checks.


def main(ns, *args, **kwargs):
    """The Mainly Main().
    """

    # default: everything is OK.
    if not ns.debug:
        check_mk_out('ok', 0)
    return None


def parse_the_args(args=None):
    if args is not None:
        parser = argparse.ArgumentParser(args)
    else:
        parser = argparse.ArgumentParser()

    parser.add_argument('--debug', default=False, action='store_true')

    return parser.parse_args(args)

if __name__ == '__main__':
    ns = parse_the_args()
    main(ns)
