import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels.csv", header=None, sep = ' ')
test = pd.read_csv("C:\\datasets\\data_preprocessed_python\\labels_252_0_01.dat", header=None, sep=' ')
X = np.array(train.astype(float))
# test.info()
y=np.array(test)
# print(type(test))
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
def kmeans():
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X_scaled)

    correct = 0
    for i in range(len(X)):
        predict_me = np.array(X[i].astype(float))
        predict_me = predict_me.reshape(-1, len(predict_me))
        prediction = kmeans.predict(predict_me)

        if (prediction[0] == y[i]):
            correct += 1

    print(correct/len(test))

kmeans()
def wcss():
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
