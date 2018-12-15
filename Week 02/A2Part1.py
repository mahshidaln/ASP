import numpy as np

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


A = 1.0
f = 10.0
phi = 1.0
fs = 50.0
t = 0.1
output = genSine(A, f, phi, fs, t)
print(output)