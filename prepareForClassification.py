forOneValue, total, allrow = 252, 0, 10112
allChannelsFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv'
selectedChannels = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'
rowNumberFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\rownumber.csv'
selectedLabel = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\0.csv'

#ilość wierszy dla każdego uczestnika: 10080
import pickle
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
            for tr in range(40): #ilość prób
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

def removechannelsemptylines():
    with open(allChannelsFile, "r") as file:
        lines = file.readlines()
        with open(allChannelsFile, "w") as file:
            for line in lines:
                if line.strip() != "":
                    file.write(line)

#to samo co pobieranie len do wartości num
def maxLenFunc():
    with open(allChannelsFile, 'r') as fileValue:
        maxLen = len(fileValue.readlines())
        return maxLen
# print(maxLenFunc()) 10080

def takeOneOrZeroValueFunc():
    with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_2_01.dat', 'r') as fileValue:
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

# def ifTwoValueFunc():
#     with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv', 'r') as file:
#         temp = []
#         for line in file:
#             if ' ' in line:
#                 x = line.split(' ')
#     return x
#
# print(ifTwoValueFunc())

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
                        if x[0] == y[7]:
                            with open(rowNumberFile, "a") as file1:
                                file1.write(str(num))
                                file1.write('\n')
                            # print(num)

def execFunc():
    r = len(readRowNumberFunc())
    re = readRowNumberFunc()
    num = len(takeOneOrZeroValueFunc())
    oneOrZero = takeOneOrZeroValueFunc()
    with open(selectedLabel, "w") as file:
        for i in range(r):
            for j in range(num):
                if int(j) == int(re[i]):
                    with open(selectedLabel, "a") as file1:
                        file1.write(str(oneOrZero[j]))
                        file1.write('\n')
                    # print(oneOrZero[j])


# sampleFeatures()
# removechannelsemptylines()
# selectThreeOrMoreChannelsFunc()
# takeRowNumbFunc()
execFunc()