#https://www.dsprelated.com/showarticle/800.php

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

#########################################################
#Method 1
fig, ax = plt.subplots(3,2,sharex=False,sharey=False)

ax[0,0].plot(np.real(y))
ax[0,1].plot(np.imag(y))
ax[0,0].set_title('Real part of original signal')
ax[0,1].set_title('Imag part of original signal')

ax[1,0].plot(xf, 2.0/N * np.real(yf[:N//2]))
ax[1,1].plot(xf, 2.0/N * np.imag(yf[:N//2]))
ax[1,0].set_title('Real part of DFT')
ax[1,1].set_title('Imag part of DFT')

yf2 = scipy.fftpack.fft(yf)

sig1 = np.concatenate((np.real(yf2)[0],np.real(yf2)[-1:0:-1]),axis=None)
sig2 = np.concatenate((np.imag(yf2)[0],np.imag(yf2)[-1:0:-1]),axis=None)
ax[2,0].plot(1.0/N * sig1)
ax[2,1].plot(1.0/N * sig2)
ax[2,0].set_title('Real part of reconstructed signal')
ax[2,1].set_title('Imag part of reconstructed signal')
fig.suptitle('Inverse FFT Using the Forward FFT:Method 1')

##########################################################
#Method 3
yf_real = np.real(yf)
yf_imag = np.imag(yf)
#y_in = complex(yf_imag,yf_real)
y_in = yf_imag + 1j* yf_real
yf3 = scipy.fftpack.fft(y_in)
fig2, ax2 = plt.subplots(2,2,sharex=False,sharey=False)
sig3_imag = (1.0/N)*np.real(yf3)
sig3_real = (1.0/N)*np.imag(yf3)
ax2[0,0].plot(np.real(y))
ax2[0,1].plot(np.imag(y))
ax2[0,0].set_title('Real part of original signal')
ax2[0,1].set_title('Imag part of original signal')
ax2[1,0].plot(sig3_real)
ax2[1,1].plot(sig3_imag)
ax2[1,0].set_title('Real part of reconstructed signal')
ax2[1,1].set_title('Imag part of reconstructed signal')
fig2.suptitle('Inverse FFT Using the Forward FFT:Method 3')
##########################################################
yf_real = np.real(yf)
yf_imag = np.imag(yf)
#y_in = complex(yf_imag,yf_real)
y_in = yf_real - 1j* yf_imag
yf4 = scipy.fftpack.fft(y_in)
fig4, ax4 = plt.subplots(2,2,sharex=False,sharey=False)
sig4_imag = (-1.0/N)*np.imag(yf4)
sig4_real = (1.0/N)*np.real(yf4)
ax4[0,0].plot(np.real(y))
ax4[0,1].plot(np.imag(y))
ax4[0,0].set_title('Real part of original signal')
ax4[0,1].set_title('Imag part of original signal')
ax4[1,0].plot(sig4_real)
ax4[1,1].plot(sig4_imag)
ax4[1,0].set_title('Real part of reconstructed signal')
ax4[1,1].set_title('Imag part of reconstructed signal')
fig4.suptitle('Inverse FFT Using the Forward FFT:Method 4')
##########################################################
plt.tight_layout()
plt.show()
