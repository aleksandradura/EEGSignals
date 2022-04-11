import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AffinityPropagation, AgglomerativeClustering, MeanShift
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.cluster import adjusted_rand_score, homogeneity_score, adjusted_mutual_info_score, v_measure_score, completeness_score, silhouette_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# from DEAP import name_files as nf

def prepare_data(file_x, file_y):
    # targetPath = 'C:\\datasets\\DEAP\\data_preprocessed_python\\'

# valFile = targetPath + 'arousal.csv'

# file_x = 'C:\\datasets\\DEAP\\data_preprocessed_python\\out.dat'
# channelsFile = pd.read_csv(targetPath + 'allChannels.csv', sep=' ', low_memory=False)
    train = pd.read_csv(file_x, sep=' ', low_memory=False, header=None)
# channelsFile.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11']#, 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32']

    test = pd.read_csv(file_y, sep=' ', header=None)
# train = pd.read_csv("C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels.csv", header=None, sep=' ')
# train = pd.read_csv("C:\\datasets\\data_preprocessed_python\\asdf.csv", header=None, sep=' ')
# test = pd.read_csv("C:\\datasets\\data_preprocessed_python\\labels_252_1_01.dat", header=None, sep=' ')
# test = pd.read_csv(nf.label4class, header=None, sep=' ')

    return train, test



def data_standarization(train):
    # data, y = prepare_data(train, test)
    X = np.array(train.astype(float))
    # y = np.array(test)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

def kmeans(number_of_clusters, train, test):
    # data, y = prepare_data(train, test)

    data = pd.read_csv(train, sep=' ', low_memory=False, header=None)
    # channelsFile.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11']#, 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32']

    y = pd.read_csv(test, sep=' ', header=None)

    # p = pd.read_csv(path, sep=' ', header=None)
    # p_2 = pd.read_csv(path_2, sep=' ', header=None)
    kmeans = KMeans(n_clusters=number_of_clusters, max_iter=300)
    pred = kmeans.fit_predict(data)
    # kmeans.fit(data)
    # pred = kmeans.predict(data)
    label_predicted = []
    correct = 0

    # for i in range(len(data)):
    #     predict_me = np.array(data[i].astype(float))
        # print(len(predict_me))
        # predict_me = predict_me.reshape(-1, len(predict_me))
        # print(len(predict_me))
        # prediction = kmeans.predict(predict_me)
        # label_predicted.append(int(prediction))
        # if (prediction[0] == y[i]):
        #     correct += 1
        # print(int(prediction))
    # plt.scatter(data[:, 0], X[:,1], c=pred, s = 50, cmap='viridis')
    # print('Accuracy: '+ str(correct/len(test) * 100) + '%')
    label = np.squeeze(y)
    predicted = np.squeeze(pred)

    # plt.scatter(p, p_2, c=predicted,s=50,cmap='viridis')
    # plt.ylim(0, 10)
    # plt.xlim(0, 10)
    # plt.show()
    # print(predicted)
    # print(label.shape)
    # print(predicted.shape)
    # print('Rand score: %0.8f' % adjusted_rand_score(label, predicted))
    adjusted_rand = round(adjusted_rand_score(label, predicted), 8)
    acc = round(accuracy_score(label, predicted) * 100, 2)
    b = round(homogeneity_score(label, predicted), 8)
    c = round(completeness_score(label, predicted), 8)
    d = round(v_measure_score(label, predicted), 8)
    e = round(adjusted_mutual_info_score(label, predicted), 8)
    # print(adjusted_rand)
    return adjusted_rand, b,c,d,e, acc

def metrics(label, predicted):
    # print('Rand score: %0.8f' % adjusted_rand_score(label, predicted))
    # print('Homogeneity score: %0.8f' % homogeneity_score(label, predicted))
    # print("Completeness: %0.8f" % completeness_score(label, predicted))
    # print("V-measure: %0.8f" % v_measure_score(label, predicted))
    # print("Adjusted Mutual Information: %0.8f" % adjusted_mutual_info_score(label, predicted))
    # print("Silhouette Coefficient: %0.8f" % silhouette_score(X, label))
    # cm = confusion_matrix(predicted, label)
    # sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    # plt.show()
    adjusted_rand = str(round(adjusted_rand_score(label, predicted), 8))
    # print(adjusted_rand)
    # homogeneity = str(round(homogeneity_score(label, predicted), 8))
    # completeness = str(round(completeness_score(label, predicted), 8))
    # v_measure = str(round(v_measure_score(label, predicted), 8))
    # adjusted_mutual_info = str(round(adjusted_mutual_info_score(label, predicted), 8))
    return adjusted_rand

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


def dbscan():
    model = DBSCAN(eps=30)
    prediction = model.fit_predict(X)
    print(prediction)
    n_clusters_ = len(set(prediction)) - (1 if -1 in prediction else 0)
    n_noise_ = list(prediction).count(-1)
    print('Clusters: ' + str(n_clusters_))
    print('Noise: ' + str(n_noise_))


def agglomerativeClustering(number_of_clusters, data):
    model = AgglomerativeClustering(n_clusters=number_of_clusters)
    label_predicted = model.fit_predict(data)
    label = np.squeeze(y)
    predicted = np.squeeze(label_predicted)
    metrics(label, predicted)


def meanShift(data):
    model = MeanShift()
    label_predicted = model.fit_predict(data)
    label = np.squeeze(y)
    predicted = np.squeeze(label_predicted)
    metrics(label, predicted)

# wcss()
# def show_results(X, train, test):
def show_results(cluster_number, train, test):

    print('Normal data')
    print('Kmean')
    a = kmeans(cluster_number, train, test)
    # X = data_standarization(data)
    # print('Normalized data')
    # print('Kmean')
    # kmeans(cluster_number, X, test)
    return a
# print('Agglomerative clustering')
# agglomerativeClustering(cluster_number, X)
# print('Mean Shift')
# meanShift(X)

# print('Agglomerative clustering')
# agglomerativeClustering(cluster_number, data_standarization())
# print('Mean Shift')
# meanShift(data_standarization())
# print('Dbscan')
# dbscan()
