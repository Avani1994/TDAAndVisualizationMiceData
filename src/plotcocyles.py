import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
import webbrowser
import os
import heapq
from getEmbedding import getEmbedding
from runCohomology import getCocyles
from sys import argv
import sys

# plot cocycles - points.val using two most prominent directions obtained using PCA
def plotcocyles(inputDir, cofile, micename):
   # mapping for circular value parameterization
    directory = inputDir + micename + "/" 
    # Generating the output in the form of a PDF
    print(cofile)
    vis_path = 'python3 plotpca.py ' + directory + 'points-' + cofile + '.val ' + directory + 'data.txt' 
    q = call([vis_path], shell=True)
    if q==0:
        print("Plotting sucessful!")

def main():
    if(len(sys.argv) < 2):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputDirPath, this is where pdf will be generated")
    elif(len(sys.argv) > 2):
        print("Extra Arguments")
        print("Please provide - arg1 as InputDirPath, this is where pdf will be generated")
    inputDir = sys.argv[1]
    print(inputDir)
    maxPersistenceCircle = -1
    for path, subdirs, files in os.walk(inputDir):
        for subname in subdirs:
            print(subname)
            maxPersistenceCircle = -1 
            for p, sub, fil in os.walk(inputDir+subname):
                for f in fil:
                    if( f.endswith('.val')):
                        print(f)
                        maxPersistenceCircle = max(maxPersistenceCircle, int(f.split('-')[1].split('.')[0]))
            
            plotcocyles(inputDir, str(maxPersistenceCircle), subname)

if __name__ == '__main__':
    main()

    
