import numpy as np
from fractions import gcd
from scipy.fftpack import fft


def optimalZeropad(x, fs, f):
    """
    Inputs:
    x (numpy array) = input signal of length M
    fs (float) = sampling frequency in Hz
    f (float) = frequency of the sinusoid in Hz
    Output:
    The function should return
    mX (numpy array) = The positive half of the DFT spectrum
    of the N point DFT after zero-padding input x
    appropriately (zero-padding length to be computed).
    mX is (N/2)+1 samples long
    """
    T = int(fs/f)
    M = len(x)
    zpn = T - (M % T)
    zp = np.zeros(zpn)
    x = np.append(x, zp)
    N = len(x)
    X = fft(x)
    mX = 20*np.log10(abs(X[:int(N/2)+1]))
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


fs = 1000 
f = 100
M = 25 
phi = 0
A = 1
t = 0.025
x = genSine(A,f, phi, fs, t)
output = optimalZeropad(x, fs, f)
print(output)