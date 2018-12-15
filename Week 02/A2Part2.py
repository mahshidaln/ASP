import numpy as np


def genComplexSine(k, N):
    """
    Inputs:
    k (integer) = frequency index of the complex sinusoid
    of the DFT
    N (integer) = length of complex sinusoid in samples
    Output:
    The function should return a numpy array
    cSine (numpy array) = The generated complex sinusoid
    (length N)
    """     
    n = np.arange(N)
    cSien = np.exp(-2j*np.pi*k*n/N)
    return cSien


N = 5
k = 1
output = genComplexSine(k, N)
#print(output)
    