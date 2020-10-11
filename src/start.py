import numpy as np
import pandas as pd
from generateParameterization import findParameterization
from sys import argv
from readandsmooth import readandsmooth
from astropy.stats import LombScargle
import pylab as plt
from readRawMice import readRawMice 
import os
from plotcocyles import plotcocyles
import csv
from getEmbedding import getEmbedding

if __name__ == '__main__':
    # Smoothens the input and converts to a matrix for further processing
    #dicts = readRawMice()
    
    for filename in os.listdir('CleanMiceBeiMiss'):
        if(filename.endswith('.csv')):
            readandsmooth('CleanMiceBeiMiss/'+filename)
    #exit()
    values = []
    with open("smoothed-mice.csv", 'rb') as fp:
        for line in fp.xreadlines():
            values.append(float(line))
    m = min(values)
    values = [(v-m) % 1. for v in values]
    period = getPeriod2(values)
    print("period",period)
    
    
    # Finds the appropriate embedding and circular parameterization
    root = "./SmoothedMiceBeiMiss/"
    #root = "./Pregnant/"
    #print root
    windows = 300
    for key in dicts.keys():
        print(key)
        Embed = np.empty((0,300), float)
        for col in dicts[key]:
            print col
            points = []
            #smoothed-mice
            try:
                with open(root+col+'/finalsmoothed.csv', 'rb') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        points.append(float(row[0]))
                y = points
                t = np.linspace(1, len(y), len(y))
                V = pd.DataFrame([t,y]).transpose()
                #V.plot()
                V = V.as_matrix()
                if(len(V) > windows):
                    X = getEmbedding(V[:,1], windowsize = windows, gap = 1)
                    print np.shape(X)
                    Embed = np.append(Embed,X,axis=0)
            except IOError:
                print("Wrong file or file path")

            #print str(datetime.now())
            #return(V)
        print "Avani"
        print Embed
        #5.65
        findParameterization(Embed, 1, 3, key)
        #exit()
    
    root2 = "./CohomologyOPBeiMissWithoutRankNJNP/"
    for path, subdirs, files in os.walk(root2):
        for subname in subdirs:
            if (subname == 'm61_'):
                '''
                plotcocyles(0,subname)
                plotcocyles(1,subname)
                plotcocyles(2,subname)
                plotcocyles(3,subname)
                plotcocyles(4,subname)
                plotcocyles(5,subname)
                plotcocyles(45,subname)
                plotcocyles(46,subname)
                plotcocyles(87,subname)
                '''
                plotcocyles(69,subname)
                '''
                plotcocyles(10,subname)
                plotcocyles(11,subname)
                plotcocyles(12,subname)
                plotcocyles(13,subname)
                plotcocyles(14,subname)
                plotcocyles(15,subname)
                plotcocyles(16,subname)
                plotcocyles(19,subname)
                plotcocyles(33,subname)
                plotcocyles(67,subname)
                plotcocyles(72,subname)
                plotcocyles(94,subname)
                plotcocyles(166,subname)
                plotcocyles(102,subname)
                plotcocyles(103,subname)
                plotcocyles(104,subname)
                plotcocyles(105,subname)
                plotcocyles(153,subname)
                plotcocyles(119,subname)
                plotcocyles(129,subname)
                plotcocyles(255,subname)
                plotcocyles(155,subname)
                plotcocyles(45,subname)
                plotcocyles(46,subname)
                plotcocyles(47,subname)
                plotcocyles(48,subname)
                plotcocyles(49,subname)
                plotcocyles(80,subname)
                plotcocyles(85,subname)
                plotcocyles(50,subname)
                plotcocyles(25,subname)
                plotcocyles(28,subname)
                plotcocyles(121,subname)
                plotcocyles(86,subname)
                plotcocyles(7,subname)
                plotcocyles(40,subname)
                plotcocyles(44,subname)
                plotcocyles(89,subname)
                plotcocyles(114,subname)
                plotcocyles(61,subname)
                plotcocyles(215,subname)
                plotcocyles(87,subname)
                plotcocyles(145,subname)
                plotcocyles(17,subname)
                plotcocyles(187,subname)
                '''







