import os
import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import welch
from scipy.fft import fft, ifft
from scipy import fftpack
import sys
import numpy
import collections
import shutil
import prepareFile as pf
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
oneRowFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'
toFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv'
fromFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\connectTwoFiles.csv'
file = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\xyz.csv"
# file = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv"

# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# /kaggle/input/eeg-sample/samplingPD.csv
def removeSecondPart():
    for key in list(datW.keys()):
        if key > 3839:
            datW.pop(key)
    return datW

def removeSmallValues():
    for key in list(datW.keys()):
        if float(datW[key]) < 0.0001:
            datW.pop(key)
            # print(str(datW[key]))
    return datW

def sortDict():

    od = collections.OrderedDict(sorted(datW.items()))
    with open(file, "w") as f1:
        for keys, values in od.items():
            print(str(keys) + ': ' + str(values))
            f1.write(str(values) + ' ')
            f1.write('\n')


def mergeLabelsWithChannels(fromFile, toFile, oneRowFile):
    amount = 0
    num_lines1 = sum(1 for line in open(fromFile))
    num_lines2 = sum(1 for line in open(oneRowFile))
    if num_lines1 > num_lines2:
        amount = num_lines2
    else:
        amount = num_lines1
    with open(oneRowFile) as xh:
        with open(fromFile) as yh:
            with open(toFile, "w") as zh:
                xlines = xh.readlines()
                ylines = yh.readlines()
                for i in range(amount - 1):
                        line = ylines[i].strip() + ' ' + xlines[i]
                        zh.write(line)

def copyToOtherFile(fromFile, toFile):
    with open(toFile) as f:
        with open(fromFile, "r+") as f1:
            for line in f:
                f1.write(line)


def cleanFile(copiedFile):
    f = open(copiedFile, 'r+')
    # f.seek(0)
    f.truncate()
    f.close()
f = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\xyz.csv", "a")
col_list = ["ch1", "ch2"]
df_ch1 = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", sep=' ', header=0)
# print(df_ch1)
# print(list(df_ch1.columns.values))
# df_ch1.columns = ["ch1", "ch2"]
# print(df_ch1)
# print("DONE1")
amount = 1
for col in range(len(list(df_ch1.columns.values))):
    # print(df_ch1.columns.values[col])

    #transform to frequency-domain
    #fs = 512                                # Sampling rate (512 Hz)
    fs = 128

    #print("f_s= " + str(f_s))

    # The FFT of the signal
    sig_fft = fftpack.fft(df_ch1[[df_ch1.columns.values[col]]])

    # And the power (sig_fft is of complex dtype)
    power = np.abs(sig_fft)**2

    # The corresponding frequencies
    sample_freq = fftpack.fftfreq(df_ch1.size+1, d=1./fs)

    # print(max(power))
    # for i in range(7680):
    #     print(power[i])
    # print("razem= " + str(np.count_nonzero(power)))


    # Define EEG bands
    eeg_bands = {'Delta': (0, 4),
                 'Theta': (4, 8),
                 'Alpha': (8, 12),
                 'Beta': (12, 30),
                 'Gamma': (30, 47)}

    datW = {}
    df_subbands = pd.DataFrame(columns = ["Delta", "Theta", "Alpha", "Beta", "Gamma"])

    numpy.set_printoptions(threshold=sys.maxsize)
    # Take the mean of the fft amplitude for each EEG band. Enter subbands into dataframe
    eeg_band_fft = dict()
    for band in eeg_bands:
        freq_ix = np.where((abs(power) >= eeg_bands[band][0]) &
                           (abs(power) <= eeg_bands[band][1]))[0]
        # print(band)
        # print(str(freq_ix))
        # print("freq_ix= " + str(freq_ix) + " fft_vals[freq_ix]= " + str(power[freq_ix]))

        # print("razem= " + str(np.count_nonzero(sample_freq[freq_ix])))
        for i in range(np.count_nonzero(sample_freq[freq_ix])):
            datW[freq_ix[i]] = ' '.join(map(str, power[freq_ix][i]))
    removeSecondPart()
    removeSmallValues()
    # print([df_ch1.columns.values[col]])

    if df_ch1.columns.values[col] == 'ch1':
        cleanFile(oneRowFile)
        cleanFile(file)
        sortDict()
        copyToOtherFile(oneRowFile, file)
        print(amount)
        # shutil.copyfile(file, oneRowFile)
    else:
        cleanFile(file)
        sortDict()
        mergeLabelsWithChannels(oneRowFile, toFile, file)
        copyToOtherFile(oneRowFile, toFile)
        amount += 1
        print(amount)



#40 filmików 32 uczestników
print("done")