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
                     index_col=False, encoding='utf-8-sig')
# x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']
# x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96']
x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128']
# x = [ '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a','1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b', '31b', '32b', '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g', '9g', '10g', '11g', '12g', '13g', '14g', '15g', '16g', '17g', '18g', '19g', '20g', '21g', '22g', '23g', '24g', '25g', '26g', '27g', '28g', '29g', '30g', '31g', '32g']
# print(df)
# x = ['1', '2', '3', '4', '5', '6', '7', '8']
# df.boxplot(column= ['1t', '2t', '3t', '4t', '5t', '6t', '7t', '8t', '9t', '10t', '11t', '12t', '13t', '14t', '15t', '16t', '17t', '18t', '19t', '20t', '21t', '22t', '23t', '24t', '25t', '26t', '27t', '28t', '29t', '30t', '31t', '32t', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b', '31b', '32b'
# ], grid=False)
# plt.show()
allChannels = 128

# print(df.columns.tolist())


def takeFirstChannel():
    result, channelsChain = [], []
    summ, amount, channel = 0, 0, 1
    for i in range(allChannels):
        for j in range(allChannels):
            fvalue, pvalue = stats.f_oneway(abs(df[x[i]]), abs(df[x[j]]))
            # print(str(i) + str(j) + ' - ' + str(pvalue))
            # print(abs(df[x[i]]))
            if numpy.isnan(pvalue):
                pass
            else:
                summ += float(pvalue)
                amount += 1
        # print(str(i) + '  -  ' + str(summ) + ' : ' + str(amount))
        if summ != 0.0:
            result.append(summ/amount)
        else:
            result.append(1)
        summ, amount = 0, 0
    smallestValue = result[0]
    for k in range(len(result)):
        if float(result[k]) < float(smallestValue):
            smallestValue = result[k]
            channel = k + 1
    channelsChain.append(channel)
    return channelsChain

def takeSecondAndMoreChannels(N):
    channels = takeFirstChannel()
    chan, small, largets, summp, summf, amount = 0, 0, 0, 0, 0, 0
    summary, chList, fList = [], [], []
    for p in range(1, N):
        for j in range(allChannels):
            for i in range(len(channels)):
                fvalue, pvalue = stats.f_oneway(abs(df[x[channels[i] - 1]]), abs(df[x[j]]))
                summp += pvalue
                summf += fvalue
                amount += 1
                # print(abs(df[x[channels[i] - 1]]))
                # print(str(channels[i] - 1) + ' : ' + str(j) + ' - ' + str(pvalue) + ' - ' + str(amount))
            summary.append(summp/amount)
            # print(j, summp/amount)
            if summp == 0.0:
                fList.append(summf/amount)
                chList.append(j + 1)
                # print(str(j + 1) + '  -  ' + str((summf)/amount))
            else:
                chList.append(j + 1)
            summp, summf, amount = 0, 0, 0
        if len(fList) != 0:
            largest = fList[0]
            for i in range(1, len(fList)):
                if fList[i] > largest:
                    largest = fList[i]
                    chan = chList[i]
                    # print(chList[i], largest)
            channels.append(chan)
        else:
            small = 1
            for k in range(len(summary)):
                if small > summary[k] :
                    small = summary[k]
                    chan = chList[k]
                    # print(chan, small)
            channels.append(chan)
        summary.clear()
        fList.clear()
        chList.clear()
    return channels

#N - number of channels
N = 5
ch = takeSecondAndMoreChannels(N)
for i in range(len(ch)):
    print(ch[i])
# takeFirstChannel()

