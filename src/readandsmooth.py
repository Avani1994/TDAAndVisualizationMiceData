"""Converts the input file into a matrix and smooths the input using low pass filter"""

#inmport modules
import numpy as np
import pandas as pd
import csv
from subprocess import call
import os
from datetime import datetime
import scipy.signal as signal
import matplotlib.pyplot as plt
import os, errno
import sys

def readandsmooth(inputDir, infile, outDir):
    temp = np.genfromtxt(inputDir+infile, delimiter=',')
    print(np.shape(temp))

    if(np.shape(temp) > (10,)):
        # First, design the Buterworth filter
        N  = 2    # Filter order
        Wn = 0.002 # Cutoff frequency
        B, A = signal.butter(N, Wn, output='ba')
         
        # Second, apply the filter
        tempf = signal.filtfilt(B, A, temp)
        #x = range(1,len(tempf)+1)

        directory = outDir+infile[:-10]
        
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        np.savetxt(directory + '/lpf.csv', tempf, delimiter=',')

        #Call RScript that smoothens the input
        #cutoff = 0.002
        #cutoff = str(cutoff)
        path = 'Rscript discretesmooth.R lpf.csv ' + directory
        call([path], shell=True)

def smoothAll(inputDir, outDir):
    for filename in os.listdir(inputDir):
        if(not filename.endswith('.png')):
            readandsmooth(inputDir, filename, outDir)
        
def main():
    if(len(sys.argv) < 3):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputDirPath, arg2 as OutdirPath")
    elif(len(sys.argv) > 3):
        print("Extra Arguments")
        print("Please provide - arg1 as InputDirPath, arg2 as OutdirPath")

    inputDir = sys.argv[1]
    outDir = sys.argv[2]
    smoothAll(inputDir, outDir)

if __name__ == '__main__':
    main()      
     
    
'''
points = []
#smoothed-mice
with open('finalsmoothed.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        points.append(float(row[0]))
y = points
t = np.linspace(1, len(y), len(y))
V = pd.DataFrame([t,y]).transpose()
V.plot()
V = V.as_matrix()
print str(datetime.now())
return(V)
'''
