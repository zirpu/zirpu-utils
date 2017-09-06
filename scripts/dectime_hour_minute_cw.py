#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Play CW numbers at H and MM of decimal time.  ie. at :00 play H and MM CW.

Optional, after 10 secs, play either A-Z rotating window of N chars, or random N chars.
Or a random word from /usr/share/dict/words, QSO's, Q codes.

Q codes could be 2 or 3 times each.  1st time to remember/lookup, 2nd and 3rd for repetition.

"""

import sys
import os

import argparse
import logging

import time

from zirpu.time import time_string


CW='/home/allan/sounds/cw'
NUMBERS = {n.replace('.ogg',''): CW+'/numbers/'+n for n in os.listdir(CW+'/numbers')}
LETTERS = {n.replace('.ogg',''): CW+'/letters/'+n for n in os.listdir(CW+'/letters')}

PUNCTS  = {
    "&": CW+"/punctuation/" + "Ampersand.ogg",
    "'": CW+"/punctuation/" + "Apostrope.ogg",
    "@": CW+"/punctuation/" + "At.ogg",
    ":": CW+"/punctuation/" + "Colon.ogg",
    ",": CW+"/punctuation/" + "Comma.ogg",
    "$": CW+"/punctuation/" + "Dollar_Sign.ogg",
    "=": CW+"/punctuation/" + "Equals.ogg",
    "!": CW+"/punctuation/" + "Exclamation_Point.ogg",
    "-": CW+"/punctuation/" + "Hyphen,_Minus.ogg",
    "(": CW+"/punctuation/" + "Parenthesis_(Close).ogg",
    ")": CW+"/punctuation/" + "Parenthesis_(Open).ogg",
    ".": CW+"/punctuation/" + "Period.ogg",
    "+": CW+"/punctuation/" + "Plus.ogg",
    "?": CW+"/punctuation/" + "Question_Mark.ogg",
    "\"": CW+"/punctuation/" + "Quotation_Mark.ogg",
    ";": CW+"/punctuation/" + "Semicolon.ogg",
    "/": CW+"/punctuation/" + "Slash.ogg",
    "_": CW+"/punctuation/" + "Underscore.ogg"
}


def main(args):
    lets = list(LETTERS.keys())
    lets.sort()
    
    while True:
        ts = int(time.time())
        now = str(ts)
        ss = now[-2:]
        mm = now[-4:-2]
        h = now[-5:-4]
        if ss == '00':  #  maybe:  ss in ['00', '99', '01'] ?
            fs = [NUMBERS[i] for i in [h, mm[0], mm[1]]]
            # play h and mm.
            os.system("ff {} {} {}".format(*fs))
            print(time_string(now))
            # play 4 letters, rotating window of a-z.
            tmp = [lets.pop(0) for i in range(4)]
            for i in tmp: lets.append(i)
            t = [LETTERS[i] for i in tmp]
            os.system("ff {} {} {} {}".format(*t))
            print(' '.join(tmp))
        else:  # sleep until ss == 00
            sl = 100 - (int(time.time()) % 100)
            print(sl)
            time.sleep(sl)
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
