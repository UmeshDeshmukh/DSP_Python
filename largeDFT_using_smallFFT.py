import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


N = 8
T = 1.0/200.0
a0 = 0.6
f0 = 25
a1 = 0.33
f1 = 50
N1 = 16

x1 = np.linspace(0.0,N1*T,N1)
y = a0*np.sin(2.0*np.pi*f0*x1) + a1*np.sin(2.0*np.pi*f1*x1)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)


y_even = y[::2]
y_odd  = y[1::2]
y_even2 = np.concatenate((y_even,y_even),axis=None)
y_odd2 = np.concatenate((y_odd,y_odd),axis=None)

n = np.array([[np.zeros(N1)],[np.arange(0,N1,1)]],dtype=complex)
e = np.exp(-2*(np.pi/N1)*n)

xf1 = np.linspace(0.0,N1*T,N1)
y1 = a0*np.sin(2.0*np.pi*f0*x1) + a1*np.sin(2.0*np.pi*f1*x1)

print(np.shape(y_even2))
print(np.shape(y_odd2))
print(e)
yf_N = scipy.fftpack.fft(y1)
yf_N1 = y_even2 + np.dot(y_odd2,e)

fig, ax = plt.subplots(2,sharex=False,sharey=False)
ax[0].plot(xf, 2.0/N * np.abs(yf_N[:N//2]))
ax[0].set_title('original signal')
ax[1].plot(xf1, 2.0/N1 * np.abs(yf_N1[:N1//2]))