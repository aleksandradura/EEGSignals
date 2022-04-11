import pickle
import numpy as np
from pyeeg import spectral_entropy, bin_power
from DEAP import prepareFile as pf
from scipy.stats import entropy
import math
from os import listdir
from os.path import isfile, join
from DEAP import svm, deeplearning, data_clustering
import sys
import pandas as pd
def spectral_entropy(X, Band, Fs, Power_Ratio=None):
    """Compute spectral entropy of a time series from either two cases below:
    1. X, the time series (default)
    2. Power_Ratio, a list of normalized signal power in a set of frequency
    bins defined in Band (if Power_Ratio is provided, recommended to speed up)
    In case 1, Power_Ratio is computed by bin_power() function.
    Notes
    -----
    To speed up, it is recommended to compute Power_Ratio before calling this
    function because it may also be used by other functions whereas computing
    it here again will slow down.
    Parameters
    ----------
    Band
        list
        boundary frequencies (in Hz) of bins. They can be unequal bins, e.g.
        [0.5,4,7,12,30] which are delta, theta, alpha and beta respectively.
        You can also use range() function of Python to generate equal bins and
        pass the generated list to this function.
        Each element of Band is a physical frequency and shall not exceed the
        Nyquist frequency, i.e., half of sampling frequency.
     X
        list
        a 1-D real time series.
    Fs
        integer
        the sampling rate in physical frequency
    Returns
    -------
    As indicated in return line
    See Also
    --------
    bin_power: pyeeg function that computes spectral power in frequency bins
    """

    if Power_Ratio is None:
        Power, Power_Ratio = bin_power(X, Band, Fs)

    Spectral_Entropy = 0
    for i in range(0, len(Power_Ratio) - 1):
        Spectral_Entropy += Power_Ratio[i] * math.log(Power_Ratio[i])
    Spectral_Entropy /= math.log(len(Power_Ratio))  # to save time, minus one is omitted
    return -1 * Spectral_Entropy

def FFT_Processing(channel, band, window_size, step_size, sample_rate, source_path, destination_path):
    meta, valence, arousal = [], [], []
    number_of_movies = 40
    with open(source_path, 'rb') as source_file:
        subject = pickle.load(source_file, encoding='latin')
        for i in range(0, number_of_movies):
            data = subject["data"][i]
            valence.append(subject["labels"][i][0])
            arousal.append(subject["labels"][i][1])
            start = 0
            while 384 + start + window_size <= data.shape[1]:
                meta_array = []
                meta_data = []
                # baseline = baseline + 384
                for j in channel:
                    #slice raw data over 2 seconds
                    X = data[j][384 + start: 384 + start + window_size]
                    Y = bin_power(X, band, sample_rate)
                    # Y = spectral_entropy(X, band, sample_rate, Power_Ratio = None)
                    # print(list(Y[0]))
                    meta_data = meta_data + list(Y[0])
                    # print(meta_data)
                    # meta_data.append(Y)
                meta_array.append(np.array(meta_data))
                # meta_array.append(labels)
                length = np.array(meta_data)
                meta.append(np.array(meta_array))
                with open(destination_path, 'a') as destination_file:
                    for k in range(len(length)):

                        destination_file.write(str(length[k]) + str(' '))
                    destination_file.write('\n')
                start = start + window_size

        meta = np.array(meta)
    return valence, arousal

def label(val, arr, valence_path, arousal_path):
    pf.cleanFile(valence_path)
    for i in range(len(val)):
        for n in range(30):
            with open(valence_path, 'a') as file:
                if val[i] < 4.5:
                    file.write(str(0))
                    file.write('\n')

                else:
                    file.write(str(1))
                    file.write('\n')
    pf.cleanFile(arousal_path)
    for i in range(len(arr)):
        for n in range(30):
            with open(arousal_path, 'a') as file:
                if arr[i] < 4.5:
                    file.write(str(0))
                    file.write('\n')

                else:
                    file.write(str(1))
                    file.write('\n')
    with open('C:\\datasets\\data_preprocessed_python\\1200.dat', 'w') as dest:
        for k in range(len(val)):
            for n in range(30):
                dest.write(str(val[k]))
                if n != 29:
                    dest.write('\n')
            dest.write('\n')
    with open('C:\\datasets\\data_preprocessed_python\\1200_2.dat', 'w') as dest2:
        for k in range(len(arr)):
            for n in range(30):
                dest2.write(str(arr[k]))
                if n != 29:
                    dest2.write('\n')
            dest2.write('\n')
bands = [4,8,12,16,25,45]
# channels = [24, 5, 12, 19, 4, 23, 11, 13, 25, 27, 31]
# channels = [24, 5, 12, 19, 4, 23, 11, 13, 25, 27, 31]
channels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
window_size = 256 #256 #2 sekundy
step_size = 16 #Each 0.125 sec update once
sample_rate = 256 #Sampling rate of 128 Hz
destination_path = 'C:\\datasets\\DEAP\\data_preprocessed_python\\out.dat'
arousal_path = 'C:\\datasets\\DEAP\\data_preprocessed_python\\arousal.csv'
valence_path = 'C:\\datasets\\DEAP\\data_preprocessed_python\\valence.csv'



source_path = 'C:\\datasets\\DEAP\\s\\'
onlyfiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]

for i in range(len(onlyfiles)):

    pf.cleanFile(destination_path)

    val, arr = FFT_Processing(channels, bands, window_size, step_size, sample_rate, source_path + onlyfiles[i], destination_path)

    f = open('C:\\datasets\\DEAP\\data_preprocessed_python\\results.csv', 'a')
    print('-----------------------------------', file = f)
    print('-----------------------------------', file = f)
    print('-----------------------------------', file = f)
    print(str('User:' + str(i + 1)), file = f)
    print('-----------------------------------', file = f)
    print('-----------------------------------', file = f)
    print('-----------------------------------', file = f)
    pf.deleteLatestColumn(destination_path)
    label(val, arr, valence_path, arousal_path)
    print('-----------------------------------', file = f)
    print('Valence:', file = f)
    print('-----------------------------------', file = f)
    classification = svm.svm_classifier(valence_path, destination_path)
    print('SVM Accuracy: ' + classification, file = f)
    loss, acc = deeplearning.CNN(destination_path, valence_path)
    print('CNN: loss - ' + str(round(loss * 100, 2)) + ', accuracy - ' + str(round(acc * 100, 2)), file = f)
    print('KMEANS: ', file = f)
    q,w,e,r,t, qwerty = data_clustering.kmeans(2, destination_path, valence_path)
    print('Accuracy: ', qwerty, file = f)
    print('Rand score: ', q, file = f)
    print('Homogeneity score: ', w, file = f)
    print("Completeness: ", e, file = f)
    print("V-measure: ", r, file = f)
    print("Adjusted Mutual Information: ", t, file = f)
    print('-----------------------------------', file = f)
    print('-----------------------------------', file = f)
    print('Arousal:', file = f)
    print('-----------------------------------', file = f)

    clas = svm.svm_classifier(arousal_path, destination_path)
    print('SVM Accuracy: ' +  clas, file = f)
    lo, ac = deeplearning.CNN(destination_path, arousal_path)
    print('CNN: loss - ' +  str(round(lo * 100, 2)) + ', accuracy - ' + str(round(ac * 100, 2)), file = f)

    print('KMEANS: ', file = f)
    a, b,c,d,e, qwerty = data_clustering.kmeans(2, destination_path, arousal_path)
    print('Accuracy: ', qwerty, file = f)
    print('Rand score: ', a, file = f)
    print('Homogeneity score: ', b, file = f)
    print("Completeness: ", c, file = f)
    print("V-measure: ", d, file = f)
    print("Adjusted Mutual Information: ", e, file = f)
# sys.stdout.close()



