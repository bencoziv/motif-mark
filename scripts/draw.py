#!/usr/bin/env python

import cairo
import matplotlib.cm as cm


class draw(object):

    def __init__(self, obs,motifs):
        self.obs = obs
        self.motifs = motifs
        cmap = []
        d = 254/(len(obs)-1)
        for i in range(len(obs)):
            cmap.append(cm.jet(round(i * d) + 1))
        width = 0
        for ob in self.obs:
            if ob.seqLen > width:
                width = ob.seqLen
        height = (100*len(obs))+(25*len(motifs))
        surface = cairo.SVGSurface("MotifMark.svg", width, height)
        ct = cairo.Context(surface)
        ct.set_line_width(1)
        y = 50
        for ob in self.obs:
            ct.set_font_size(10)
            ct.set_source_rgb(0, 0, 0)
            ct.move_to(5,(y-30))
            ct.show_text(ob.chrPos)
            ct.move_to(0, y)
            ct.line_to(ob.seqLen, y)
            ct.stroke()
            for exon in ob.exons:
                ct.set_source_rgba(0, 0, 0, .5)
                ct.rectangle(exon[0], (y-15), (exon[1]-exon[0]), 30)
                ct.fill()
            m = 0
            for motif in ob.motifPos:
                ct.move_to(motif, y)
                ct.set_source_rgba(cmap[(ob.motifTyp[m]-1)][0],cmap[(ob.motifTyp[m]-1)][1],cmap[(ob.motifTyp[m]-1)][2],
                                   ((cmap[(ob.motifTyp[m]-1)][3])*1))
                ct.move_to((int(motif)), (y-10))
                ct.line_to(int(motif), (y+10))
                ct.stroke()
                m += 1
            y += 100
        i = 0
        ct.move_to(10, y - 60)
        ct.set_source_rgb(0, 0, 0)
        ct.show_text("Motif Legend")
        for motif in motifs:
            ct.set_source_rgba(cmap[i][0], cmap[i][1], cmap[i][2], cmap[i][3])
            ct.rectangle(5, (y - 50), 100, y)
            ct.fill()
            ct.move_to(110, y - 35)
            ct.set_font_size(10)
            ct.set_source_rgb(0, 0, 0)
            ct.show_text(motif)
            y += 25
            i += 1 

        surface.finish()





