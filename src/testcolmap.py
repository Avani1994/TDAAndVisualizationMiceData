# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
from sys import argv
import sys
from mapback_ak import mapplot
import matplotlib.pyplot as plt

def toMatrix(points):
	t = np.linspace(1, len(points), len(points))
	y = points
	V = pd.DataFrame([t,y]).transpose()
	V = V.to_numpy()
	return(V)

def main():
	if(len(sys.argv) < 3):
		print("Insufficient Arguments")
		print("Please provide - arg1 as SmoothedFile, arg2 as dotValFile")
	elif(len(sys.argv) > 3):
		print("Extra Arguments")
		print("Please provide - arg1 as SmoothedFile, arg2 as dotValFile")

	inputSmoothedFile = sys.argv[1]
	dotValFile = sys.argv[2]
	points = []
	with open(inputSmoothedFile, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			#print row
			points.append(float(row[0]))	
	V = toMatrix(points)
	#
	
	'''
	arr = []
	with open('points-0.val') as fp:
		for line in fp.xreadlines():
			arr.append(float(line.split()[1]))                        
	val = []
	for i in range(0, 126):
		val.append(np.mean(arr[max(i - 31, 0): min(127,i+1)]))
	print val

	f = open("exten_val.val", 'w')
	for i,item in enumerate(val):
		f.write(str(i)+' ' +str(item) + '\n')

	f.close()
	'''

	colMap = mapplot(V, dotValFile , 1)

	plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
	plt.subplot(212)
	plt.plot(np.arange(len(V[:,1])), V[:,1], linewidth=0.5, color='k')
	#plt.scatter(np.arange(len(V[:,1])), V[:,1], c=colMap[:len(colMap)], s= 60)
	plt.scatter(np.arange(len(V[:,1])), V[:,1], c=colMap, s= 40, cmap=plt.cm.jet)
	plt.axis([0,len(V[:,1]),min(V[:,1])-0.5,max(V[:,1])+0.5])
	plt.subplot(211)
	plt.plot(np.arange(len(V[:,1])), V[:,1], color='k')
	plt.axis([0,len(V[:,1]),min(V[:,1])-0.5,max(V[:,1])+0.5])
	plt.show()


if __name__ == '__main__':
	main()
	