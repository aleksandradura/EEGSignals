forOneValue, total, allrow = 252, 0, 13000
nLabel, nTrial, nUser, nChannel, nTime = 4, 40, 32, 32, 8064
minValue, maxValue = 8, 47

binaryFileForValence = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_0.dat"
labelValenceFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_0.dat'
binary252ValuesValence = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_0_01.dat"

binaryFileForArousal = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_1.dat"
labelArousalFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_1.dat'
binary252ValuesArousal = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_1_01.dat"

binaryFileForDominance = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_2.dat"
labelDominanceFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_2.dat'
binary252ValuesDominance = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_2_01.dat"

binaryFileForLiking = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_3.dat"
labelLikingFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_3.dat'
binary252ValuesLiking = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_3_01.dat"

oneRowFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv'
toFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv'
fromFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\connectTwoFiles.csv'

from shutil import copyfile
#convert files to read
import pickle
def convertData():
    #all 40 features
    data = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\features_raw.dat", 'w')
    #0 - valence, 1 - arousal, 2 - dominance, 3 - liking
    s0 = open(labelValenceFile, 'w')
    s1 = open(labelArousalFile, 'w')
    s2 = open(labelDominanceFile, 'w')
    s3 = open(labelLikingFile, 'w')
    for i in range(nUser):
        if (i % 1 == 0):
            if i < 10:
                name = '%0*d' % (2, i + 1)
            else:
                name = i + 1
        fname = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\s\\s" + str(name) + ".dat"
        f = open(fname, 'rb')
        x = pickle.load(f, encoding='latin1')
        for tr in range(nTrial):
            if (tr % 1 == 0):
                for dat in range(nTime):
                    if (dat % 32 == 0):
                        for ch in range(nChannel):
                            data.write(str(x['data'][tr][ch][dat]) + " ")
                s0.write(str(x['labels'][tr][0]) + "\n")
                s1.write(str(x['labels'][tr][1]) + "\n")
                s2.write(str(x['labels'][tr][2]) + "\n")
                s3.write(str(x['labels'][tr][3]) + "\n")
                data.write("\n")
    s0.close()
    s1.close()
    s2.close()
    s3.close()
    data.close()

def sampleFeatures(n):
    print("Program started"+"\n")
    data = open(oneRowFile,'w')
    for i in range(nUser):
        if(i%1 == 0):
            if i < 10:
                name = '%0*d' % (2,i+1)
            else:
                name = i+1
            fname = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\s\\s"+str(name)+".dat" #pobieranie plików binarnych każdego uczestnika z folderu s
            x = pickle.load(open(fname, 'rb'), encoding='latin1')
            for tr in range(nTrial):
                if(tr%1 == 0):
                    for dat in range(nTime):
                        if(dat%32 == 0):
                            for ch in range(nChannel):
                                #for RCA
                                # if (ch == 19 and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue))) or (ch == 31 and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue))) or (ch == 29 and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue))):# or (ch == 1 and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue))):
                                if ch == n and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue)):
                                #     data.write(str(ch+1) + " ")
                                # if (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7)):
                                    data.write(str(x['data'][tr][ch][dat]) + " ")
                                # else:
                                #     data.write('1 ')

                                if (ch+1 == nChannel):
                                    data.write("\n")
                data.write("\n")
    data.close()

#change value to binary
def changeEmotionsToBinaryValue(binaryFile, labelFile):
    fout_labels_class = open(binaryFile, 'w')
    with open(labelFile, 'r') as f:
        for val in f:
            if float(val) > 4.5:
                fout_labels_class.write(str(1) + "\n")
            else:
                fout_labels_class.write(str(0) + "\n")

# copy 252 times each value
def copy252TimesEachLabelValue(binary252Values, binaryFile):
    fout_labels_class = open(binary252Values, 'w')
    #files with 0-1 values, for one movie 40 rows
    with open(binaryFile, 'r') as f:

        for val in f:
            for forOne in range(forOneValue):
                fout_labels_class.write(str(val))
            fout_labels_class.write("\n")
        fout_labels_class.write("\n")

def remove01emptylines(selectedLabelFiles):
    with open(selectedLabelFiles, "r") as file01:
        lines = file01.readlines()
        with open(selectedLabelFiles, "w") as file01:
            for line in lines:
                if line.strip() != "":
                    file01.write(line)


def mergeLabelsWithChannels(fromFile, toFile, oneRowFile):
    amount = 0
    num_lines1 = sum(1 for line in open(fromFile))
    num_lines2 = sum(1 for line in open(oneRowFile))
    if num_lines1 > num_lines2:
        amount = num_lines2
    else:
        amount = num_lines1
    with open(oneRowFile) as xh:
        with open(fromFile) as yh:
            with open(toFile, "w") as zh:
                xlines = xh.readlines()
                ylines = yh.readlines()
                for i in range(amount - 1):
                        line = ylines[i].strip() + ' ' + xlines[i]
                        zh.write(line)

def copyToOtherFile(fromFile, toFile):
        with open(toFile) as f:
            with open(fromFile, "w") as f1:
                for line in f:
                    f1.write(line)

def cleanFile(copiedFile):
    f = open(copiedFile, 'w')
    f.seek(0)
    f.truncate()
    f.close()

def prepareLabelsFile():
    convertData()

    changeEmotionsToBinaryValue(binaryFileForValence, labelValenceFile)
    copy252TimesEachLabelValue(binary252ValuesValence, binaryFileForValence)
    remove01emptylines(binary252ValuesValence)

    changeEmotionsToBinaryValue(binaryFileForArousal, labelArousalFile)
    copy252TimesEachLabelValue(binary252ValuesArousal, binaryFileForArousal)
    remove01emptylines(binary252ValuesArousal)

    changeEmotionsToBinaryValue(binaryFileForDominance, labelDominanceFile)
    copy252TimesEachLabelValue(binary252ValuesDominance, binaryFileForDominance)
    remove01emptylines(binary252ValuesDominance)

    changeEmotionsToBinaryValue(binaryFileForLiking, labelLikingFile)
    copy252TimesEachLabelValue(binary252ValuesLiking, binaryFileForLiking)
    remove01emptylines(binary252ValuesLiking)


# prepareLabelsFile()

def forOneFrequency():
    count = 0
    cleanFile(fromFile)
    sampleFeatures(0)
    remove01emptylines('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv')
    copyToOtherFile(fromFile, oneRowFile)
    count = 1
    print(count)
    for i in range(1, 32):
        sampleFeatures(i)
        remove01emptylines('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv')
        mergeLabelsWithChannels(fromFile, toFile, oneRowFile)
        copyToOtherFile(fromFile, toFile)
        count += 1
        print(count)


forOneFrequency()







