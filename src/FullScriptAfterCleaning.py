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
from getEmbedding import getEmbedding, getEmbeddingSubSample
import sys

def generateVisualprofile(inputDir, outDir):
    # Smoothens the input and converts to a matrix for further processing
    '''
    values = []
    with open("smoothed-mice.csv", 'rb') as fp:
        for line in fp.xreadlines():
            values.append(float(line))
    m = min(values)
    values = [(v-m) % 1. for v in values]
    period = getPeriod2(values)
    print "period",period
    '''
    
    # Finds the appropriate embedding and circular parameterization
    #root = "./SmoothedMiceBeiMiss/"
    root = inputDir
    dicts = {}
    for path, subdirs, files in os.walk(root):
        for subdir in subdirs:
            key = subdir[:-2]
            if key not in dicts:
                dicts[key] = [subdir]
            else:
                dicts[key].append(subdir)

    windows = 300
    #tau = 300
    print(dicts)
    for key in dicts.keys():
        print(key)
        Embed = np.empty((0,300), float)
        for col in dicts[key]:
            print(col)
            points = []
            #smoothed-mice
            try:
                with open(root+col+'/finalsmoothed.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        points.append(float(row[0]))
                    y = points
                    t = np.linspace(1, len(y), len(y))
                    V = pd.DataFrame([t,y]).transpose()
                    #V.plot()
                    V = V.to_numpy() 
                    print(len(V))
                    #print V
                    if(len(V) > windows):
                        X = getEmbedding(V[:,1], windowsize = windows, gap = 1)
                        #X = getEmbeddingSubSample(V[:,1], windowsize = windows , gap = 1)
                        print(np.shape(X))
                        #print X
                        #exit()
                        Embed = np.append(Embed,X,axis=0)
            except IOError:
                print("Wrong file or file path")

        #print str(datetime.now())
        #return(V)
        print(Embed)
        findParameterization(Embed, 1, 3, key, outDir)
        #exit()
    
def main():
    if(len(sys.argv) < 3):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputDirPath, arg2 as OutputDirPath")
    elif(len(sys.argv) > 3):
        print("Extra Arguments")
        print("Please provide - arg1 as InputDirPath, arg2 as OutputDirPath")

    inputDir = sys.argv[1]
    outDir = sys.argv[2]
    generateVisualprofile(inputDir, outDir)


if __name__ == '__main__':
    main()

'''
root2 = "./CohomologyOPBen4dist/"
for path, subdirs, files in os.walk(root2):
    for subname in subdirs:
        plotcocyles(0,subname)
        plotcocyles(1,subname)
'''








