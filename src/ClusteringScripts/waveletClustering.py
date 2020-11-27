import pywt
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy
from sklearn.cluster import DBSCAN
from scipy.cluster.hierarchy import fcluster
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import fcluster, set_link_color_palette
import sys

def waveletClustering(inputFile, sheetname):
    #filepath = "../Mice_Dataset/preg_for_mice.xlsx"
    filepath = inputFile
    #mycolumns = "BU" # choose your columns (comma separated)
    df = pd.read_excel(filepath, sheet_name = sheetname, skiprows=0, squeeze = True)
    df = df.replace(0, np.nan)
    #outputs_dict = {}
    #df = df.dropna(axis = 1, thresh = 30000)
    df = df.dropna(axis = 1, thresh = 1)

    df = df.apply(lambda x: pd.Series(x.dropna().values))
    #print (df)
    print(df.info())

    # Truncating the dataset as hierarchichal clustering takes same length for each subject
    df = df[:25079]	# JNPPreg
    #df = df[:23163] # JP #JPPreg
    #df = df[:23639] #JPPPreg
    #df = df[:50623] #JPP

    #print df[:18832].info()
    #(cA, cD) = pywt.dwt([1, 2, 3, 4, 5, 6], 'db1')
    print(df.shape)
    cAdata = []
    cDdata = []
    labelsWavelet = []
    for col in df.columns:
        print(col)
        labelsWavelet.append(col.rstrip('preg'))
        cA, cD = pywt.dwt(df[col], 'haar')
        cAdata = cAdata + [cA]
        cDdata = cDdata + [cD]
    #print len(cAdata[0]), len(cAdata)
    #print len(cDdata[0]), len(cDdata)


    cAdatanp = np.array([np.array(xi) for xi in cAdata])
    cDdatanp = np.array([np.array(xi) for xi in cDdata])
    #print cAdatanp
    print(np.shape(cAdatanp))
    pairwisedist = pdist(cAdatanp, 'euclidean')
    print(pairwisedist)
    print(squareform(pairwisedist))
    #uppertriu =	scipy.sparse.triu(pairwisedist, k =1)


    #Takes in wavelet coefficients instead of pairwise distance b/w them, 
    # calculated distance internally
    result = linkage(cAdatanp, method='average', metric='euclidean')
    #result = linkage(cDdatanp, method='average', metric='euclidean')
    print(result)

    plt.title('Hierarchical Clustering Dendrogram (Wavelet)')
    plt.xlabel('Mice Id')
    plt.ylabel('Euclidian Distance')
    dendrogram(
        result,
        truncate_mode='lastp',  # show only the last p merged clusters
        #p=10,  # show only the last p merged clusters
        labels = ['m39','m40', 'm47', 'm98', 'm102', 'm2', 'm3', 'm4', 'm6', 'm8', 'm59'], #JNPPreg
        #labels = ['m7','m30', 'm31', 'm35', 'm35_1', 'm36', 'm36_1', 'm41', 'm41_1', 'm45', 'm46', 'm50', 'm58', 'm75', 'm79', 'm95', 'm96', 'm100'], #JPP
        #labels = ['m1', 'm5', 'm37', 'm37_1', 'm38', 'm38_1', 'm51', 'm53', 'm57', 'm76', 'm94', 'm101'], #JP
        #labels = ['m7', 'm30', 'm31', 'm35', 'm36', 'm41', 'm41_1', 'm45', 'm46', 'm50', 'm58', 'm75', 'm79', 'm95', 'm96', 'm100'], #JPPPreg
        #labels = ['m1', 'm37', 'm38', 'm38_1', 'm51', 'm53', 'm57', 'm76', 'm94', 'm101'], #JPPreg

        leaf_rotation=30.,
        leaf_font_size=8.,
        show_contracted=True,  # to get a distribution impression in truncated branch50
        color_threshold = 160,
        above_threshold_color = 'k'
    )

    hierarchy.set_link_color_palette(['#b30000','#996600', '#b30086'])
    # Add horizontal line.
    plt.axhline(y=160, c='grey', lw=1, linestyle='dashed')

    plt.show()

    max_d = 160

    clusters = fcluster(result, max_d, criterion='distance')
    print(clusters)

    #198 JPP, # 150 JPPPreg
    #140 JP, # 90 : JPPreg
    #160 JNPPreg 
    return clusters, labelsWavelet

def main():
    if(len(sys.argv) < 3):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputFile (xlsx), arg2 as sheetname")
        exit()
    elif(len(sys.argv) > 3):
        print("Extra Arguments")
        print("Please provide - arg1 as InputFile (xlsx), arg2 as sheetname")
        exit()
    
    inputFile = sys.argv[1]
    sheetname = sys.argv[2]

    waveletClustering(inputFile, sheetname)

if __name__ == '__main__':
    main()


