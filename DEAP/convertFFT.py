import numpy as np # linear algebra
import pandas as pd # data processing
from scipy import fftpack
import collections

filePath = 'C:\\datasets\\data_preprocessed_python\\'
oneRowFile = filePath + 'arffFiles\\OneRowFile.csv'
toFile = filePath + 'asdf.csv'
file = filePath + "xyz.csv"
fftValues = filePath + "fftValues.csv"
a = filePath + "aaa.csv"
b = filePath + "bbb.csv"
label0 = filePath + '0.csv'
label1 = filePath + '1.csv'
k = filePath + 'k.csv'
q = filePath + "q.csv"

# valence = ["0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "1", "1", "0", "1", "0"]
# arousal = ["1", "1", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "1", "0", "1", "1", "0", "1", "0", "0", "0", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "0", "0", "1", "1", "1", "0"]
file_x = filePath + 'RandomTree.csv'
onlyRowNumbforThreeCol = filePath + 'onlyRowNumbforThreecol.csv'
f = open(filePath + "xyz.csv", "a")
df_ch1 = pd.read_csv("C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels.csv", sep=' ', low_memory=False, header=None)
df_ch1.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32']
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

def select0or1LabelValues(x, numb, file):
    cleanFile(x)
    for z in range(len(numb)):
        for l in range(len(t)):
            if int(numb[z]) < int(t[l]):
                # print(str(z) + ' : ' + str(ix_rows[z]) + ' - ' + str(l ) + ' - ' + str(t[l]))
                with open(x, 'a') as lab:
                    lab.write(file[l])
                    lab.write('\n')
                    break

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
        for keys, values in od.items():
            f1.write(str(values) + ' ')
            f1.write('\n')

def sortDictByRow():
    list = []
    od = collections.OrderedDict(sorted(datW.items()))
    with open(onlyRowNumbforThreeCol, "w") as f1:
        for keys, values in od.items():
            f1.write(str(keys) + ' ')
            f1.write('\n')

def countingRows(oneRowFile, file):
    num_lines1 = sum(1 for line in open(oneRowFile))
    num_lines2 = sum(1 for line in open(file))
    if int(num_lines1) < int(num_lines2):
        amount = num_lines1
    else:
        amount = num_lines2
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
    # headers = ['1', '2', '3', '4', '5']
    ix = pd.read_csv(filePath + "bbb.csv", sep=' ')
    ix.columns = ['1', '2', '3', '4']
    x1 = ix['1'].tolist()
    x2 = ix['2'].tolist()
    x3 = ix['3'].tolist()
    x4 = ix['4'].tolist()
    # x5 = ix['5'].tolist()
    # x6 = ix['6'].tolist()

    lis = []
    for i in range(len(x1)):
        for j in range(len(x2)):
            if x1[i] == x2[j]:
                for k in range(len(x3)):
                    if x1[i] == x3[k]:
                        for z in range(len(x4)):
                            if x1[i] == x4[z]:
                        #         print(str(x1[i]) + ' ' + str(x2[j]))
                                # for p in range(len(x5)):
                                #     if x1[i] == x5[p]:
                                #         for g in range(len(x6)):
                                #             if x1[i] == x6[g]:
                                print(str(x1[i]) + ' ' + str(x2[j]) + ' ' + str(x3[k]))
                                lis.append(x1[i])
    return lis
# print(selectNumberOfTheSameRows())
from scipy.fft import fft, ifft

# with open('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels2.csv', 'r+') as f:
#     # print(col)
#     # x = f.readlines()
#     for idxFile, fileLine in enumerate(f):
#         # print('tujestem')
#         f.write("Cokolwiek")

# fastFourierTransform = fft(df_ch1[[df_ch1.columns.values[1]]])
# power = np.abs(fastFourierTransform) ** 2
# with open('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels2.csv', 'r+') as f:
#     f.truncate(0)
#     for idxu, line in enumerate(power):
#         f.write(str(line).strip("[]") + '\n')
# original = r'C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels3.csv'
# target = r'C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels2.csv'
# import shutil
# for col in range(len(list(df_ch1.columns.values))):
#     fastFourierTransform = fft(df_ch1[[df_ch1.columns.values[col]]])
#     power = np.abs(fastFourierTransform) ** 2
#     if col == 0:
#         with open('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels2.csv', 'r+') as f:
#             f.truncate(0)
#             for idxu, line in enumerate(power):
#                 f.write(str(line).strip("[]") + '\n')
#     elif col in range(1, 32):
#         with open('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels3.csv', 'r+') as fi:
#             with open('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels2.csv', 'r+') as f:
#                 print(col)
#         # x = f.readlines()
#                 for idxFile, fileLine in enumerate(f):
#                     # print(str(fileLine))
#                     # print(str(fileLine))
#                     for idx, linec in enumerate(power):
#                         # print(linec)
#                         if idxFile == idx:
#                             # print(str(fileLine).strip() + " " + str(linec).strip("[]"))
#                             # print("Tu")
#                             # print(str(fileLine).strip())
#
#                             fi.write(str(fileLine).strip() + " " + str(linec).strip("[]") + '\n')
#                 shutil.copyfile(original, target)

        # print(line)
# y = fftpack.fft(df_ch1[[df_ch1.columns.values[0]]])
# print(df_ch1[[df_ch1.columns.values[0]]])
# print(power[-2])
# print(power.min())
# print(len(y))
# print(y.min())
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


amount = 1


# column = df_ch1["ch1"]
# max_val = column.max()
# print(max_val)
# min_val = column.min()
# print(min_val)
for col in range(len(list(df_ch1.columns.values))):
    power, sample_freq = fastFourierTransform()
    # print(col)
    # Define EEG bands
    eeg_bands = {
                'Delta': (0.0, 4.0),
                 'Theta': (4.0, 8.0),
                 'Alpha': (8.0, 13.0),
                 'Beta': (13.0, 30.0),
                 'Gamma': (30.0, 500000.0)
    }

    datW = {}
    df_subbands = pd.DataFrame(columns=["Delta", "Theta", "Alpha", "Beta", "Gamma"])

    # numpy.set_printoptions(threshold=sys.maxsize)
    # Take the mean of the fft amplitude for each EEG band. Enter subbands into dataframe
    eeg_band_fft = dict()
    # cleanFile(file_x)
    res = []
    # res.append(sample_freq.sort())
    # print(res)
    # print(np.where(abs(power))[0])
    # print(np.where(abs(power))[0])
    for band in eeg_bands:
        freq_ix = np.where((abs(power) >= eeg_bands[band][0]) &
                           (abs(power) <= eeg_bands[band][1]))[0]
        # print(power.min())
        # print(power.max())
        # print(band)
        # print(str(freq_ix))
        # print(" fft_vals[freq_ix]= " + str(power[freq_ix]))
        # res.append(freq_ix)
        # print("razem= " + str(np.count_nonzero(sample_freq[freq_ix])))
        for i in range(np.count_nonzero(sample_freq[freq_ix])):
            datW[freq_ix[i]] = ' '.join(map(str, power[freq_ix][i]))
        # res.extend(freq_ix)
        # print(res)
    # col = 32
    if df_ch1.columns.values[col] == 'ch1':
        cleanFile(oneRowFile)
        cleanFile(file)
        cleanFile(a)
        cleanFile(onlyRowNumbforThreeCol)
        sortDict()
        copyToOtherFile(oneRowFile, file)
        sortDictByRow()
        copyToOtherFile(a, onlyRowNumbforThreeCol)
        print(amount)
    else:
    # if df_ch1.columns.values[col] == 'ch3':
        cleanFile(onlyRowNumbforThreeCol)
        cleanFile(file)
        sortDict()
        mergeLabelsWithChannels(oneRowFile, toFile, file)
        copyToOtherFile(oneRowFile, toFile)
        sortDictByRow()
        mergeLabelsWithChannels(a, b, onlyRowNumbforThreeCol)
        copyToOtherFile(a, b)
        amount += 1
        print(amount)

# numb = selectNumberOfTheSameRows()
# print(numb)
# select0or1LabelValues(label0, ix_rows, valence)
# select0or1LabelValues(label1, ix_rows, arousal)

def takeR(n):
    df = pd.read_csv(filePath + "bbb.csv", sep=' ')
    df.columns = ['1', '2', '3', '4']
    index = df.index
    numb_of_rows = len(index)
    df.insert(0, 'row_num', range(0,len(df)))
    ro = []
    # u = df.columns.values
    # for col in range(len(list(df.columns.values)) - 1):
    #     n = '2'
    for i in range(len(ix_rows)):
        # print(ix_rows[i])
        # if df.columns.values[n] == '2':
        k = df.loc[df[n] == int(ix_rows[i])]
        # print(k.row_num)
        ro.append(int(k.row_num))

    # k = df['1'].where(df['1'] == 1630)
    # print(k)

    # for j in range(len(ro)):
    #     print(ro[j])
    return ro

def takeValue(n, t):
    k = filePath + 'k.csv'
    cleanFile(k)
    df_asdf = pd.read_csv(filePath + "asdf.csv", sep=' ')
    df_asdf.columns =  ['ch1', 'ch2', 'ch3', 'ch4']
    df_asdf.insert(0, 'row_num', range(0, len(df_asdf)))
    # print(df_asdf)
    r = takeR(n)
    # print(r)
    with open(k, 'a') as file:
        for i in range(len(r)):
            k = df_asdf.loc[df_asdf['row_num'] == int(r[i])]
            # print(float(k[t]))
            file.write(str(float(k[t])) + str(' '))
            file.write('\n')
        print(k.ch1)


# first = ['1', '2', '3']
# sec = ['ch1', 'ch2', 'ch3']
# for i in range(len(first)):
#     if first[i] == '1':
#         cleanFile(q)
#         takeValue(first[i], sec[i])
#         copyToOtherFile(q, k)
#     else:
#         takeValue(first[i], sec[i])
#         mergeLabelsWithChannels(q, fftValues, k)
#         copyToOtherFile(q, fftValues)
