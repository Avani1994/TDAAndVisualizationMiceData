#!/usr/bin/env python

from    pylab           import scatter, show, cm, colorbar, savefig, axis, \
                               figure, xlim, axes, hsv, subplots_adjust as adjust
#from    itertools       import izip
from    sys             import argv, exit
import  os.path         as     osp
from pprint import pprint
import itertools
import pylab as plt
import numpy as np
import scipy as sp
from astropy.stats import LombScargle
import math

def getPeriod(value):
    X = np.array(value)
    N = len(value)
    # Compute the FFT
    W    = np.fft.fft(X)
    freq = np.fft.fftfreq(N,1)
    # Look for the longest signal that is "loud"
    print(max(W))
    threshold = 20
    idx = np.where(abs(W)>threshold)[0][-1]

    max_f = abs(freq[idx])
    return 1/max_f

def getPeriod2(values):
    frequency, power = LombScargle(range(1, len(values) + 1), values).autopower()
    plt.plot(frequency, power)
    plt.show()
    # print power
    p = 99.5
    while True:
        threshold = np.percentile(power, p)
        print(threshold)
        #print(np.where(abs(power)>threshold)[0])
        #idx = np.where(abs(power)>threshold)[0]
        #threshold
        idx = np.where(abs(power)>threshold)[0]
        print(idx)
        if (len(idx) > 3 and (idx[1] - idx[0]) == 1 and (idx[2] - idx[1]) == 1 and (idx[3] - idx[2]) == 1):
            break;
        p -= 0.1
    max_f = abs(frequency[idx][1])
    return 1/max_f


def mapplot(V, val_fn, dt):
    points = V
    
    values = []
    with open(val_fn) as fp:
        for line in fp.readlines():
            values.append(float(line.split()[1]))
    m = min(values)
    values = [(v-m) % 1. for v in values]
    period = getPeriod2(values)
    print(period)
    colormap = [0.0] * len(V)
    size = len(values)
    j = len(values)
    for i in range(len(V)):
        if i < len(values):
            colormap[i] = values[i]
        else:
            # ====>> should use math.round instead of int so that 1.7 => 2 instead of 1
            # or as a hack just add 0.5 to the end(which I did)
            colormap[i] = values[min(int(size - (period * math.ceil((i - size) / period)) + (i - size) % period - 1 + 1.5 + 1), len(values) - 1)]
            #colormap[i] = values[int(size - period + (i - size) % period)]
            #colormap[i] = values[min(int(size - (period * math.ceil((i - size) / period)) + (i - size) % period + 1), len(values)-1)]
            '''
            if(j < len(values)*2 and j < len(V)):
                colormap[i] = values[int(size - (period * math.ceil((j - size) / period)) + (j - size) % period + 1)]
                j = j + 1
            
            else:
                j = len(values)
            '''
                                   
    # print(colormap)
    # sys.exit()
    #print colormap
    return colormap
    # hsv()

# if __name__ == '_main_':
#     if len(argv) < 3:
#         print "Usage: %s VALUES POINTS" % argv[0]
#         exit()
