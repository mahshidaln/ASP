#from utilFunctions import wavread
from scipy.io.wavfile import read
from A1Part1 import readAudio

def hopSamples(x,M):
    """
    Inputs:
    x: input numpy array
    M: hop size (positive integer)
    Output:
    A numpy array containing every Mth element in x, starting
    from the first element in x.
    """
    return x[0::M]


input = './sounds/32158__zin__piano-2-140bpm.wav'
x = readAudio(input)
M = 2
output = hopSamples(x, M)
print(output)
