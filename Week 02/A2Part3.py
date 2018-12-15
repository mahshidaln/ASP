import numpy as np
from A2Part2 import genComplexSine


def DFT(x):
    """
    Input:
    x (numpy array) = input sequence of length N
    Output:
    The function should return a numpy array of length N
    X (numpy array) = The N point DFT of the input sequence x
    """
    N = len(x)
    X = np.array([(np.sum(x*genComplexSine(k, N))) for k in range(N)])
    return X


x = np.array([1, 2, 3, 4])
output = DFT(x)
#print(output)