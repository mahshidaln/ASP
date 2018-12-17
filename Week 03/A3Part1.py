
import numpy as np
from fractions import gcd
from scipy.fftpack import fft

def minimizeEnergySpreadDFT(x, fs, f1, f2):
    """
    Inputs:
    x (numpy array) = input signal
    fs (float) = sampling frequency in Hz
    f1 (float) = frequency of the first sinusoid
    component in Hz
    f2 (float) = frequency of the second sinusoid
    component in Hz
    Output:
    The function should return
    mX (numpy array) = The positive half of the DFT spectrum
    of the M sample segment of x.
    mX is (M/2)+1 samples long
    (M is to be computed)
    """
    T1 = fs/f1
    T2 = fs/f2
    M = int(T1*T2/gcd(T1, T2))
    X = fft(x[:M])
    mX = 20*np.log10(np.abs(X[:int(M/2)+1]))
    return mX
 

def genSine(A, f, phi, fs, t):
    """
    Inputs:
    A (float) = amplitude of the sinusoid
    f (float) = frequency of the sinusoid in Hz
    phi (float) = initial phase of the sinusoid in radians
    fs (float) = sampling frequency of the sinusoid in Hz
    t (float) = duration of the sinusoid (is second)
    Output:
    The function should return a numpy array
    x (numpy array) = The generated sinusoid (use np.cos())
    """
    T = 1/fs
    n = np.arange(0, t, T)
    x = A*np.cos(2*(np.pi)*f*n + phi)
    return x


fs = 48000 #10000
f1 = 300 #80
f2 = 800 #200
phi = 0
A = 1
t = 1
x1 = genSine(A,f1, phi, fs, t)
x2 = genSine(A,f2, phi, fs, t)
x = x1 + x2
output = minimizeEnergySpreadDFT(x, fs, f1, f2)
print(output)