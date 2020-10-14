import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy
from sklearn.cluster import DBSCAN
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import fcluster, set_link_color_palette
import os
from subprocess import call
import sys

def tdaClustering(inputDir):
	rel_err = 1
	#root2 = "./CohomologyOPPregJNP/"
	root2 = inputDir
	pairdist = []
	labelsTDA = []
	for path, subdirs, files in os.walk(root2):
		for i, subname1 in enumerate(subdirs):
			labelsTDA.append(subname1.rstrip("preg_"))
			for path2, subdirs2, files2 in os.walk(root2):
				for j, subname2 in enumerate(subdirs2):
					if(j > i):
						# ' ' + str(rel_err) + 
						#df1 = pd.read_csv(root2+subname1+'/points.dgm', sep = ' ', header = None)
						#df1 = df1[[1,2]]
						#df1 = df1.replace(np.inf, 3)
						#print df1
						#df1.to_csv(root2 + subname1 + '/' + subname1 + '.dgm', index = False, header = False, sep=' ')
						#df2 = pd.read_csv(root2+subname2+'/points.dgm', sep = ' ', header = None)
						#df2 = df2[[1,2]]
						#df2 = df2.replace(np.inf, 3)
						#df2.to_csv(root2 + subname2 + '/' + subname2 + '.dgm', index = False, header = False, sep=' ')
						path_wass = '../TopologyExecutables/wasserstein_dist ' + root2 + subname1 + '/' + subname1 + '1.dgm' + ' ' + root2 + subname2 + '/' + subname2 + '1.dgm 2'+ ' > was.txt'
						print(path_wass)
						call([path_wass], shell=True)
						with open('was.txt', 'r') as f:
							was = f.read()
							was = was.strip('\n')
							#print was
							pairdist = pairdist + [float(was)]
						
	print(pairdist)	
	print(len(pairdist))
	result = linkage(pairdist, method='average')
	print(result)

	plt.title('Hierarchical Clustering Dendrogram (TDA Dim 1)')
	plt.xlabel('Mice Id')
	plt.ylabel('Wasserstein Distance')

	# Set the colour of the cluster here:
	dendrogram(
		result,
		truncate_mode='lastp',  # show only the last p merged clusters
		#p=12,  # show only the last p merged clusters
		labels = ['m59','m39','m102', 'm6', 'm47', 'm8', 'm4', 'm98', 'm2', 'm40', 'm3'], #JNPPreg
		#labels = ['m75','m79', 'm96', 'm58', 'm35', 'm45', 'm7', 'm30', 'm31', 'm50', 'm46', 'm36', 'm41', 'm95', 'm100'], #JPPPreg
		#labels = ['m38', 'm1', 'm53', 'm51', 'm101', 'm57', 'm94', 'm37', 'm76'], #JPPreg
		leaf_rotation=30.,
		leaf_font_size = 8.,
		color_threshold = 1.5,
		show_contracted=True,  # to get a distribution impression in truncated branches
		above_threshold_color='k'
	)
	hierarchy.set_link_color_palette(['#b30000','#996600', '#b30086'])
	# Add horizontal line.
	plt.axhline(y=1.5, c='grey', lw=1, linestyle='dashed')

	plt.show()
	#print(dn['color_list'])

	max_d = 1.5
	clusters = fcluster(result, max_d, criterion='distance')
	print(clusters)

	#JNPPreg : 90 , 6.5 (dim 0), 1.5 (dim 1) (degree 2)
	#JPPPreg : 110
	#JPPreg : 70 , 4 (degree 2)
	return clusters, labelsTDA

def main():
	if(len(sys.argv) < 2):
		print("Insufficient Arguments")
		print("Please provide - arg1 as InputDir which contains (birth,death) pair in points1.dgm for each mice")
		exit()
	elif(len(sys.argv) > 2):
		print("Extra Arguments")
		print("Please provide - arg1 as InputDir which contains (birth,death) pair in points1.dgm for each mice")
		exit()
	inputDir = sys.argv[1]
	tdaClustering(inputDir)

if __name__ == '__main__':
	main()

