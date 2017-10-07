#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tick tock.
"""

import sys
import os

import argparse
import logging

import time

from zirpu.time import time_string
import pygame.mixer

SOUNDS='/home/allan/sounds'

# T0 = pyglet.media.load(SOUNDS + "/SS/0.wav", streaming=False)
# TN = pyglet.media.load(SOUNDS + "/SS/N.wav", streaming=False)
pygame.mixer.init()

T0 = pygame.mixer.Sound(SOUNDS + "/SS/0.wav")
TN = pygame.mixer.Sound(SOUNDS + "/SS/N.wav")

def main(args):

    while True:
        ts = int(time.time())

        now = str(ts)
        ss = now[-2:]
        mm = now[-4:-2]
        h = now[-5:-4]
        if ss[1] == '0':
            T0.play(maxtime=300)
        else:
            TN.play(maxtime=300)
        print(time_string(ts, color=True))
        time.sleep(1.0)
    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='template')

    t = 'some default'
    parser.add_argument('--some-var', default=t, help=t)

    parser.add_argument('--debug', default=False, action='store_true',
                        help="debug flag.")

    args = parser.parse_args()

    if args.debug:
        print(args)

    main(args)
