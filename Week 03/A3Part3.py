import numpy as np
from fractions import gcd
from scipy.fftpack import fft

def testRealEven(x):
    """
    Inputs:
    x (numpy array)= input signal of length M (M is odd)
    Output:
    The function should return a tuple (isRealEven, dftbuffer, X)
    isRealEven (boolean) = True if the input x is real and even,
    and False otherwise
    dftbuffer (numpy array, possibly complex) = The M point zero
    phase windowed version of x
    X (numpy array, possibly complex) = The M point DFT
    of dftbuffer
    """
    M = len(x)
    hM1 = int(np.floor((M+1)/2)) #3
    hM2 = int(np.floor(M/2)) #2
    dftbuffer = np.zeros(M)
    dftbuffer[:hM1] = x[hM2:] #0 1 2
    dftbuffer[-hM2:] = x[:hM2] #
    X = fft(dftbuffer)
    test1 = 0
    test2 = 0
    for k in range(-hM2, hM1):
        if(np.abs(X[k]) == np.abs(X[-k])):
            test1 = test1 + 1
    for k in range(-hM2, hM1):
        if(np.imag(X[k]) == 0):
            test2 = test2 + 1 
    isRealEven = True if (test1 == M and test2 == M) else False
    return(isRealEven, dftbuffer, X)


x = np.array([ 2, 3, 4, 3, 2 ])
output = testRealEven(x)
print(output)
