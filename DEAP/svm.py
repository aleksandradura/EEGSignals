import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import time
import pandas as pd

# targetPath = 'C:\\datasets\\DEAP\\data_preprocessed_python\\'

# labelFile0 = targetPath + 'arousal.csv'
# labelFile1 = targetPath + 'labels_252_1_01.dat'
# labelFile2 = targetPath + '2.csv'
# labelFile3 = targetPath + '3.csv'
# file_x = 'C:\\datasets\\DEAP\\data_preprocessed_python\\out.dat'

np.random.seed(42)
def shuffle_data(x, y):
    idx = np.random.permutation(len(x))
    x_data= x[idx]
    y_labels=y[idx]
    return x_data, y_labels

def svm_classifier(file_y, file):
    mean = 0.0
    X = pd.read_csv(file, sep=' ', low_memory=False, header=None)

    y = pd.read_csv(file_y, sep=' ', header=None)
    # X = np.genfromtxt(file, delimiter=' ')
    # y = np.genfromtxt(file_y, delimiter=' ')
    # start = time.time()
    # for i in range(10):
    #     d, l = shuffle_data(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    clf = SVC(kernel='rbf', random_state=42)
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
        # mean += (accuracy_score(y_test, y_predict) * 100)
    # print("Average:")
    # print(mean/10.0)
    # print(accuracy_score(y_test, y_predict) * 100)

    # cross-validation
    # clf = SVC(kernel='linear', C=1)
    # scores = cross_val_score(clf, X, y, cv=10)
    # print("Cross-validation:")
    # print("%2.2f (+/- %2.2f)" % (scores.mean() * 100, scores.std() * 100))
    # end = time.time()
    # elapsed = end - start
    # print(elapsed)
    return str(round(accuracy_score(y_test, y_predict) * 100, 2))
# print("--------------------VALENCE----------------------")
# svm_classifier(labelFile0, file_x)
# print("---------------------------AROUSAL-----------------------------")
# svm_classifier(labelFile1)

# print("--------------------DOMINANCE----------------------")
# svm_classifier(labelFile2)
# print("-----------------LIKING-------------------")
# svm_classifier(labelFile3)



