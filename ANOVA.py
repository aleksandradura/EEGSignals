import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import scipy.stats as stats
import numpy

# plt.figure(figsize=(40,40))
# top_corr_features = cor.index
# sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
# fig, ax = plt.subplots(figsize=(10,6))
# plt.show()


df = pd.read_csv('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv', sep=' ',
                 # columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'],
                     index_col=False)
# x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']
x = ['1t', '2t', '3t', '4t', '5t', '6t', '7t', '8t', '9t', '10t', '11t', '12t', '13t', '14t', '15t', '16t', '17t', '18t', '19t', '20t', '21t', '22t', '23t', '24t', '25t', '26t', '27t', '28t', '29t', '30t', '31t', '32t', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b', '31b', '32b', '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g', '9g', '10g', '11g', '12g', '13g', '14g', '15g', '16g', '17g', '18g', '19g', '20g', '21g', '22g', '23g', '24g', '25g', '26g', '27g', '28g', '29g', '30g', '31g', '32g']
# print(df)
# df.boxplot(column= ['1t', '2t', '3t', '4t', '5t', '6t', '7t', '8t', '9t', '10t', '11t', '12t', '13t', '14t', '15t', '16t', '17t', '18t', '19t', '20t', '21t', '22t', '23t', '24t', '25t', '26t', '27t', '28t', '29t', '30t', '31t', '32t', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b', '31b', '32b'
# ], grid=False)
# plt.show()
allChannels = 128

# fvalue, pvalue = stats.f_oneway(df[x[0]], df[x[1]])
def takeFirstChannel():
    result = []
    summ, channel, ammount = 0, 1, 0
    for i in range(allChannels):
        for j in range(0, allChannels):
            fvalue, pvalue = stats.f_oneway(abs(df[x[i]]), abs(df[x[j]]))
            if numpy.isnan(pvalue):
                pass
            else:
                summ += float(pvalue)
                ammount += 1
                # print(str(i) + '  -  ' + str(j) + '  -  ' + str(pvalue))
        result.append(summ/(ammount))
        summ = 0
    smallestValue = result[0]

    for k in range(len(result)):
        if float(result[k]) < float(smallestValue):
            smallestValue = result[k]
            channel = k + 1
        # print(str(k) + '  -  ' + str(result[k]))
    # print(channel)
    return channel
print(takeFirstChannel())
def takeSecondChannel():
    fList, chList = [], []
    smallest, secCh, small, chan = 0.0, 0, 0, 0
    ch = takeFirstChannel()
    if ch - 1 != 0:
        fvalue, pvalue = stats.f_oneway(abs(df[x[ch - 1]]), abs(df[x[0]]))
        secCh = 1
        if pvalue == 0.0:
            fList.append(fvalue)
            chList.insert(0, 0)
            # print(fvalue)
    else:
        fvalue, pvalue = stats.f_oneway(abs(df[x[ch - 1]]), abs(df[x[1]]))
        secCh = 2
        if pvalue == 0.0:
            fList.append(fvalue)
            chList.insert(0, 1)
            # print(fvalue)
    if numpy.isnan(pvalue):
        # print("Null")
        pass
    else:
        smallest = float(pvalue)
    # print(smallest)
    for j in range(allChannels):
        if ch - 1 != j:
            fvalue, pvalue = stats.f_oneway(abs(df[x[ch-1]]), abs(df[x[j]]))
            # print(str(j) + '  -  ' + str(pvalue))
            if numpy.isnan(pvalue):
                pass
            else:
                if pvalue < smallest:
                    smallest = pvalue
                    secCh = j + 1
                if pvalue == 0.0:
                    fList.append(fvalue)
                    # print(str(j+1) + '  -  ' + str(fvalue))
                    chList.append(j)
    if len(fList) != 0:
        small = fList[0]
        for i in range(1, len(fList)):
            if fList[i] > small:
                small = fList[i]
                # print(small)
                chan = chList[i] + 1
        return chan
    else:
        return secCh
print(takeSecondChannel())
def thirdChanel():
    ch = takeFirstChannel()
    chan, small = 0, 0
    secCh = takeSecondChannel()
    result = []
    summary, chList, fList = [], [], []
    summ, channel = 0, 1
    thirdCh = 0
    for j in range(allChannels):
        if j != ch - 1 and j != secCh - 1:
            fvalue, pvalue = stats.f_oneway(abs(df[x[ch - 1]]), abs(df[x[j]]))
            fvalue2, pvalue2 = stats.f_oneway(abs(df[x[secCh - 1]]), abs(df[x[j]]))
            summ = pvalue + pvalue2
            summary.append(summ/2)
            if (summ/2) == 0.0:
                fList.append((fvalue + fvalue2)/2)
                chList.append(j + 1)
                # print(str(j + 1) + '  -  ' + str((fvalue + fvalue2)/2))
        elif j == ch - 1:
            summary.insert(j, 1)
        elif j == secCh - 1:
            summary.insert(j, 1)
        summ = 0
    if len(fList) != 0:
        small = fList[0]
        for i in range(1, len(fList)):
            if fList[i] > small:
                small = fList[i]
                chan = chList[i]
        return chan
    else:
        return "Nie ma"


# print(ch)
# print(secCh)
# print(res)
print(thirdChanel())
# print(thirdCh)

def fourthChanel():
    ch = takeFirstChannel()
    chan, small = 0, 0
    secCh = takeSecondChannel()
    th = thirdChanel()
    su = []
    fList, chList = [], []
    s = 0
    for m in range(allChannels):
        # print(m)
        if m != ch - 1 and m != secCh - 1 and m != th - 1:
            fvalue, pvalue = stats.f_oneway(abs(df[x[ch - 1]]), abs(df[x[m]]))
            fvalue2, pvalue2 = stats.f_oneway(abs(df[x[secCh - 1]]), abs(df[x[m]]))
            fvalue3, pvalue3 = stats.f_oneway(abs(df[x[th - 1]]), abs(df[x[m]]))

            s = pvalue + pvalue2 + pvalue3
            # print(str(m) + '  -  ' + str(pvalue) +  '  -  ' + str(pvalue2) +  '  -  ' + str(pvalue3))
            # print(s/3)
            su.append(s/3)
            if (s/3) == 0.0:
                fList.append((fvalue + fvalue2 + fvalue3)/3)
                chList.append(m + 1)
                # print(str(m + 1) + '  -  ' + str((fvalue + fvalue2 + fvalue3)/3))
        elif m == ch - 1:
            su.insert(m, 1)
        elif m == secCh - 1:
            su.insert(m, 1)
        elif m == th - 1:
            su.insert(m, 1)
        summ = 0
    if len(fList) != 0:
        small = fList[0]
        for i in range(1, len(fList)):
            if fList[i] > small:
                small = fList[i]
                chan = chList[i]
        return chan
    else:
        return "Nie ma"
        # print(m)

        # print(su[m])
    # if len(fList) != 0:
    #     small = fList[0]
    #     for i in range(1, len(fList)):
    #         if fList[i] > small:
    #             small = fList[i]
    #             chan = chList[i]
    #     return chan
    # else:
        # if pvalue < result[i]:
        #     result.append(pvalue)
        #     channel = i + 1
        # print(fvalue, pvalue)
print(fourthChanel())
# su = []
# su = fourthChanel()
#
# f = 0
# res = su[0]
# for i in range(len(su)):
#     if su[i] < res:
#         res = su[i]
#         f = i + 1
# print(f)

    # if pvalue < result[i]:
    #     result.append(pvalue)
    #     channel = i + 1
    # print(fvalue, pvalue)
# res = s[0]
# for i in range(len(s)):
#     if s[i] < res:
#         res = s[i]
#         fourthCh = i + 1
# print(fourthCh)
# for i in range(3):
#     for j in range(1, 3):
#         fvalue, pvalue = stats.f_oneway(df[x[i]], df[x[j]])
#         print(str(j) + '-' +str(i) + '  -   ' + str(pvalue))

# print(channel)

# fvalue, pvalue = stats.f_oneway(df['2'], df['3'])
# print(fvalue, pvalue)
# fvalue, pvalue = stats.f_oneway(df['1'], df['3'])
# print(fvalue, pvalue)
# from sympy.mpmath import *
# import mpmath as mpf

# for i in range(127):
#
#
#     fvalue, pvalue = stats.f_oneway(abs(df[x[68]]), abs(df[x[i]]))
#     if pvalue == 0.0:
#         print(str(pvalue) + '  -  ' + str(fvalue))