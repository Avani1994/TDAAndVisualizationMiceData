#!/usr/bin/env python

from    pylab           import scatter, show, cm, colorbar, savefig, axis, \
                               figure, xlim, axes, hsv, subplots_adjust as adjust
from    itertools       import izip
from    sys             import argv, exit
import  os.path         as     osp


def mapplot(V, val_fn, dt):
    points = V
    
    values = []
    with open(val_fn) as fp:
        for line in fp.xreadlines():
            values.append(float(line.split()[1]))

    m = min(values)
    values = [(v-m) % 1. for v in values]

    colormap = [0.0] * len(V)
    print(len(V))
    for i in range(len(values)-1):
        colormap[i] = values[i] - values[i+1]
    #for i in range(len(values),len(V)):
#	colormap[i] = values[len(values)-1] - colormap[i-1]
    return colormap
    # hsv()

if __name__ == '__main__':
    if len(argv) < 3:
        print "Usage: %s VALUES POINTS" % argv[0]
        exit()

    val_fn = argv[1]
    pts_fn  = argv[2]
    output_fn, ext = osp.splitext(val_fn)
    output_fn += '.pdf'
    plot(val_fn, pts_fn, output_fn)
