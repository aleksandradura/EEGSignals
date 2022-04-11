from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from keras.models import Sequential, Model
from keras.layers import Dense, Input
from keras.layers import Convolution1D, ZeroPadding1D, MaxPooling1D, BatchNormalization, Activation, Dropout, Flatten, Dense, Conv1D
import keras
import time
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
# targetPath = 'C:\\datasets\\data_preprocessed_python\\'
# targetPath = 'C:\\datasets\\DEAP\\data_preprocessed_python\\'

# valFile = targetPath + 'arousal.csv'

# file_x = 'C:\\datasets\\DEAP\\data_preprocessed_python\\out.dat'
# channelsFile = pd.read_csv(targetPath + 'allChannels.csv', sep=' ', low_memory=False)
def cnn_prepare_data(file, label):
    channelsFile = pd.read_csv(file, sep=' ', low_memory=False, header=None)
    # channelsFile.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11']#, 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32']

    valFile = pd.read_csv(label, sep=' ', header=None)
    # arrFile = pd.read_csv(targetPath + 'labels_252_1_01.dat', sep=' ')
    # valFile.columns = ['label']
    # arrFile.columns = ['label']

    x_train, x_test, y_train, y_test = train_test_split(channelsFile, valFile, test_size=0.2, random_state=1)
    # x_train, x_test, y_train, y_test = train_test_split(channelsFile, arrFile, test_size=0.2, random_state=1)

    x_train = x_train.values.reshape(x_train.shape[0], x_train.shape[1], 1)
    y_train = y_train.values.reshape(y_train.shape[0], y_train.shape[1], 1)
    x_test = x_test.values.reshape(x_test.shape[0], x_test.shape[1], 1)
    y_test = y_test.values.reshape(y_test.shape[0], y_test.shape[1], 1)
    t = MinMaxScaler()
    return x_train, y_train, x_test, y_test
# channelsFile = np.asarray(channelsFile).astype(np.float32)

# def Autoencoder():
#     t.fit(x_train)
#     X_train = t.transform(x_train)
#     X_test = t.transform(x_test)
#     t.fit(channelsFile)
#     channelsFile1 = t.transform(channelsFile)
#     valFile1 = t.transform(valFile)
#     # print(channelsFile.shape)
#
#     # model = LogisticRegression()
#     # model.fit(X_train, y_train)
#     # yhat = model.predict(X_test)
#     # acc = accuracy_score(y_test, yhat)
#     # print(acc)
#
#     encoder = keras.models.load_model('encoder.h5')
#
#     # encode the train data
#     X_train_encode = encoder.predict(X_train)
#     # encode the test data
#     X_test_encode = encoder.predict(X_test)

def CNN(file, label):
    # X = np.genfromtxt(file, delimiter=' ')
    # y = np.genfromtxt(label, delimiter=' ')
    channelsFile = pd.read_csv(file, sep=' ', low_memory=False, header=None)
    # channelsFile.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11']#, 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32']

    valFile = pd.read_csv(label, sep=' ', header=None)
    # arrFile = pd.read_csv(targetPath + 'labels_252_1_01.dat', sep=' ')
    # valFile.columns = ['label']
    # arrFile.columns = ['label']

    x_train, x_test, y_train, y_test = train_test_split(channelsFile, valFile, test_size=0.2, random_state=1)

    x_train = x_train.values.reshape(x_train.shape[0], x_train.shape[1], 1)
    y_train = y_train.values.reshape(y_train.shape[0], y_train.shape[1], 1)
    x_test = x_test.values.reshape(x_test.shape[0], x_test.shape[1], 1)
    y_test = y_test.values.reshape(y_test.shape[0], y_test.shape[1], 1)
    num_classes = 10
    input_shape = (x_train.shape[1], 1)
    # input_shape = (x_train.shape[1])
    model = Sequential()
    model.add(Conv1D(128, kernel_size=10,padding = 'same',activation='relu', input_shape= input_shape))
    # model.add(BatchNormalization())
    # model.add(MaxPooling1D(pool_size=(2)))
    model.add(MaxPooling1D(pool_size=(2)))
    model.add(Conv1D(128,kernel_size=10,padding = 'same', activation='relu'))
    # model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=(2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(16, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(16, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(num_classes, activation='softmax'))
    # model.summary()
    start = time.time()
    model.compile(loss='sparse_categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
    history = model.fit(x_train, y_train, epochs=200, batch_size=100)
    # tf.device('/cpu:0')
    loss, acc = model.evaluate(x_test, y_test, verbose=1)
    # print('test acc:', test_acc)
    # print('test loss:', test_loss)

    # end = time.time()
    # elapsed = end - start
    # print(elapsed / 60.00)
    # plt.plot(history.history['accuracy'], label='accuracy')
    # plt.plot(history.history['val_accuracy'], label='val_accuracy')
    # plt.xlabel('Epoch')
    # plt.ylabel('Accuracy')
    # # plt.ylim([0.5, 1])
    # # plt.legend(loc='lower right')
    # plt.legend(['test'], loc='upper left')
    # plt.show()

    # # plt.plot(history.history['loss'])
    # plt.plot(history.history['val_loss'])
    # plt.title('model loss')
    # plt.ylabel('loss')
    # plt.xlabel('epoch')
    # plt.legend(['test'], loc='upper left')
    # plt.show()
    return loss, acc
def DNN(input, hidden, output):
    model = Sequential()
    model.add(Dense(input,  activation='relu')) #Flatten try
    model.add(Dense(hidden, activation='relu')) #hidden
    model.add(Dense(output, activation='sigmoid')) #output try softmax

    model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy']) #sparse_categorical_crossentropy
    model.fit(x_train, y_train, epochs=50, batch_size=11)

    results = model.evaluate(x_test, y_test, verbose=1)
    # print('test acc:', test_acc)
    return results
    # plt.plot(history.history['accuracy'], label='accuracy')
    # plt.plot(history.history['val_accuracy'], label='val_accuracy')
    # plt.xlabel('Epoch')
    # plt.ylabel('Accuracy')
    # plt.ylim([0.5, 1])
    # plt.legend(loc='lower right')
# DNN(11, 5, 1)
destination_path = 'C:\\datasets\\DEAP\\data_preprocessed_python\\out.dat'
arousal_path = 'C:\\datasets\\DEAP\\data_preprocessed_python\\arousal.csv'
CNN(destination_path, arousal_path)
# if tf.test.gpu_device_name():
#     print('Default GPU Device:{}'.format(tf.test.gpu_device_name()))
# else:
#     print("Please install GPU version of TF")