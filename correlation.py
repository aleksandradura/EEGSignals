from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# plt.figure(figsize=(40,40))
# top_corr_features = cor.index
# sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
# fig, ax = plt.subplots(figsize=(10,6))
# plt.show()


df = pd.read_csv('C:\\Users\\aleks\\OneDrive\\Pulpit\data_preprocessed_python\\asdf.csv', sep=' ', index_col=False)
corr = df.corr()
channels = 96
def takeAverageList():
    result = []
    for i in range(channels):
        result.append(corr.values[np.triu_indices_from(corr.values, i)].mean())
        # print(str(i + 1) + ' ' + str(corr.values[np.triu_indices_from(corr.values, i)].mean()))
    return result

def takeFirstChannelWithTheSmallestCorr():
    channel = 0
    result = takeAverageList()
    smallestValue = abs(result[0])
    for j in range(len(result)):
        if abs(result[j]) < abs(smallestValue):
            smallestValue = result[j]
            channel = j + 1
    return channel

def selectNextChannels(N):
    ch = takeFirstChannelWithTheSmallestCorr()
    minList, channelList, temp, channelAmount, minValue, cha = [], [], 1, 1, 0, 0
    #write on the list first element
    channelList.insert(0, ch)
    for k in range(N):
        for i in range(channels):
            #choose second channel
            if channelAmount == 1:
                minList.append(abs(df.corr().iloc[ch - 1, i]))
            else:
                #choose third channel
                for t in range(k):
                    minValue += abs(df.corr().iloc[channelList[t] - 1, i])
                minList.append(float(minValue) / float(channelAmount))
                minValue = 0
                # print(str(channelList[t] - 1) + ' ' + str(i) + ' ' + str(min[i]))
        for j in range(channels):
            if abs(minList[j]) < temp:
                temp = abs(minList[j])
                cha = j + 1
                # print(str(min[j]) + ' ' + str(cha))
        #clear list for another channel
        minList.clear()
        channelList.append(cha)
        minValue, temp = 0, 1
        channelAmount += 1
    return channelList

n = 5
channels = []
channels = selectNextChannels(n)
for z in range(n):
    print(channels[z])



