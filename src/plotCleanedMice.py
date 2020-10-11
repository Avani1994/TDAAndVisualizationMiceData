import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
plt.rcParams.update({'figure.max_open_warning': 0})

def plot(inputDir):
	root = inputDir
	for path, subdirs, files in os.walk(root):
		for f in files:
			print(f)
			if os.path.exists(path+f) and f.endswith('.png'):
				try:
					os.remove(path+f)
				except OSError:
					pass
	for path, subdirs, files in os.walk(root):
		for file in files:
			if(os.stat(root + file).st_size != 0):
				df = pd.read_csv(root + file, squeeze = True)
				if(df.empty == False):
					plt.figure()
					ax = df.plot()
					fig = ax.get_figure()
					#print root+ file[:-4] + ".png"
					fig.savefig(root+ file[:-4] + ".png")
					#plt.show()

def main():
    if(len(sys.argv) < 2):
        print("Insufficient Arguments")
        print("Please provide - arg1 as InputDirPath, That's where your images will also be stored")
    elif(len(sys.argv) > 2):
        print("Extra Arguments")
        print("Please provide - arg1 as InputDirPath, That's where your images will also be stored")

    inputDir = sys.argv[1]
    plot(inputDir)


if __name__ == '__main__':
    main()
