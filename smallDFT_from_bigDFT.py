import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


N = 64
T = 1.0/400.0
a0 = 0.6
f0 = 50
a1 = 0.33
f1 = 75

x = np.linspace(0.0,N*T,N)
y = a0*np.sin(2.0*np.pi*f0*x) + a1*np.sin(2.0*np.pi*f1*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
fig, ax = plt.subplots(5,2,sharex=False,sharey=False)
ax[0,0].plot(xf, 2.0/N * np.abs(yf[:N//2]))
ax[0,0].set_title('original signal')

N1 = 128

#Add 64 zeros at the end of signal
y1 = np.concatenate((y,np.zeros(N1-N)),axis=None)
#Add 32 zeros at the start and 32 at the end of the signal
y2 = np.pad(y,pad_width=(N1-N)//2)
#Interleave zeros with the signal
m = np.shape(y2)[0]
y3 = np.zeros((N1),dtype=y.dtype) 
y3[::2] = y
#Replicate the sequence
y4 = np.concatenate((y,y),axis=None)

yf1 = scipy.fftpack.fft(y1)
yf2 = scipy.fftpack.fft(y2)
yf3 = scipy.fftpack.fft(y3)
yf4 = scipy.fftpack.fft(y4)
xf1 = np.linspace(0.0, 1.0/(2.0*T), N1//2)

ax[1,0].plot(xf1, 2.0/N1 * np.abs(yf1[:N1//2]))
ax[2,0].plot(xf1, 2.0/N1 * np.abs(yf2[:N1//2]))
ax[3,0].plot(xf1, 2.0/N1 * np.abs(yf3[:N1//2]))
ax[4,0].plot(xf1, 2.0/N1 * np.abs(yf4[:N1//2]))
ax[1,0].set_title('DFT of 64 zeros at end')
ax[2,0].set_title('DFT of 32 zeros at start and end')
ax[3,0].set_title('DFT of Interleave zeros')
ax[4,0].set_title('DFT of Replicated signal')

yf1_even = yf1[::2]
yf2_even = yf2[::2]
yf3_even = yf3[::2]
yf4_even = yf4[::2]
ax[1,1].plot(xf, 2.0/N * np.abs(yf1_even[:N//2]))
ax[2,1].plot(xf, 2.0/N * np.abs(yf2_even[:N//2]))
ax[3,1].plot(xf, 2.0/N * np.abs(yf3_even[:N//2]))
ax[4,1].plot(xf, 2.0/N * np.abs(yf4_even[:N//2]))
plt.tight_layout()
plt.show()
