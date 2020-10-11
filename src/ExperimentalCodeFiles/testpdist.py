from scipy.spatial.distance import pdist, squareform
import numpy as np
from nolitsa import data, dimension
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


x = pd.read_csv("./SmoothedMiceBeiMiss/m98_0/finalsmoothed.csv")
xnp = x.values
xnp = xnp.reshape(len(xnp),)
dim = np.arange(1, 400 + 1)
#print dim
f1, f2, f3 = dimension.fnn(xnp, tau=1, dim=dim, window=0, metric='euclidean', parallel = True, R=10.0, A=2.5)

plt.plot(xnp)
plt.show()

plt.title(r'FNN for mice')
plt.xlabel(r'Embedding dimension $d$')
plt.ylabel(r'FNN (%)')
#plt.plot(dim, 100 * f1, 'bo--', label=r'Test I')
#plt.plot(dim, 100 * f2, 'g^--', label=r'Test II')
#label=r'Kennel Test'
plt.plot(dim, 100 * f3, 'rs-')
plt.legend()

plt.show()



'''

points = np.array([[0,1],[1,1],[3,5], [15, 5]])
dist_condensed = pdist(points)
dist = squareform(dist_condensed)
print dist
maxdist = np.max(dist)
print "maxdist", maxdist
'''
