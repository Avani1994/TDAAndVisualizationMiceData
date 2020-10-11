import scipy.signal as signal
import matplotlib.pyplot as plt

import numpy as np
temp = np.genfromtxt('m84_nonpreg_clean.csv',delimiter=',')
 
# First, design the Buterworth filter
N  = 2    # Filter order
Wn = 0.002 # Cutoff frequency
B, A = signal.butter(N, Wn, output='ba')
 
# Second, apply the filter
tempf = signal.filtfilt(B, A, temp)
x = range(1,len(tempf)+1)

np.savetxt('lpf84.csv', tempf, delimiter=',')
'''
fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(x,temp, 'b-')
plt.plot(x,tempf, 'r-',linewidth=2)
plt.ylabel("Temperature (oC)")
plt.legend(['Original','Filtered'])
plt.title("M49")
ax1.axes.get_xaxis().set_visible(False)
plt.show()

print tempf
'''
