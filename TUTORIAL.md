# Tutorial for Single mouse

### Installation
We are using `python3` and `pip3`
###### Preqrequisites
1. I would recommend using virtual env using conda or pip3. Here we have used pip3 virtual environment. 
2. I would also recommend running below scripts from src folder in the directory


Once virtual environment is activated, please follow below:
1. `pip3 install -r requirements.txt`

##### Generate Parameterization Tutorial
Have initial raw data for mouse in .xlsx file in a sheet, in a column with column header as m1. You would need an output directory to output cleaned mice. Please specify the path for output directory as well in the command below
* Step 1 is cleaning the Data 
    Run following command:
    `python3 readRawMice.py InputFilePath.xlsx sheetname outputDirPath`

* Step 2 is smoothing the temperature time series for each mice
    1. You will need the input Directory which would be the path to Output Directory in step 1 and Output Directory to store output of Step 2
   Use following command:
   `python3 readandsmooth.py inputDirPath outDirPath `

* Step 3 is to generate circular valued parameterization for the output in step 2 (step to be done on Linux Machine
    1. You will need the input Directory which would be the path to Output Directory in step 2 and Output Directory to store output of Step 3
    2. You can try using the rips-pairwise-cohomology, I already have generated in TopologyExecutables folder. Otherwise you will have to generate your own binary and ypu can take help from this page: https://mrzv.org/software/dionysus/get-build-install.html. Once you have built dionysus
    Use following command:
    `python3 FullScriptAfterCleaning.py inputDirPath outDirPath`

* Step 4 is to generate Visual Profile using 2 most prominent directions (PCA) and assign rainbow colour according to the parameterization values:
    1. You will need the input Directory which would be the path to Output Directory in step 3
    Use following command:
    `python3 plotcocyles.py inputDirPath`

Finally you will see .pdf files generated in the input Directory for Step 4, which contain circular value parameterization for mouse.