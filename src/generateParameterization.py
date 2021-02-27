import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
import webbrowser
import os
import heapq
from getEmbedding import getEmbedding
from runCohomology import getCocyles
from scipy.spatial.distance import pdist


# generate parameterization and get cocycles using the scripts available in dionysus
def findParameterization(X, gap, maxdist, micename, outDir):
    #X = getEmbedding(datain[:,1], windowsize = 300, gap = 1)
    print(np.shape(X))
    #print X
    #d = pdist(X)
    #maxdist = np.mean(d)
    directory = outDir + micename + '/'
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    print("maxdist", maxdist)
    X.astype('float64', order='C')
    np.savetxt(directory+'data.txt', X, fmt = '%f')
    
    # run rips-pairwise cohomology to generate cocycles
    getCocyles(directory+'data.txt', maxdist, micename, outDir)
    
    # generate mapping/points.val for circular value parameterization
    #if(os.exists(directory + 'points-0.ccl')
    for p, sub, fil in os.walk(directory):
        for f in fil:
            if( f.endswith('.ccl')): 
                q = call(['python cocycle.py ' + directory + 'points.bdry '+ directory + 'points-' + f.split('-')[1].split('.')[0] + '.ccl ' + directory + 'points.vrt'], shell=True)
                #call(['python cocycle.py ' + directory + 'points.bdry '+ directory + 'points-1.ccl ' + directory + 'points.vrt'], shell=True)
                if q==0:
                    print("Circular Value Parameterization successful")
                else:
                    print("Circular Value Parameterization not successful. Continuing ...")
