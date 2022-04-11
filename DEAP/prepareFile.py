import pandas as pd
from DEAP import name_files as nf

forOneValue, total, allrow = 7680, 0, 13000
nLabel, nTrial, nUser, nChannel, nTime = 4, 40, 32, 32, 8064
minValue, maxValue = 30, 47
on, tw = 0, 32

#convert files to read
import pickle
def convertData(minUser, maxUser):
    #all 40 features
    data = open(nf.targetFile + "features_raw.dat", 'w')
    #0 - valence, 1 - arousal, 2 - dominance, 3 - liking
    s0 = open(nf.labelValenceFile, 'w')
    s1 = open(nf.labelArousalFile, 'w')
    s2 = open(nf.labelDominanceFile, 'w')
    s3 = open(nf.labelLikingFile, 'w')
    for i in range(minUser, maxUser):
        if (i % 1 == 0):
            if i < 10:
                name = '%0*d' % (2, i + 1)
            else:
                name = i + 1
        fname = "C:\\datasets\\DEAP\\data_preprocessed_python\\s" + str(name) + ".dat"
        f = open(fname, 'rb')
        x = pickle.load(f, encoding='latin1')
        for tr in range(nTrial):
            if (tr % 1 == 0):
                for dat in range(nTime):
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

def sampleFeatures():
    print("Program started"+"\n")
    data = open('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels.csv','w')
    for i in range(on, tw):
        if(i%1 == 0):
            if i < 10:
                name = '%0*d' % (2,i+1)
            else:
                name = i+1
            fname = "C:\\datasets\\DEAP\\data_preprocessed_python\\s"+str(name)+".dat"
            x = pickle.load(open(fname, 'rb'), encoding='latin1')
            for tr in range(nTrial):
                if(tr%1 == 0):
                    for dat in range(384, nTime):
                        # if(dat%32 == 0):
                            for ch in range(nChannel):
                                #for RCA
                                #dlav4
                                # if (ch == 24  or ch == 5 or ch == 12 or ch == 19):
                                #dla 6
                                #if (ch == 24  or ch == 5 or ch == 12 or ch == 19 or ch == 4 or ch == 23):# or ch==11 or ch==13 or ch==25 or ch==27 or ch==31):# or ch == 9):# or ch == 23 or ch == 2 or ch == 29):#  or ch == 30 or ch == 26):# or (ch == 25 and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue))):
                                #dla 11
                                #if (ch == 24  or ch == 5 or ch == 12 or ch == 19 or ch == 4 or ch == 23 or ch==11 or ch==13 or ch==25 or ch==27 or ch==31):

                                # if ch == n and (float(x['data'][tr][ch][dat]) > float(minValue) and float(x['data'][tr][ch][dat]) < float(maxValue)):
                                #dla 28
                                # if ch not in (0,1,9,20):
                                    # print(ch)
                                data.write(str(x['data'][tr][ch][dat]) + " ")
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
            for forOne in range(30):
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
            with open(fromFile, "r+") as f1:
                for line in f:
                    f1.write(line)

def cleanFile(copiedFile):
    f = open(copiedFile, 'r+')
    f.truncate()
    f.close()

def prepareLabelsFile():


    changeEmotionsToBinaryValue(nf.binaryFileForValence, nf.labelValenceFile)
    copy252TimesEachLabelValue(nf.binary252ValuesValence, nf.binaryFileForValence)
    remove01emptylines(nf.binary252ValuesValence)

    changeEmotionsToBinaryValue(nf.binaryFileForArousal, nf.labelArousalFile)
    copy252TimesEachLabelValue(nf.binary252ValuesArousal, nf.binaryFileForArousal)
    remove01emptylines(nf.binary252ValuesArousal)

    # changeEmotionsToBinaryValue(binaryFileForDominance, labelDominanceFile)
    # copy252TimesEachLabelValue(binary252ValuesDominance, binaryFileForDominance)
    # remove01emptylines(binary252ValuesDominance)
    #
    # changeEmotionsToBinaryValue(binaryFileForLiking, labelLikingFile)
    # copy252TimesEachLabelValue(binary252ValuesLiking, binaryFileForLiking)
    # remove01emptylines(binary252ValuesLiking)



def forOneFrequency():
    count = 0
    cleanFile(nf.fromFile)
    sampleFeatures(0)
    remove01emptylines(nf.targetFile + 'RandomTree.csv')
    copyToOtherFile(nf.fromFile, nf.oneRowFile)
    count = 1
    print(count)
    for i in range(0, 32):
        sampleFeatures(i)
        remove01emptylines(nf.targetFile + 'RandomTree.csv')
        mergeLabelsWithChannels(nf.fromFile, nf.toFile, nf.oneRowFile)
        copyToOtherFile(nf.fromFile, nf.toFile)
        count += 1
        print(count)
def deleteLatestColumn(file_name):
    df = pd.read_csv(file_name, sep=' ')
    df = df.iloc[: , : -1]
    df.to_csv(file_name, index=False, sep = ' ')

# forOneFrequency()
# convertData(on, tw)
# prepareLabelsFile()
# sampleFeatures()
# remove01emptylines('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels.csv')
# name = 'C:\\datasets\\data_preprocessed_python\\asdf.csv'
# deleteLatestColumn('C:\\datasets\\DEAP\\data_preprocessed_python\\allChannels.csv')

# copy252TimesEachLabelValue('C:\\datasets\\data_preprocessed_python\\1200.dat', 'C:\\datasets\\data_preprocessed_python\\labels_0.dat')







