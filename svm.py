import numpy
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

labelFile0 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_0_01.dat'
labelFile1 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_1_01.dat'
labelFile2 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_2_01.dat'
labelFile3 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_3_01.dat'

def svm_classifier(file_y):
    file_x = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'

    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    clf = SVC(kernel='rbf', random_state=42)
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print(accuracy_score(y_test, y_predict) * 100)


print("Accuracy score of valence ")
svm_classifier(labelFile0)
print("Accuracy score of arousal ")
svm_classifier(labelFile1)
print("Accuracy score of dominance ")
svm_classifier(labelFile2)
print("Accuracy score of liking ")
svm_classifier(labelFile3)


