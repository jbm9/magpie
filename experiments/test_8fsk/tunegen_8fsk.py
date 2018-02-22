#!/usr/bin/python

#yeah yeah argparse me plz
import sys
filename=sys.argv[1]

t_high = 200
t_low = 0

freqs = [ 200,300,500,700, 1100,1300,1700,1900 ]

def gimmebits(l1,l0, bs):
    # l1, l0 the last two bits transmitted, bs a list of bytes to transmit
    
    for b in bs:
        for i in xrange(8):
            b_i = (b >> i) & 1
            nextval = 4*l1 + 2*l0 + b_i
            l1 = l0
            l0 = b_i
            yield nextval

def parsefile(filename):
    f = file(filename)
    payload = f.read()
    f.close()

    for bits in gimmebits(0, 0, [ord(c) for c in payload]):
        print "%d %d" % (t_high, freqs[bits])
        print "%d 0" % t_low

parsefile(filename)
