import numpy
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
def svm_classifier():
    file_x = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'
    file_y = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\0.csv'

    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    clf = SVC(kernel='rbf', random_state=42)
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("Accuracy score of arousal ")
    print(accuracy_score(y_test, y_predict) * 100)

if __name__ == '__main__':
    svm_classifier()
#     file_x = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\features_sampled.dat'
#     file_y = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_1.dat'
#
#     X = numpy.genfromtxt(file_x, delimiter=' ')
#     y = numpy.genfromtxt(file_y, delimiter=' ')
#
#     # Split the data into training/testing sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
#
#     # Feature Scaling
#     from sklearn.preprocessing import StandardScaler
#     sc = StandardScaler()
#     X_train = sc.fit_transform(X_train)
#     X_test = sc.transform(X_test)
# #
#     # SVM Classifier
#     clf = SVC(kernel='rbf', random_state=42)
#     clf.fit(X_train, y_train)
#     y_predict = clf.predict(X_test)
#     cm = confusion_matrix(y_test, y_predict)
#     print(cm)
#     print("Accuracy score of Arousal ")
#     print(accuracy_score(y_test, y_predict) * 100)
#     file_x = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\features_sampled.dat'
#     file_y = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_2.dat'
#
#     X = numpy.genfromtxt(file_x, delimiter=' ')
#     y = numpy.genfromtxt(file_y, delimiter=' ')
#
#     # Split the data into training/testing sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
#
#     # Feature Scaling
#     from sklearn.preprocessing import StandardScaler
#     sc = StandardScaler()
#     X_train = sc.fit_transform(X_train)
#     X_test = sc.transform(X_test)
#
#     # SVM Classifier
#     clf = SVC(kernel='rbf', random_state=42)
#     clf.fit(X_train, y_train)
#     y_predict = clf.predict(X_test)
#     cm = confusion_matrix(y_test, y_predict)
#     print(cm)
#     print("Accuracy score of Dominance ")
#     print(accuracy_score(y_test, y_predict) * 100)
#     ######################################################################3
#
#     file_x = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\features_sampled.dat'
#     file_y = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_3.dat'
#
#     X = numpy.genfromtxt(file_x, delimiter=' ')
#     y = numpy.genfromtxt(file_y, delimiter=' ')
#
#     # Split the data into training/testing sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
#
#     # Feature Scaling
#     from sklearn.preprocessing import StandardScaler
#     sc = StandardScaler()
#     X_train = sc.fit_transform(X_train)
#     X_test = sc.transform(X_test)
#
#     # SVM Classifier
#     clf = SVC(kernel='rbf', random_state=42)
#     clf.fit(X_train, y_train)
#     y_predict = clf.predict(X_test)
#     cm = confusion_matrix(y_test, y_predict)
#     print(cm)
#     print("Accuracy score of liking  ")
#     print(accuracy_score(y_test, y_predict) * 100)


