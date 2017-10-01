#!/usr/bin/env python

'''
'''

import os
import time
import string

from random import randint

import pyglet

from zirpu.time import time_string

window = pyglet.window.Window(fullscreen=True)

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

def dectime():
    n = int(time.time())
    return(time_string(n))


# x: 0 .. 560
# y: 0 .. 940
# x, y: 1920, 1080

class Timer(object):
    def __init__(self):
        self.label = pyglet.text.Label(dectime(), font_size=120,
                                       x=0,
                                       y=0,
                                       anchor_x='left', anchor_y='baseline')
        # x=window.width//2, y=window.height//2,
        # self.t0 = pyglet.media.load('/home/allan/sounds/SS/0.wav', streaming=False)
        # self.tn = pyglet.media.load('/home/allan/sounds/SS/N.wav', streaming=False)
        # self.cwn = {}
        # for n in NUMBERS:
        #     self.cwn[n] = pyglet.media.load(NUMBERS[n], streaming=False)
        # self.cwl = {}
        # for n in LETTERS:
        #     self.cwl[n] = pyglet.media.load(LETTERS[n], streaming=False)
            
        self.block = False

        self.reset()

    def reset(self, bogus=None):
        self.label.x = randint(0, 560)
        self.label.y = randint(0, 940)
        # self.label.text = dectime()
        # self.label.color = (255, 255, 255, 255)

    def update(self, dt=0):
        # 15:0:6:6 5:60:60
        dt = dectime()
        ss = dt[-2:]
        mm = dt[-5:-3]
        h  = dt[-7]
        self.label.text = dt

        # turning off sound for now.
        return
    
        if self.block:
            return
        
        # FIX: timing issue. update continues being called. how to play cw over/with the ticks?
        # if ss == '00':
        #     self.block = True
        #     # play cw.
        #     self.cwn[h].play()
        #     self.cwn[mm[0]].play()
        #     self.cwn[mm[1]].play()
        #     self.block = False
            
        if ss[1] == '0':
            self.t0.play()
        else:
            self.tn.play()
        if ss == '99':
            self.reset()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        pass #timer.reset()

    elif symbol == pyglet.window.key.ESCAPE:
        window.close()

@window.event
def on_draw():
    window.clear()
    timer.label.draw()

timer = Timer()
pyglet.clock.schedule_interval(timer.update, 1.0)
#pyglet.clock.schedule_interval(timer.reset, 100)
pyglet.app.run()

