import numpy
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle

allrow = 121968
channelMin = 14
channelMax = 29
allChannelsFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv'
channelsWithLabel = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\FS\\32channelsWith01.csv"
selectedLabelFiles = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\FS\\01.csv"
channelsFile = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\FS\\akuku2.csv"
#0 valence, 1 arousal, 2 dominance, 3 liking
allLabels = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_0_01.dat"
correlationFiles = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\FS\\correlation.csv"


#ilość wierszy dla każdego uczestnika: 10080
#dla 22 uczestników
def sampleFeatures():
    data = open(allChannelsFile,'w')

    for i in range(22):
        if(i%1 == 0):
            if i < 10:
                name = '%0*d' % (2,i+1)
            else:
                name = i+1
            # pobieranie plików binarnych każdego uczestnika z folderu s
            fname = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\s\\s"+str(name)+".dat"
            x = pickle.load(open(fname, 'rb'), encoding='latin1')
            for tr in range(22): #ilość prób
                if(tr%1 == 0):
                    for dat in range(8064): #czas
                        if(dat%32 == 0 ):
                            for ch in range(32): #ilość kanałów
                                    # fout_data.write(str(ch+1) + " ");
                                    data.write(str(x['data'][tr][ch][dat]) + " ")
                                    if (ch+1 == 32):
                                        data.write("\n")
                data.write("\n")
    data.close()
#sampleFeatures()

# merge label file with file where are 32 channels - arrfiles format for correlation
def mergeLabesWithChannels():
    with open(allLabels) as yh:
      with open(allChannelsFile) as xh:
          with open(correlationFiles, "w") as zh:

            xlines = xh.readlines()
            ylines = yh.readlines()
            for i in range(allrow):
                line = ylines[i].strip() + ' ' + xlines[i]
                zh.write(line)
# mergeLabesWithChannels()

def writeToTable():
    with open(channelsWithLabel, "r") as file:
        result = []
        for line in file:
            result.append(line.split(' '))
        return result

maxLength = len(writeToTable())
result = writeToTable()

def remove01emptylines():
    with open(selectedLabelFiles, "r") as file01:
        lines = file01.readlines()
        with open(selectedLabelFiles, "w") as file01:
            for line in lines:
                if line.strip() != "":
                    file01.write(line)

def removechannelsemptylines():
    with open(channelsFile, "r") as file:
        lines = file.readlines()
        with open(channelsFile, "w") as file:
            for line in lines:
                if line.strip() != "":
                    file.write(line)

def svm_classifier():
    file_x = channelsFile
    file_y = selectedLabelFiles

    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    clf = SVC(kernel='rbf', random_state=42)
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_predict) * 100
    return accuracy


def numberOfRows(ch1, ch2, ch3):
    count = len(open(channelsFile).readlines())
    if count > 200:
        acc = svm_classifier()
        if acc > 85:
            print(str(ch3) + " " + str(ch2) + " " + str(ch1) + " " + str(acc))


def selectValueFunc(r, r2, r3):
    with open(channelsFile, "w") as file1:
        with open(selectedLabelFiles, "w") as file01:
            for j in range(r, r+1):
                for i in range(0, maxLength):
                    if ((float(result[i][j]) > float(channelMin) and float(result[i][j]) < float(channelMax)) and (float(result[i][r2]) > float(channelMin) and float(result[i][r2]) < float(channelMax)) and (float(result[i][r3]) > float(channelMin) and float(result[i][r3]) < float(channelMax))):
                            # print(result[i][0])
                        file01.write(result[i][0])
                        file1.write(result[i][1] + ' ' + result[i][2] + ' ' + result[i][3])
                    file1. write('\n')
                    file01.write('\n')


def takeAccAllChannels():
    z1, z2, z3 = 1, 2, 3
    for i3 in range(z1, 31):
        for i2 in range(z2, 32):
            if i2 > i3:
                for i in range(z3, 33):
                    if i > i2:
                        selectValueFunc(i, i2, i3)
                        removechannelsemptylines()
                        remove01emptylines()
                        numberOfRows(i, i2, i3)

# takeAccAllChannels()
