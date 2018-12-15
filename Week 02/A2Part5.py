import numpy as np
from A2Part3 import DFT


def genMagSpec(x):
    """
    Input:
    x (numpy array) = input sequence of length N
    Output:
    The function should return a numpy array
    magX (numpy array) = The length N magnitude spectrum of
    the input sequence x
    """
    X = DFT(x)
    magX = np.array(np.abs(X))
    return magX


x = np.array([1, 2, 3, 4])
output = genMagSpec(x)
print(output)