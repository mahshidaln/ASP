#from utilFunctions import wavread
from scipy.io.wavfile import read


def readAudio(inputFile):
    """
    Input:
    inputFile: file path to the wav file
    Output:
    A tuple of the minimum and the maximum value of the audio
    samples, like: (min_val, max_val)
    """
    #(fs, x) = wavread(inputFile)
    (fs, x) = read(inputFile)
    #sample values of the left channel in stereo
    return x[:,0][50000 : 50010]


input = './sounds/32158__zin__piano-2-140bpm.wav'
output = readAudio(input)
print(output)
