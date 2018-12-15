#from utilFunctions import wavread
from scipy.io.wavfile import read
from scipy.io.wavfile import write


def downsampleAudio(inputFile, M):
    """
    Inputs:
    inputFile: file name of the wav file (including path)
    M: downsampling factor (positive integer)
    """
    #(fs, x) = wavread(inputFile)
    (fs, x) = read(inputFile)
    downSampledX = x[0::M]
    rate = int(fs/M)
    write('./sounds/downSampled_' + str(rate) + '.wav', rate, downSampledX)


input = './sounds/32158__zin__piano-2-140bpm.wav'
M = 40
downsampleAudio(input, M)

