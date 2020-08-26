forOneValue, total, allrow = 252, 0, 10112
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 22, 32, 8064
allChannelsFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv'
selectedChannels = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'
rowNumberFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\rownumber.csv'
selectedLabel0 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\0.csv'
selectedLabel1 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\1.csv'
selectedLabel2 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\2.csv'
selectedLabel3 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\3.csv'
label0 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_0_01.dat'
label1 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_1_01.dat'
label2 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_2_01.dat'
label3 = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_3_01.dat'

#for one user: 10080 row
import pickle
def sampleFeatures():
    data = open(allChannelsFile,'w')
    for i in range(nUser):
        if(i%1 == 0):
            if i < 10:
                name = '%0*d' % (2,i+1)
            else:
                name = i+1
            # pobieranie plików binarnych każdego uczestnika z folderu s
            fname = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\s\\s"+str(name)+".dat"
            x = pickle.load(open(fname, 'rb'), encoding='latin1')
            for tr in range(nTrial): #ilość prób
                if(tr%1 == 0):
                    for dat in range(nTime): #czas
                        if(dat%32 == 0 ):
                            for ch in range(nChannel): #ilość kanałów
                                    # fout_data.write(str(ch+1) + " ");
                                    data.write(str(x['data'][tr][ch][dat]) + " ")
                                    if (ch+1 == nChannel):
                                        data.write("\n")
                data.write("\n")
    data.close()

def removechannelsemptylines():
    with open(allChannelsFile, "r") as file:
        lines = file.readlines()
        with open(allChannelsFile, "w") as file:
            for line in lines:
                if line.strip() != "":
                    file.write(line)

#take length for num
def maxLenFunc():
    with open(allChannelsFile, 'r') as fileValue:
        maxLen = len(fileValue.readlines())
        return maxLen

def takeOneOrZeroValueFunc(label):
    with open(label, 'r') as fileValue:
        oneOrZero = []
        for line in fileValue:
            oneOrZero.append(line.rstrip('\n'))
        return oneOrZero

def readRowNumberFunc():
    with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\rownumber.csv') as rowNumberFile:
        result = []
        for line in rowNumberFile:
            result.append(line.rstrip('\n'))
        return result

def selectThreeOrMoreChannelsFunc():
    with open(selectedChannels, 'r') as file:
        result = []
        for line in file:
            parts = line.split()
            if len(parts) > 2:
                print(' '.join(parts))

def takeRowNumbFunc():
    maxLen = maxLenFunc()
    with open(selectedChannels, 'r') as file:
        with open(rowNumberFile, "w") as file1:
            for line in file:
                x = line.split(' ')
                with open(allChannelsFile, 'r') as file2:
                    for num, allLine in enumerate(file2, 1):
                        y = allLine.split(' ')
                        #change y[channel] for channel which is the first value at file RandomTree
                        if x[0] == y[0]:
                            with open(rowNumberFile, "a") as file1:
                                file1.write(str(num))
                                file1.write('\n')

#take valence, arousal, dominance, liking value (0 or 1) for SVM
def execFunc(label, selectedLabel):
    r = len(readRowNumberFunc())
    re = readRowNumberFunc()
    num = len(takeOneOrZeroValueFunc(label))
    oneOrZero = takeOneOrZeroValueFunc(label)
    with open(selectedLabel, "w") as file:
        for i in range(r):
            for j in range(num):
                if int(j) == int(re[i]):
                    with open(selectedLabel, "a") as file1:
                        file1.write(str(oneOrZero[j]))
                        file1.write('\n')

# sampleFeatures()
# removechannelsemptylines()
# selectThreeOrMoreChannelsFunc()
# takeRowNumbFunc()
execFunc(label0, selectedLabel0)
execFunc(label1, selectedLabel1)
execFunc(label2, selectedLabel2)
execFunc(label3, selectedLabel3)