import sys
sys.path.append('../sms-tools/software/models/')
from dftModel import dftAnal
from dftModel import dftSynth
import numpy as np
from scipy.signal import get_window

def zpFFTsizeExpt(x, fs):
    """
    Inputs:
    x (numpy array) = input signal (2*M = 512 samples long)
    fs (float) = sampling frequency in Hz
    Output:
    The function should return a tuple (mX1_80, mX2_80, mX3_80)
    mX1_80 (numpy array): The first 80 samples of the magnitude
    spectrum output of dftAnal for Case-1
    mX2_80 (numpy array): The first 80 samples of the magnitude
    spectrum output of dftAnal for Case-2
    mX3_80 (numpy array): The first 80 samples of the magnitude
    spectrum output of dftAnal for Case-3
    The first few lines of the code to generate xseg and the windows
    8
    have been written for you, please use it and do not modify it.
    """
    M = len(x)/2
    xseg = x[:M]
    w1 = get_window('hamming',M)
    w2 = get_window('hamming',2*M)
    mX1 = dftAnal(xseg, w1, w1.size())[0]
    mX2 = dftAnal(x, w2, w2.size())[0]
    mX3 = dftAnal(xseg, w1, w2.size())[0]
    mX1_80 = mX1[:80]
    mX2_80 = mX2[:80]
    mX3_80 = mX3[:80]
    return mX1_80, mX2_80, mX3_80