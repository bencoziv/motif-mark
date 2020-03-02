#!/usr/bin/env python

import pycairo

class draw(object):

    def __init__(self, obs, fileName):
        self.obs = obs
        self.fileName = fileName
    def draw (self):
        width = 0
        for ob in self.obs:
            if obs[ob].seqLen > width:
                width = obs[ob].seqLen
        width += 200



