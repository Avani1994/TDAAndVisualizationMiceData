import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

directory = './CohomologyOPBeiMissWithoutRankNJNP/'
df = pd.read_csv(directory + "m85_/points.dgm", names = ['dim','birth','death'], delim_whitespace = True)
dim1_df = df[df.dim == 1]
dim1_df = dim1_df.replace(to_replace = np.inf, value=6)

dim1_df['persistence'] = dim1_df['death'] - dim1_df['birth']

dim1_df = dim1_df.sort_values('persistence', ascending = False)
print(dim1_df)
threemostuseful = dim1_df[:6]
print(threemostuseful)
radiiuseful = threemostuseful["death"] - 0.1
print(radiiuseful)
exit()

#Without rankfilter none of them was useful,*******************************************************
#Only 2 of them produced some .ccl files:
#That too highest persistence = 0.08, 0.14 on radii = 3

#For the ones which did not die 
#m76 : highest persistence = 0.25
#m1 : highest persistence = 0.10

#Not at all useful


#With Rank Filter:*****************************************************************************************
#Highest Persistence : starting from 0.6, 0.7, 0.8, 0.9, 0.99 till infinity or 3

#Non Jetlagged:
#m32 : pregnant - next higher persistence = 0.264683
#m49 : Not Pregnant - next higher persistence = 0.367610

# JetLagged:
# Pregnant:
#m1, next higher persistence: 0.349302
#m38, next higher persistence: 0.210610
#m76, next higher persistence: 0.403885 , highest = 2.115800 , for this all died at radii = 3 , 2.43 something

# Not Pregnant:
#m2, next higher persistence: 0.268935
#m3, next higher persistence: 0.381606

#Category 1
#m75, next higher persistence: 0.383060, highest = 2.395697, for this all died at radii = 3, 2.784
#m31, next higher persistence: 0.348840, next = 0.086390, highest =  1.905824, for this too all died at radii = 3

#Will Try : m76, m75, m31 for round two

#got good results :) out of these

#With Sub Sampling:*************************************************************************************

#Highest Persistence : starting from 0.5, 0.8, 0.9, 1.6 till infinity or 3
#one did not produce any result

#Non Jetlagged:
#m32 : pregnant - next higher persistence = 0.069938
#m49 : Not Pregnant - next higher persistence = 0.167898

# JetLagged:
# Pregnant:
#m1, next higher persistence: 0.194029 
#m38, next higher persistence: Empty data.txt
#m76, next higher persistence: 0.146786

# Not Pregnant:
#m2, next higher persistence: 0.159084 
#m3, next higher persistence: no other highest persistence : only one dim1 feature 

#Category 1
#m75, next higher persistence: 0.149390
#m31, next higher persistence: 0.021284

#Will Try : Nothing here to try all are very low persistence





