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

# relevant_features = cor_target[cor_target>0.5]
# print(relevant_features)
# print(df[["1","2"]].corr())
# print(df['1'].corr(df['2']))


# df = pd.read_csv('C:\\Users\\aleks\\OneDrive\\Pulpit\data_preprocessed_python\\arffFiles\\allChannels.csv', sep=' ', index_col=False)
# corr = df.corr()
df = pd.read_csv('C:\\Users\\aleks\\OneDrive\\Pulpit\data_preprocessed_python\\arffFiles\\allChannels.csv', sep=' ',
                 # columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'],
                     index_col=False)
corr = df.corr()

def takeAverageList():
    result = []
    for i in range(32):
        result.append(corr.values[np.triu_indices_from(corr.values, i)].mean())
        print(str(i + 1) + ' ' + str(corr.values[np.triu_indices_from(corr.values, i)].mean()))
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

print(takeFirstChannelWithTheSmallestCorr())
def selectMinValue(N):
    ch = takeFirstChannelWithTheSmallestCorr()
    min, spr, m, z, t,cha = [], [], 1, 0, 0, 0
    channelAmount = 1
    channelList = []
    channelList.insert(0, ch)
    # for h in range(32):
    #     min.insert(h, 0)
    # min.insert(0,0)
    for k in range(N):
        for i in range(32):
            if channelAmount == 1:
                min.append(abs(df.corr().iloc[ch - 1, i]))
            else:
                for t in range(k):
                    # print(channelList[m])
                    z += abs(df.corr().iloc[channelList[t] - 1, i])

                min.append(float(z) / float(channelAmount))
                z = 0
                print(str(channelList[t] - 1) + ' ' + str(i) + ' ' + str(min[i]))
        for j in range(32):
            if abs(min[j]) < m:
                m = abs(min[j])
                cha = j + 1
                print(str(min[j]) + ' ' + str(cha))
        # for o in range(32):
        #     min.pop(o)
        min.clear()
            # print(min[o])
        channelList.append(cha)
        # print(cha)
        z, m = 0, 1
        channelAmount += 1

    return channelList
# selectMinValue(3)
# kanaly = []
# kanaly = selectMinValue(5)
# for z in range(5):
#     print(kanaly[z])
# cor = df.corr()
# cor_target = abs(cor['17']).min()
# print(cor_target)

# print(abs(cor['17']))
# print(abs(cor['24']))

# second_value = 24
# # print(abs(df.corr().iloc[16,0]))
# # print(abs(df.corr().iloc[16]))
# firstChannel = takeFirstChannelWithTheSmallestCorr()
# s = []
# for k in range(32):
#     z = (abs(df.corr().iloc[firstChannel, k]) + abs(df.corr().iloc[23,k]))/2
#     s.append(z)
# mi = s[0]
# for f in range(1, 32):
#     if s[f] < mi:
#         mi = s[f]
#         bu = f + 1
#     # thirdValue is 8
# print(bu)

# q = []
# for k in range(32):

#     z = (abs(df.corr().iloc[16, k]) + abs(df.corr().iloc[23,k]) + abs(df.corr().iloc[8,k]))/3
#     q.append(z)
# mi = q[0]
# for f in range(1, 32):
#     if q[f] < mi:
#         mi = q[f]
#         bu = f + 1
#     # thirdValue is 16
# print(bu)



