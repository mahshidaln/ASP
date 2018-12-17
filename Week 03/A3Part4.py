import sys
sys.path.append('../sms-tools/software/models/')
from dftModel import dftAnal
from dftModel import dftSynth
import numpy as np
from scipy.signal import get_window

def suppressFreqDFTmodel(x, fs, N):
    """
    Input:
    x (numpy array) = input signal of length M (odd)
    fs (float) = sampling frequency (Hz)
    N (positive integer) = FFT size
    Output:
    The function should return a tuple (y, yfilt)
    y (numpy array) = Output of the dftSynth() without
    filtering (M samples long)
    yfilt = Output of the dftSynth() with filtering
    (M samples long)
    The first few lines of the code have been written for you,
    do not modify it.
    """
    M = len(x)
    w = get_window('hamming', M)
    outputScaleFactor = sum(w)
    mX, pX = dftAnal(x, w, N)
    mXfilt = mX.copy()
    y = dftSynth(mX, pX, M) * outputScaleFactor
    below70 = int(np.ceil(70 * N / fs))
    mXfilt[:below70] = -120
    yfilt = dftSynth(mXfilt, pX, M) * outputScaleFactor
    return y, yfilt

