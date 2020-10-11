import numpy as np

#file = open("points-0_1.val", 'r')
arr = []
with open('mice4_points.val') as fp:
	for line in fp.xreadlines():
		arr.append(float(line.split()[1]))  

colmap = []
timeseries = 504
j = 0
dt = 244
period = len(arr) - dt
for i in range(0,timeseries):
	if(i < len(arr)-dt):
		colmap = colmap + [arr[i]]
	else:
		if(j <= period):
			colmap = colmap + [arr[j]]
			j = j + 1
		else:
			j = 0

f = open("mice4_val.val", 'w')
for i,item in enumerate(colmap):
    f.write(str(i)+' ' +str(item) + '\n')

f.close()