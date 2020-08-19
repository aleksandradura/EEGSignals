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
                     index_col=False)
corr = df.corr()

def takeAverageList():
    result = []
    for i in range(32):
        result.append(corr.values[np.triu_indices_from(corr.values, i)].mean())
        # print(str(i + 1) + ' ' + str(m))
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
def selectMinValue():
    ch = takeFirstChannelWithTheSmallestCorr()
    min, m = [], 1
    for i in range(32):
        min.append(df.corr().iloc[ch - 1, i])

    for j in range(32):
        if abs(min[j]) < m:
            m = abs(min[j])
            ch = j + 1
            # print(m)
    return ch
print(selectMinValue())
# cor = df.corr()
# cor_target = abs(cor['17']).min()
# print(cor_target)

# print(abs(cor['17']))
# print(abs(cor['24']))

# second_value = 24
# # print(abs(df.corr().iloc[16,0]))
# # print(abs(df.corr().iloc[16]))

s = []
for k in range(32):
    z = (abs(df.corr().iloc[16, k]) + abs(df.corr().iloc[23,k]))/2
    s.append(z)
mi = s[0]
for f in range(1, 32):
    if s[f] < mi:
        mi = s[f]
        bu = f + 1
    # thirdValue is 8
print(bu)

q = []
for k in range(32):
    z = (abs(df.corr().iloc[16, k]) + abs(df.corr().iloc[23,k]) + abs(df.corr().iloc[23,k]))/3
    q.append(z)
mi = q[0]
for f in range(1, 32):
    if q[f] < mi:
        mi = q[f]
        bu = f + 1
    # thirdValue is 8
print(bu)



