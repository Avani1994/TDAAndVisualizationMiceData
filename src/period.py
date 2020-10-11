from cogent.maths.period import dft
from cogent.maths.period import auto_corr
from    pylab           import scatter, show, cm, colorbar, savefig, axis, \
                               figure, xlim, axes, hsv, subplots_adjust as adjust
from    itertools       import izip
from    sys             import argv, exit
import  os.path         as     osp
from pprint import pprint
import itertools
import pylab as plt
import numpy as np
import scipy as sp
from astropy.stats import LombScargle
import math
import os
import pandas as pd


def getPeriod(value):
    X = np.array(value)
    N = len(value)
    # Compute the FFT
    W    = np.fft.fft(X)
    freq = np.fft.fftfreq(N,1)
    # Look for the longest signal that is "loud"
    #print max(W)
    threshold = 20
    idx = np.where(abs(W)>threshold)[0][-1]

    max_f = abs(freq[idx])
    return 1/max_f


def getPeriod2(values):
    frequency, power = LombScargle(range(1, len(values) + 1), values).autopower()
    #plt.plot(frequency, power)
    #plt.show()
    # print power
    #power = abs(power)
    #max_pwr, max_f = sorted(zip(power,frequency),key=lambda x: x[0])[-1]
    #max_pwr2, max_f2 = sorted(zip(power,frequency),key=lambda x: x[0])[-2]
    
    p = 99.5
    while True:
        threshold = np.percentile(power, p)
        #print threshold
        #print(np.where(abs(power)>threshold)[0])
        #idx = np.where(abs(power)>threshold)[0]
        #threshold
        idx = np.where(abs(power)>threshold)[0]
        #print idx
        if (len(idx) > 3 and (idx[1] - idx[0]) == 1 and (idx[2] - idx[1]) == 1 and (idx[3] - idx[2]) == 1):
            break;
        p -= 0.1
    max_f = abs(frequency[idx][1])
    max_f2 = abs(frequency[idx][2])
    
    return [1/max_f, 1/max_f2]
    
def getPeriodDFT(values):
    pwr, period = dft(values)
    #print period
    #print pwr


    pwr = abs(pwr)
    max_pwr, max_period = sorted(zip(pwr,period),key=lambda x: x[0])[-1]
    max_pwr2, max_period2 = sorted(zip(pwr,period),key=lambda x: x[0])[-2]
    '''
    p = 99.9
    while True:
        threshold = np.percentile(pwr, p)
        #print threshold
        #print(np.where(abs(power)>threshold)[0])
        #idx = np.where(abs(power)>threshold)[0]
        #threshold
        idx = np.where(pwr>threshold)[0]
        #print idx
        if (len(idx) > 3 and (idx[1] - idx[0]) == 1 and (idx[2] - idx[1]) == 1 and (idx[3] - idx[2]) == 1):
            break;
        p -= 0.1
    max_period = abs(period[idx][1])
    max_period2 = abs(period[idx][2])
    '''

    return [max_period,max_period2]

def getPeriodAutoCorr(values):
    pwr, period = auto_corr(values)
    max_pwr, max_period = sorted(zip(pwr,period))[-1]
    return max_period

root = "./SmoothedMiceBeiMiss/"
for path, subdirs, files in os.walk(root):
    for subdir in subdirs:
        values = []
        print subdir
        with open(root + subdir + "/finalsmoothed.csv", 'rb') as fp:
            for line in fp.xreadlines():
                values.append(float(line))
            
            print getPeriodDFT(values)
            print getPeriodAutoCorr(values)
            #print getPeriod(values)
            values = np.asarray(values)
            m = np.min(values)
            #values = (values-np.mean(values))/values.std()
            values = [(v-m) % 1 for v in values]
            print getPeriod2(values)

            print("\n")
    





