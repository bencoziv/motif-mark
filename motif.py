#!/usr/bin/env python
import re


class motifList(object):

    def __init__(self, sequence, header, motifs,
                 motifPos = None,
                 motifTyp = None,
                 seqLen = None,
                 exons = None,
                 chrPos = None):
        self.sequence = sequence
        self.header = header
        self.motifs = motifs
        self.motifPos = []
        self.motifTyp = []
        self.seqLen = len(self.sequence)
        self.exons = []
        self.chrPos = header.split(" ")[1]
        p = re.compile("[A-Z]+")
        m = p.finditer(self.sequence)
        for match in m:
            self.exons.append(match.span())
        self.sequence = self.sequence.lower()
        x = 0
        for i in self.motifs:
            x += 1
            p = re.compile(i)
            m = p.finditer(self.sequence)
            for match in m:
                self.motifPos.append(match.start())
                self.motifTyp.append(x)
        self.sequence = None
        self.header = None
        self.motifs = None

    def info(self):
        return self.motifPos, self.motifTyp, self.seqLen, self.exons, self.chrPos


