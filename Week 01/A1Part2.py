#from utilFunctions import wavread
from scipy.io.wavfile import read


def minMaxAudio(inputFile):
    """
    Input:
    inputFile: file path to the wav file
    Output:
    A tuple of the minimum and the maximum value of the audio
    samples, like: (min_val, max_val)
    """
    #(fs, x) = wavread(inputFile)
    (fs, x) = read(inputFile)
    #min & max values of the left channel in stereo
    minMaxTup = (min(x[:,0]), max(x[:,0]))
    return minMaxTup


input = './sounds/32158__zin__piano-2-140bpm.wav'
output = minMaxAudio(input)
print(output)
