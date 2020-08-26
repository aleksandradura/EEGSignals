from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import scipy.stats as stats
import numpy
# stats f_oneway functions takes the groups as input and returns F and P-value

# plt.figure(figsize=(40,40))
# top_corr_features = cor.index
# sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
# fig, ax = plt.subplots(figsize=(10,6))
# plt.show()


df = pd.read_csv('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv', sep=' ')
                 # columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'],
                 #     index_col=False)
# x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']
x = ['1t', '2t', '3t', '4t', '5t', '6t', '7t', '8t', '9t', '10t', '11t', '12t', '13t', '14t', '15t', '16t', '17t', '18t', '19t', '20t', '21t', '22t', '23t', '24t', '25t', '26t', '27t', '28t', '29t', '30t', '31t', '32t', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b', '31b', '32b'
]
# print(df)
# df.boxplot(column= ['1t', '2t', '3t', '4t', '5t', '6t', '7t', '8t', '9t', '10t', '11t', '12t', '13t', '14t', '15t', '16t', '17t', '18t', '19t', '20t', '21t', '22t', '23t', '24t', '25t', '26t', '27t', '28t', '29t', '30t', '31t', '32t', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b', '31b', '32b'
# ], grid=False)
# plt.show()
allChannels = 96

# fvalue, pvalue = stats.f_oneway(df[x[0]], df[x[1]])
def takeFirstChannel():
    result = []
    summ, channel, ammount = 0, 1, 0
    for i in range(allChannels):
        for j in range(1, allChannels):
            fvalue, pvalue = stats.f_oneway(abs(df[x[i]]), abs(df[x[j]]))
            if numpy.isnan(pvalue):
                pass
            else:
                summ += pvalue
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
# print(takeFirstChannel())
def takeSecondChannel():

    smallest, secCh = 0.0, 0
    ch = takeFirstChannel()
    if ch - 1 != 0:
        fvalue, pvalue = stats.f_oneway(df[x[ch - 1]], df[x[0]])
        secCh = 1
    else:
        fvalue, pvalue = stats.f_oneway(df[x[ch - 1]], df[x[1]])
        secCh = 2
    if numpy.isnan(pvalue):
        # print("Null")
        pass
    else:
        smallest = float(pvalue)
    # print(smallest)
    for j in range(allChannels):
        if ch - 1 != j:
            fvalue, pvalue = stats.f_oneway(df[x[ch-1]], df[x[j]])
            # print(str(j) + '  -  ' + str(pvalue))
            if numpy.isnan(pvalue):
                pass
            else:
                if pvalue < smallest:
                    smallest = pvalue
                    secCh = j + 1
    # print(smallest)
    # print(secCh)
    return secCh
# print(takeSecondChannel())
ch = takeFirstChannel()
secCh = takeSecondChannel()
result = []
summary = []
summ, channel = 0, 1
thirdCh = 0
for j in range(allChannels):
    if j != ch - 1 and j != secCh - 1:
        fstat1 = stats.f_oneway(df[x[ch - 1]], df[x[j]])
        fstat2 = stats.f_oneway(df[x[secCh - 1]], df[x[j]])
        summ = fstat1.pvalue + fstat2.pvalue
        # print(summ/2)
        summary.append(summ/2)
    elif j == ch - 1:
        summary.insert(j, 1)
    elif j == secCh - 1:
        summary.insert(j, 1)
    summ = 0
    # if pvalue < result[i]:
    #     result.append(pvalue)
    #     channel = i + 1
    # print(fvalue, pvalue)
res = summary[0]
for i in range(len(summary)):
    if summary[i] < res:
        res = summary[i]
        thirdCh = i + 1



print(ch)
print(secCh)
# print(res)
print(thirdCh)
s = []
for j in range(allChannels):
    if j != ch - 1 and j != secCh - 1 and j != thirdCh:
        fstat1 = stats.f_oneway(df[x[ch - 1]], df[x[j]])
        fstat2 = stats.f_oneway(df[x[secCh - 1]], df[x[j]])
        fstat3 = stats.f_oneway(df[x[thirdCh - 1]], df[x[j]])
        summ = fstat1.pvalue + fstat2.pvalue + fstat3.pvalue
        # print(summ/2)
        s.append(summ/3)
    elif j == ch - 1:
        s.insert(j, 1)
    elif j == secCh - 1:
        s.insert(j, 1)
    elif j == thirdCh - 1:
        s.insert(j, 1)
    summ = 0
    # if pvalue < result[i]:
    #     result.append(pvalue)
    #     channel = i + 1
    # print(fvalue, pvalue)
res = s[0]
for i in range(len(s)):
    if s[i] < res:
        res = s[i]
        fourthCh = i + 1
print(fourthCh)
# for i in range(3):
#     for j in range(1, 3):
#         fvalue, pvalue = stats.f_oneway(df[x[i]], df[x[j]])
#         print(str(j) + '-' +str(i) + '  -   ' + str(pvalue))

# print(channel)

# fvalue, pvalue = stats.f_oneway(df['2'], df['3'])
# print(fvalue, pvalue)
# fvalue, pvalue = stats.f_oneway(df['1'], df['3'])
# print(fvalue, pvalue)