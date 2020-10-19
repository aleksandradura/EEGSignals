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

oneRowFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\OneRowFile.csv'
toFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv'
file = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\xyz.csv"
fftValues = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\fftValues.csv"
a = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\aaa.csv"
b = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\bbb.csv"
label0 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\0.csv'
label1 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\1.csv'

amount = 1
valence = ['1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1']
arousal = ['1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1']
# ix_rows = ['175', '1259', '1571', '3688', '4790', '5206', '6058', '7594', '8362', '8418', '10167', '12308', '13039', '13199', '13410', '15164', '17128', '17749', '18586', '20779', '21988', '22443', '23430', '23734', '24707', '25050', '27307', '28959', '28970', '30015', '32346', '37712', '37780', '38371', '40871', '40958', '42361', '43417', '45573', '47018', '47359', '49799', '50553', '51178', '52037', '53899', '54606', '55235', '56221', '56901', '58015', '58850', '61723', '62338', '65628', '65872', '65923', '67999', '70327', '72192', '72834', '75006', '75237', '75492', '81176', '81259', '83467', '84642', '85117', '85130', '85872', '86656', '87334', '89336', '89537', '89818', '89984', '91120', '91687', '91728', '93330', '94112', '94763', '97175', '98216', '98491', '99761', '99838', '101502', '101667', '103773', '105980', '106139', '107402', '107466', '109818', '110335', '112792', '113436', '113750', '116714', '117491', '120081', '120853', '121826', '122806', '122824', '124402', '124475', '125097', '126844', '127086', '127538', '127736', '129013', '131323', '135110', '135143', '135705', '136489', '138037', '138793', '140029', '140063', '140621', '141239', '141526', '141643', '144122', '147034', '148411', '150274', '150669', '151803', '153843', '154085', '156093', '157618', '157711', '157946', '158575', '167857', '168466', '170160', '170747', '173761', '175150', '175248', '175501', '176431', '177201', '181398', '181407', '181583', '183266', '186806', '188205', '191006', '191008', '192609', '193392', '194164', '194712', '194885', '197638', '198194', '199935', '200202', '202497', '204162', '204229', '206502', '207279', '209198', '210401', '211263', '212542', '213417', '215443', '215623', '216086', '216301', '221912', '222446', '223013', '226290', '226949', '227122', '227851', '228153', '228175', '229034', '231674', '232443', '234825', '234977', '235718', '236557', '236576', '236624', '237280', '239294', '239464', '239624', '242175', '242225', '243750', '246033', '246992', '249284', '249789', '250187', '250242', '252571', '253139', '255134', '256828', '257422', '259745', '262426', '262518', '266224', '267501', '271811', '273962', '274899', '275256', '276562', '280052', '280386', '281365', '282197', '283126', '284176', '284327']

file_x = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'
onlyRowNumbforThreeCol = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\onlyRowNumbforThreecol.csv'
f = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\xyz.csv", "a")
df_ch1 = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", sep=' ', header=0, low_memory=False)

listOfthresholds = []
def threshold():
    for k in range(40):
        listOfthresholds.append((k + 1) * 7680)
    return listOfthresholds
t = threshold()


def cleanFile(copiedFile):
    f = open(copiedFile, 'r+')
    # f.seek(0)
    f.truncate()
    f.close()
#counting 0 and 1

def select0or1LabelValues(x, numb):
    cleanFile(x)
    for z in range(len(numb)):
        for l in range(len(t)):
            if int(numb[z]) < int(t[l]):
                # print(str(z) + ' : ' + str(ix_rows[z]) + ' - ' + str(l ) + ' - ' + str(t[l]))
                with open(x, 'a') as lab:
                    lab.write(valence[l])
                    lab.write('\n')
                    break

# print(len(ix_rows))
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
#zapisać jeszcze odrębne wiersze ix_freq do pliku innego
def sortDict():
    list = []
    od = collections.OrderedDict(sorted(datW.items()))
    with open(file, "w") as f1:
        # with open(onlyRowNumbforThreeCol, 'a') as f2:
        for keys, values in od.items():
            # print(str(keys) + ': ' + str(values))
            f1.write(str(values) + ' ')
            f1.write('\n')
            # f2.write(str(keys) + ' ')
            # f2.write('\n')
def sortDictByRow():
    list = []
    od = collections.OrderedDict(sorted(datW.items()))
    with open(onlyRowNumbforThreeCol, "w") as f1:
        # with open(onlyRowNumbforThreeCol, 'a') as f2:
        for keys, values in od.items():
            # print(str(keys) + ': ' + str(values))
            f1.write(str(keys) + ' ')
            f1.write('\n')
            # f2.write(str(keys) + ' ')
            # f2.write('\n')


def countingRows(oneRowFile, file):
    num_lines1 = sum(1 for line in open(oneRowFile))
    num_lines2 = sum(1 for line in open(file))
    if int(num_lines1) < int(num_lines2):
        amount = num_lines1
        # print(str(amount) + ' = ' + str(num_lines1))
    else:
        amount = num_lines2
        # print(str(amount) + ' = ' + str(num_lines2))
    return amount


def mergeLabelsWithChannels(oneRowFile, toFile, file):
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

def selectNumberOfTheSameRows():
    headers = ['1','2','3']
    ix = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\bbb.csv", sep=' ', names = headers)
    x1 = ix['1'].tolist()
    x2 = ix['2'].tolist()
    x3 = ix['3'].tolist()
    # print(x1)
    lis = []
    for i in range(len(x1)) :
    # print(x1[i])
        for j in range(len(x2)) :
            if x1[i] == x2[j]:
                # print(x2[j])
                for k in range(len(x3)):
                    if x1[i] == x3[k]:
                        # print(str(x1[i]) + ' ' + str(x2[j]) + ' ' + str(x3[k]))
                        lis.append(x1[i])
    # print(lis)
    return lis
# selectNumberOfTheSameRows()
def fastFourierTransform():
    #transform to frequency-domain
    fs = 128

    # The FFT of the signal
    sig_fft = fftpack.fft(df_ch1[[df_ch1.columns.values[col]]])

    # And the power (sig_fft is of complex dtype)
    power = np.abs(sig_fft)**2

    # The corresponding frequencies
    sample_freq = fftpack.fftfreq(df_ch1.size+1, d=1./fs)

    return power, sample_freq
def sf():
    with open(file_x, 'a') as pq:
        pq.write(' '.join(map(str, power[freq_ix][i])))
        pq.write('\n')


for col in range(len(list(df_ch1.columns.values))):

    power, sample_freq = fastFourierTransform()
    #save all fft values
    # if df_ch1.columns.values[col] == 'ch1':
    #     with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\fftValues.csv", 'w') as ffff:
    #         # fft.write(str(power))
    #         for i in range(len(power)):
    #             ffff.write(' '.join(map(str, power[i])) + ' ')
    #             ffff.write('\n')

    # if df_ch1.columns.values[col] == 'ch32':
    #     add01ValueForLabel(power, valence)
    #     add01ValueForLabel(power, arousal)
    # print(sample_freq)
    countAll = []
    count = 0
    # countingRows = {}
    # for i in range(len(power)):
    #     if power[i] == 0:
    #         count += 1
    #         countingRows[i] = power[i - 1]
    #         countAll.append(i)
    # print("razem= " + str(np.count_nonzero(power)))
    # print("0 counter= " + str(count))
    # for x in range(len(countAll)):
    #     print(str(x) + ': ' + str(countAll[x]))
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

    numpy.set_printoptions(threshold=sys.maxsize)
    # Take the mean of the fft amplitude for each EEG band. Enter subbands into dataframe
    eeg_band_fft = dict()
    cleanFile(file_x)
    for band in eeg_bands:
        freq_ix = np.where((abs(power) >= eeg_bands[band][0]) &
                           (abs(power) <= eeg_bands[band][1]))[0]
        # print(band)
        # print(str(freq_ix))
        # print(" fft_vals[freq_ix]= " + str(power[freq_ix]))

        print("razem= " + str(np.count_nonzero(sample_freq[freq_ix])))
        for i in range(np.count_nonzero(sample_freq[freq_ix])):
            datW[freq_ix[i]] = ' '.join(map(str, power[freq_ix][i]))
    #         for k in range(len(ix_rows)):
    #             if int(freq_ix[i]) == int(ix_rows[k]):
    #                 # print(str(power[freq_ix][i]))
    #                 if df_ch1.columns.values[col] == 'ch1':
    #                     sf()
    #                 else:
    #                     sf()
    #                     # copyToOtherFile(oneRowFile, file_x)
    #
    # if df_ch1.columns.values[col] == 'ch1':
    #     copyToOtherFile(oneRowFile, file_x)
    # else:
    #     mergeLabelsWithChannels(oneRowFile, toFile, file_x)
    #     copyToOtherFile(oneRowFile, toFile)

    # removeSecondPart()
    # removeSmallValues()


    # if df_ch1.columns.values[col] == 'ch1':
    #     cleanFile(oneRowFile)
    #     cleanFile(file)
    #     cleanFile(a)
    #     cleanFile(onlyRowNumbforThreeCol)
    #     sortDict()
    #     copyToOtherFile(oneRowFile, file)
    #     sortDictByRow()
    #     copyToOtherFile(a, onlyRowNumbforThreeCol)
    #     print(amount)
    #
    # else:
    #     cleanFile(onlyRowNumbforThreeCol)
    #     cleanFile(file)
    #     sortDict()
    #     mergeLabelsWithChannels(oneRowFile, toFile, file)
    #     copyToOtherFile(oneRowFile, toFile)
    #     sortDictByRow()
    #     mergeLabelsWithChannels(a, b, onlyRowNumbforThreeCol)
    #     copyToOtherFile(a, b)
    #     amount += 1
    #     print(amount)


    # countAll.clear()
numbOfTheSameRows = []
numbOfTheSameRows = selectNumberOfTheSameRows()
select0or1LabelValues(label0, numbOfTheSameRows)
select0or1LabelValues(label1, numbOfTheSameRows)
print("done")