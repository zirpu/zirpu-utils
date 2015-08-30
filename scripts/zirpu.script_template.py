#!/usr/bin/env python3
# -*- mode: python; encoding: utf-8 -*-

"""Template CLI script.
"""

#from __future__ import print_function

import argparse
import logging


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='template cli script')

    t = []
    _help = "specify multiple times for a list of values.  empty default."
    parser.add_argument('--some-list-of-values',
                        action='append',
                        default=t,
                        help=_help)

    t = 'some default'
    parser.add_argument('--some-var', default=t, help=t)

    parser.add_argument('--debug', default=False, action='store_true',
                        help="debug flag.")

    args = parser.parse_args()

    if args.debug:
        print(args)

    main(args)
