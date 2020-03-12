#!/usr/bin/env python

import argparse
import motif as mo
import draw 
import re


def get_args():

    """ get file names for input FASTA and motifs"""
    parser = argparse.ArgumentParser(description=' File name to be used')
    parser.add_argument('-f', '--fasta', type=str,help='File Name for Fasta containing sequences to search', 
                        required=True)
    parser.add_argument('-m', '--motif', type=str, help='File Name for file containing motifs each on separate lines', 
                        required=True)
    return parser.parse_args()


args = get_args()
f = args.fasta
m = args.motif
iupac = {'r': '[a,g]', 'y': '[c,t]', 's': '[g,c]', 'w': '[a,t]', 'k': '[g,t]', 'm': '[a,c]', 'b': '[c,g,t]',
         'd': '[a,g,t]', 'h': '[a,c,t]', 'v': '[a,c,g]', 'n': '[a,c,g,t]', 'u': 't'}


def motifs(m):
    """Takes the path to motif file, extracts motifs, converts to regex, and returns two lists"""
    with open(m, 'r') as mot:

        motif = []
        motife = []
        for line in mot:
            line = line.strip()
            motif.append(line)
            line = line.lower()
            motife.append('(?=('+(''.join(iupac.get(ch, ch) for ch in line))+'))')
            # creates a regex for variable IUPAC codes and adds a lookahead to find consecutive motifs
    return motif, motife


def main():

    motif, motife = motifs(m)
    with open(f, 'r') as file:
        seq = ""
        hed = ""
        obs = []
        for line in file:
            line = line.strip()
            if re.search("^>", line) is None:
                #Checks if line is a header line or a sequence line
                seq = seq + line
            else:
                if len(seq) > 0:
                    obs.append(mo.motifList(seq, hed, motife))
                    hed = line
                    seq = ""
                else:
                    hed = line
                    seq = ""
        obs.append(mo.motifList(seq, hed, motife))
        #added to append the last sequence to an object
    draw.draw(obs, motif)
    # Passes set of motif objects to draw class, and unedited motifs to create a picture

    
if __name__ == "__main__":
    main()



