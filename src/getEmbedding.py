import numpy as np
from scipy import sparse
import pandas as pd


def my_range(start, end, step):
    roll = []
    while start < end:
        roll = roll + [start]
        start += step
    return roll

def getEmbedding(datain, windowsize, gap=1):
    #print ("MaxTau = {0} " .format(maxtau))
    print ("Window Size = {0} " .format(windowsize))
    print ("Gap = {0} " .format(gap))
    print("")
    out=[]
    
    #print roll
    #roll = [gap] * (maxtau - 1)
    #print(len(datain)-windowsize + 1)
    print(len(datain))
    roll = my_range(1, (len(datain)-windowsize + 1), gap)
    #print roll
    for tau in roll:
        #print tau
        lagged = np.roll(datain, -tau + 1, axis=0)[:-tau]
        lagged = lagged[0:windowsize]
        out.append(lagged.tolist())
    #print out    
    out = np.array(out, dtype=float)
    return(out)

def getEmbeddingSubSample(datain, windowsize, gap=1):
    #np.max(a.shape[0] - (w-1)*(g+1), 0)
    #print(np.arange(windowsize)*(gap + 1)) + np.arange(np.max(datain.shape[0]-(windowsize-1)*(gap+1),0)).reshape(-1,1)
    out = datain[(np.arange(windowsize)*(gap + 1)) + np.arange(np.max(datain.shape[0]-(windowsize-1)*(gap+1),0)).reshape(-1,1)]
    return(out)

'''
V = pd.read_csv('m49_nonpreg_clean.csv', header = None, index_col = False)
print V[0:10]
X = getEmbedding(V, maxtau = 970, windowsize = 300, gap = 100)
X.astype('float64', order='C')
np.savetxt('data.txt', X, fmt = '%f')
#print np.shape(out)
#print out
'''