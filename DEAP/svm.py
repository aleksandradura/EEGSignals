import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import time
targetPath = 'C:\\datasets\\data_preprocessed_python\\'

labelFile0 = targetPath + 'labels_252_0_01.dat'
labelFile1 = targetPath + 'labels_252_1_01.dat'
labelFile2 = targetPath + '2.csv'
labelFile3 = targetPath + '3.csv'
file_x = targetPath + 'arffFiles\\allChannels.csv'

np.random.seed(42)
def shuffle_data(x, y):
    idx = np.random.permutation(len(x))
    x_data= x[idx]
    y_labels=y[idx]
    return x_data, y_labels

def svm_classifier(file_y):
    mean = 0.0
    X = np.genfromtxt(file_x, delimiter=' ')
    y = np.genfromtxt(file_y, delimiter=' ')
    start = time.time()
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
    print(accuracy_score(y_test, y_predict) * 100)

    # cross-validation
    # clf = SVC(kernel='linear', C=1)
    # scores = cross_val_score(clf, X, y, cv=10)
    # print("Cross-validation:")
    # print("%2.2f (+/- %2.2f)" % (scores.mean() * 100, scores.std() * 100))
    end = time.time()
    elapsed = end - start
    print(elapsed)
print("--------------------VALENCE----------------------")
svm_classifier(labelFile0)
print("---------------------------AROUSAL-----------------------------")
svm_classifier(labelFile1)

# print("--------------------DOMINANCE----------------------")
# svm_classifier(labelFile2)
# print("-----------------LIKING-------------------")
# svm_classifier(labelFile3)



