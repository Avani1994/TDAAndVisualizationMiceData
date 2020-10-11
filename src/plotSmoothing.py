import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
plt.rcParams.update({'figure.max_open_warning': 0})

def plotSmooth(inputDir):

	#root = "./SmoothedMiceBeiMissSample1000/"
	root = inputDir

	for path, subdirs, files in os.walk(root):
		for f in files:
			if os.path.exists(path+f) and f.endswith('.png'):
				try:
					os.remove(path+f)
				except OSError:
					pass

	for path, subdirs, files in os.walk(root):
		for subname in subdirs:
			try:
				df1 = pd.read_csv(root+subname+"/lpf.csv",squeeze = True)
				plt.figure()
				if(not df1.empty):
					ax = df1.plot()
					fig = ax.get_figure()
					fig.savefig(root+subname+"/lpf.png")
					#plt.show()
			except IOError:
				print('There was an error opening the file!', root+subname+"/lpf.csv")
			try:
				df2 = pd.read_csv(root+subname+"/sampled.csv",squeeze = True)
				plt.figure()
				if(not df2.empty):
					ax = df2.plot()
					fig = ax.get_figure()
					fig.savefig(root+subname+"/sampled.png")
					#plt.show()
			except IOError:
				print('There was an error opening the file!', root+subname+"/sampled.csv")
			try:
				df3 = pd.read_csv(root+subname+"/finalsmoothed.csv",squeeze = True)
				plt.figure()
				if(not df3.empty):
					ax = df3.plot()
					fig = ax.get_figure()
					fig.savefig(root+subname+"/finalsmoothed.png")
					#plt.show()
					#'''
			except IOError:
				print('There was an error opening the file!', root+subname+"/finalsmoothed.csv")
			
def main():
    if(len(sys.argv) < 2):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputDirPath, That's where your images will also be stored")
    elif(len(sys.argv) > 2):
        print("Extra Arguments")
        print("Please provide - arg1 as InputDirPath, That's where your images will also be stored")

    inputDir = sys.argv[1]
    plotSmooth(inputDir)


if __name__ == '__main__':
    main()


'''
df = pd.read_csv('./CleanMice/m1_clean.csv',squeeze = True)
plt.figure()
ax = df.plot()
fig = ax.get_figure()
fig.savefig("./CleanMice/m1" + "_clean.png")
'''