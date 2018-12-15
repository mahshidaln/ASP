import numpy as np


def IDFT(X):
    """
    Input:
    X (numpy array) = frequency spectrum (length N)
    Output:
    The function should return a numpy array of length N
    x (numpy array) = The IDFT of the frequency spectrum X
    (length N)
    """
    N = len(X)
    x = 1/N * np.array([(np.sum(X*genComplexSine2(n, N))) for n in range (N)])
    return x

def genComplexSine2(n, N):
    k = np.arange(N)
    cSien = np.exp(2j*np.pi*k*n/N)
    return cSien


#X = np.array([10.+0.00000000e+00j, -2.+2.00000000e+00j, -2.-9.79717439e-16j, -2.-2.00000000e+00j])
X = np.array([1,1,1,1])
output = IDFT(X)
print(output.astype(int))