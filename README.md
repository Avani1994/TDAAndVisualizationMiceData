# Mice Clustering

### Installation
We are using `python3` and `pip3`
I would recommend using virtual env using conda or pip3. Here we have used pip3 virtual environemnt

Once virtual environment is activated, please follow below:
1. `pip3 install -r requirements.txt`
2. If you want to visualize the data you can simply run the python notebook - visualizeRawData.ipynb (make sure you have install Jupyter notebook for python 3 as well as ipykernel for python 3)

Main scripts are in Folder src and I assume you will be running all below scripts inside the src, I have set paths relative to src folder.

##### Part 1 - generate parameterization
Using intial data raw data in ./Mice_Dataset/BeiMiceTemp.xlsx
* Step 1 is cleaning the Data 
    (convert all 0s to nan, remove missing values, remove lesser than K consecutive NaNs from pandas DataFrame and then split dataset based on where > k nans are together, Remove all values which are 3 standard deviations away)
    Run following command:
    `python3 readRawMice.py InputFilePath.xlsx sheetname outputDirPath`
    Ex: `python3 readRawMice.py ../Mice_Dataset/BeiMiceTemp.xlsx ForReproducingResults ../CleanedMice/CleanReproducible/`

* To plot the data after cleaning you can simple run below script:
    `python3 readRawMice.py InputDirPath`
    Ex: `python3 plotCleanedMice.py ../CleanedMice/CleanReproducible/ `

* Step 2 is smoothing the temperature time series for each mice
   This involves 3 procedures:
   1. Low pass filter (we use butterworth filter)
   2. Sampling (1 per 100 points)
   3. Rank Filtering (pass k amplitude and above frequencies, k = 2 for our dataset)
   Use following command:
   `python3 readandsmooth.py inputDirPath outDirPath `
   Ex: `python3 readandsmooth.py ../CleanedMice/CleanReproducible/ ../SmoothenedMice/SmoothedReproducible/  `

* To plot the data after cleaning you can simple run below script:
    `python3 readRawMice.py InputDirPath`
    Ex: `python3 plotCleanedMice.py ../CleanedMice/CleanReproducible/ `

* Step 3 is to generate circular valued parameterization for the output in step 2 (step to be done on Linux Machine)
You will have to generate your own binary for rips-pairwise-cohomology. You may take help from this page: https://mrzv.org/software/dionysus/get-build-install.html
One you have built dionysus, Follow below steps
    1. Generate a point cloud using finalsmoothed.csv (output of rank filter). If there are multiple parts / splits for each mice, we create point clouds separate and then append them
    2. Feed into rips-pairwise-cohomology - it will generate cocycles
    3. Then feed the output to cocyle.py which genertes circular valued parameterization for those cocycles
    Use following command:
    `python3 FullScriptAfterCleaning.py inputDirPath outDirPath`
    Ex: `python3 FullScriptAfterCleaning.py ../SmoothenedMice/SmoothedReproducible/ ../Results/CohomologyReproducible/`

* Step 4 is to generate Visual Profile using 2 most prominent directions (PCA) and assign rainbow colour according to the parameterization values:
    1. Feed the output from Step3 to PlotCocycles.py
    Use following command:
    `python3 plotcocyles.py inputDirPath`
    Ex: `python3 plotcocyles.py ../Results/CohomologyReproducible/`

* Step 5 is mapping back the visual profile to time series of mice temperature data (smoothened output from step 2)
using the point-(int).val - (parameterization) file
    Use following command:
    `python3 testcolmap.py SmoothenedFile ParametrizationFile`
    Ex: `python3 testcolmap.py ../SmoothenedMice/SmoothedReproducible/m1_0/finalsmoothed.csv ../Results/CohomologyReproducible/m1/points-0.val`

##### PART 2 - Generate Clustering for Jetlagged Non Pregnant Mice
(using only the part of data where mice were Jetlagged)

You will have to generate binary for wasserstein distance from here (https://github.com/grey-narn/hera/tree/master/wasserstein)
and store it in Topology executables!
Using data from - ./Mice_Dataset/preg_for_mice.xlsx
1. **Wavelet clustering**
Use 'haar' wavelet coefficients and eucledian distance for clustering for:
Use following command:
`python3 ./ClusteringScripts/waveletClustering.py xlsxFile sheetname`
Ex: `python3 ./ClusteringScripts/waveletClustering.py ../Mice_Dataset/preg_for_mice.xlsx JNP`
2. **TDA Clustering**
Use Dimension 1 persistence diagrams and wasserstein distance with degree 2 for clustering
I assume you have dimension 1 persistence diagram with birth death pairs in a file in the input directory each ending with 1.dgm
Use following command:
`python3 ./ClusteringScripts/tdaClustering.py inputDir  `
Ex: `python3 ./ClusteringScripts/tdaClustering.py ../Results/CohomologyOPPregJNP/  `