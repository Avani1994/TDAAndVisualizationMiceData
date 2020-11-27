import sys
sys.path.insert(1, './ClusteringScripts')
from sklearn.metrics.cluster import fowlkes_mallows_score
from tdaClustering import tdaClustering 
from waveletClustering import waveletClustering 

def computeFowklesMallowsIndex(inputDirTDA, inputFileWavelet, sheetNameWavelet):
    #labels_TDA = ['m59','m39','m102', 'm6', 'm47', 'm8', 'm4', 'm98', 'm2', 'm40', 'm3']
    #clustering_TDA, labelsTDA = tdaClustering("../Results/CohomologyOPPregJNP/")
    clustering_TDA, labelsTDA = tdaClustering(inputDirTDA)
    #labels_Wavelet = ['m39','m40', 'm47', 'm98', 'm102', 'm2', 'm3', 'm4', 'm6', 'm8', 'm59']
    clustering_Wavelet, labelsWavelet = waveletClustering(inputFileWavelet, sheetNameWavelet)
    # 167
    #[2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 3] -- cutoff 175
    #[2, 2, 1, 1, 1, 1, 4, 4, 3, 3, 5] -- cutoff 160
    #[2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 4] -- cutoff 167


    #Reorganize labels of wavelet clustering according to TDA 
    #label so that they are in same order
    
    reOrganizedWavelet = []
    dicWavelet = {}
    for pair in zip(labelsWavelet, clustering_Wavelet):
        dicWavelet[pair[0]] = pair[1]

    for l in labelsTDA:
        reOrganizedWavelet.append(dicWavelet[l])

    print(reOrganizedWavelet)

    score = fowlkes_mallows_score(clustering_TDA, reOrganizedWavelet)

    #score = fowlkes_mallows_score([1,1,0,0], [0,0,1,1])
    return score


def main():
    if(len(sys.argv) < 4):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputDirForTDA which conatins points.dgm ( in (birth, death) format), arg2 as RawInputFile used for generating cohomology as well, arg3 as sheet name under xlsx file ")
        exit()
    elif(len(sys.argv) > 4):
        print("Extra Arguments")    
        print("Please provide - arg1 as InputDirForTDA which conatins points.dgm ( in (birth, death) format), arg2 as RawInputFile used for generating cohomology as well, arg3 as sheet name under xlsx file ")
        exit()
    inputDirTDA = sys.argv[1]
    inputFileWavelet = sys.argv[2]
    sheetNameWavelet = sys.argv[3]
    print(computeFowklesMallowsIndex(inputDirTDA, inputFileWavelet, sheetNameWavelet))

if __name__ == '__main__':
    main()