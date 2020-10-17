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

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
oneRowFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\OneRowFile.csv'
toFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv'
file = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\xyz.csv"
label0 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_0_01.dat'
label1 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_1_01.dat'
# file = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv"
amount = 0
valence = ['1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1']
arousal = ['1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1']
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
f = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\xyz.csv", "a")
df_ch1 = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", sep=' ', header=0, low_memory=False)

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
            # print(str(keys) + ': ' + str(values))
            f1.write(str(values) + ' ')
            f1.write('\n')

def countingRows(oneRowFile, file):
    num_lines1 = sum(1 for line in open(oneRowFile))
    num_lines2 = sum(1 for line in open(file))
    if int(num_lines1) < int(num_lines2):
        amount = num_lines1
        print(str(amount) + ' = ' + str(num_lines1))
    else:
        amount = num_lines2
        print(str(amount) + ' = ' + str(num_lines2))
    return amount

def mergeLabelsWithChannels(oneRowFile, toFile, file):
    # amount = countingRows(oneRowFile, file)
    # print(amount)
    with open(file) as xh:
        with open(oneRowFile) as yh:
            with open(toFile, "w") as zh:
                xlines = xh.readlines()
                ylines = yh.readlines()
                for i in range(countingRows(oneRowFile, file)):
                        line = ylines[i].strip() + ' ' + xlines[i]
                        zh.write(line)

def copyToOtherFile(oneRowFile, toFile):
    with open(toFile) as f:
        with open(oneRowFile, "w") as f1:
            for line in f:
                f1.write(line)


def cleanFile(copiedFile):
    f = open(copiedFile, 'r+')
    # f.seek(0)
    f.truncate()
    f.close()



def fastFourierTransform():
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

    return power, sample_freq

def add01ValueForLabel():
    power, sample_freq = fastFourierTransform()
    countAll = []
    count = 0
    countingRows = {}
    for i in range(len(power)):
        if power[i] == 0:
            count += 1
            countingRows[i] = power[i - 1]
            countAll.append(i)
            # countingRows.append(i + 1)
    # print("razem= " + str(np.count_nonzero(power)))
    # print("0 counter= " + str(count))
    # for x, y in countingRows.items():
        # print(str(x) + ' ' + str(y))
    k, a = 0, 0
    with open(label1, 'w') as fi:
        for z in range(len(arousal)):
            a = countAll[k]
            for h in range(a):
                fi.write(arousal[z])
                fi.write("\n")
            k += 1
add01ValueForLabel()





amount = 1
for col in range(len(list(df_ch1.columns.values))):

    power, sample_freq = fastFourierTransform()

    # Define EEG bands
    eeg_bands = {
                'Delta': (0, 4),
                 'Theta': (4, 8),
                 'Alpha': (8, 12),
                 'Beta': (12, 30),
                 'Gamma': (30, 45)
    }

    datW = {}
    df_subbands = pd.DataFrame(columns=["Delta", "Theta", "Alpha", "Beta", "Gamma"])

    # numpy.set_printoptions(threshold=sys.maxsize)
    # Take the mean of the fft amplitude for each EEG band. Enter subbands into dataframe
    eeg_band_fft = dict()
    for band in eeg_bands:
        freq_ix = np.where((abs(power) >= eeg_bands[band][0]) &
                           (abs(power) <= eeg_bands[band][1]))[0]
        # print(band)
        # print(str(freq_ix))
        # print(" fft_vals[freq_ix]= " + str(power[freq_ix]))

        # print("razem= " + str(np.count_nonzero(sample_freq[freq_ix])))
        for i in range(np.count_nonzero(sample_freq[freq_ix])):
            datW[freq_ix[i]] = ' '.join(map(str, power[freq_ix][i]))
    # removeSecondPart()
    # removeSmallValues()
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