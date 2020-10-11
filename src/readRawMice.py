import pandas as pd
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from itertools import groupby
import sys

def remove0s(col):
    return col[col!=0]

def reducevariance(col):
    return col[~((col-col.mean()).abs()>3*col.std())]


def readRawMice(inputFile, inputSheet, outDir):
    filepath = inputFile
    #filepath = "../Mice_Dataset/BeiMiceTemp.xlsx"
    #mycolumns = "BU" # choose your columns (comma separated)
    #df = pd.read_excel(filepath, sheetname = 'ForReproducingResults', skiprows=0, squeeze = True)
    df = pd.read_excel(filepath, sheet_name=inputSheet, skiprows=0, squeeze=True)
    print(df.head())
    df = df.replace(0, np.nan)
    
    outputs_dict = {}
    #df = df.dropna(axis = 1, thresh = 30000)
    df = df.dropna(axis = 1, thresh = 2751)
    print(df.head())
    #df = df.drop('m34', axis=1)
    k = 5000

    newDF = pd.DataFrame()

    #Remove lesser than K consecutive NaNs from pandas DataFrame
    for column in df:
        print(column)
        tempdf = pd.DataFrame()
        #print column
        #df[column] = (df.groupby(pd.notna(df[column]).cumsum())
        #.apply(lambda x: x.dropna() if pd.isna(x[column]).sum() <= k else x)
        #.reset_index(drop=True))
        
        i = df[column].isnull()
        m = ~(df.groupby(i.ne(i.shift()).cumsum().values)[column].transform('size').le(k) & i)
        #pd.concat([newDF,df[m]], ignore_index=True, axis=1)
        #print df[m]
        tempdf = df[column][m]
        tempdf = tempdf.reset_index(drop = True)
        #print tempdf
        newDF[column] = pd.Series(tempdf)
    
    for column in newDF:
        #print column
        
        # sparse_ts = newDF[column].to_sparse()
        # block_locs = zip(sparse_ts.sp_index.blocs, sparse_ts.sp_index.blengths)
        # #print block_locs
        # # Map the sparse blocks back to the dense timeseries
        # blocks = [[newDF[column].iloc[start:(start + length - 1)]] for (start, length) in block_locs]
        nparray = np.asarray(newDF[column])
        result = [pd.DataFrame(list(v)) for k,v in groupby(nparray,np.isfinite) if k]
        
        outputs_dict[column] = outputs_dict.get(column, result)

    newDF2 = pd.DataFrame()

    for column in outputs_dict.keys():
        #print column
        for i,block in enumerate(outputs_dict[column]):
            #print i
            dfser = pd.DataFrame()
            # if(column == 'm1' and i == 1):
            #    print(block[0])
            block[0] = block[0].reset_index(drop = True)
            dfser[column+'_'+str(i)] = pd.Series(block[0])
            newDF2 = pd.concat([newDF2, dfser[column+'_'+str(i)]], axis = 1)

    newDF2 = newDF2.apply(reducevariance, axis=0)
    column_labels = newDF2.columns.values


    dic = {k: list(v) for k, v in groupby(column_labels, key=lambda x: x[:-1])}
    #print dic

    
    for key in dic.keys():
        for col in dic[key]:
            #print col
            column = pd.Series(newDF2[col])
            column = column[~column.isnull()]
            column.to_csv(outDir + str(col) + '_clean.csv',header=False,index = False, na_rep = None)
            #column.to_csv('../CleanedMice/CleanReproducible/'+ str(col) + '_clean.csv',header=False,index = False, na_rep = None)
    
    return dic


def main():
    if(len(sys.argv) < 4):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputFilePath, arg2 as InpustSheet, arg3 as OutDirectoryPath")
    elif(len(sys.argv) > 4):
        print("Extra Arguments")
        print("Please provide - arg1 as InputFilePath, arg2 as InpustSheet, arg3 as OutDirectoryPath")

    inputFile = sys.argv[1]
    inputSheet = sys.argv[2]
    outDir = sys.argv[3]

    readRawMice(inputFile, inputSheet, outDir)


if __name__ == '__main__':
  main()   



#readRawMice()
#filepath = "../Mice_Dataset/BeiMiceTemp.xlsx"
#mycolumns = "AC" # choose your columns (comma separated)
#df = pd.read_excel(filepath, sheetname = 'Temps', skiprows=0, squeeze = True, usecols =  mycolumns)
#plt.figure()
#ax = df.plot()
#fig = ax.get_figure()
#print root+ file[:-4] + ".png"
#fig.savefig("49raw.png")
#plt.show()


