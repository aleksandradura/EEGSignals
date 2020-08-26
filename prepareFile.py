forOneValue, total, allrow = 252, 0, 10112
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 22, 32, 8064


BinaryFileForValence = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_0.dat"
labelValenceFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_0.dat'
Binary252ValuesValence = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_0_01.dat"

BinaryFileForArousal = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_1.dat"
labelArousalFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_1.dat'
Binary252ValuesArousal = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_1_01.dat"

BinaryFileForDominance = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_2.dat"
labelDominanceFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_2.dat'
Binary252ValuesDominance = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_2_01.dat"

BinaryFileForLiking = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_3.dat"
labelLikingFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_3.dat'
Binary252ValuesLiking = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_3_01.dat"

#konwersja plików na format do odczytu
import pickle
def convertData():
    #plik ze wszystkimi 40 cechami
    data = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\features_raw.dat", 'w')
    #0 - valence, 1 - arousal, 2 - dominance, 3 - liking
    s0 = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_0.dat", 'w')
    s1 = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_1.dat", 'w')
    s2 = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_2.dat", 'w')
    s3 = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_3.dat", 'w')
    for i in range(nUser):
        if (i % 1 == 0):
            if i < 10:
                name = '%0*d' % (2, i + 1)
            else:
                name = i + 1
        #pobranie wszystkich plików (32 pliki - 1 plik dla każdego uczestnika) z folderu
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

#ilość wierszy dla każdego uczestnika: 10080
def sampleFeatures():
    print("Program started"+"\n")
    data = open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv','w')

    for i in range(nUser):
        if(i%1 == 0):
            if i < 10:
                name = '%0*d' % (2,i+1)
            else:
                name = i+1
            fname = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\s\\s"+str(name)+".dat" #pobieranie plików binarnych każdego uczestnika z folderu s
            x = pickle.load(open(fname, 'rb'), encoding='latin1')
            for tr in range(nTrial): #ilość prób
                if(tr%1 == 0):
                    for dat in range(nTime): #czas
                        if(dat%32 == 0):
                            for ch in range(nChannel): #ilość kanałów
                                # if (ch == 6 or ch == 20 or ch == 21 or ch == 22 or ch==23 or ch==24 or ch==27 or ch==31):  # valence, gamma, T7 7, CP6 21, CP2 22, C4 23, T8 24, FC6 25, F8 28
                                #for beta RCA
                                # if ((ch == 0 and (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7))) or (ch == 1 and (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7))) or (ch == 23 and (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29)))):
                                # if ch == 0 or ch == 1 or ch == 31:
                                if ((ch == 0 and ((float(x['data'][tr][ch][dat]) > float(8) and float(x['data'][tr][ch][dat]) < float(13)) or (float(x['data'][tr][ch][dat]) < float(-8) and float(x['data'][tr][ch][dat]) > float(-13)))) or (ch == 30 and ((float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29)) or (float(x['data'][tr][ch][dat]) < float(-14) and float(x['data'][tr][ch][dat]) > float(-29)))) or (ch == 11 and ((float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29)) or (float(x['data'][tr][ch][dat]) < float(-14) and float(x['data'][tr][ch][dat]) > float(-29))))):  # arousal, theta CP6 21, alpha Cz 32, beta FC2 26
                                # if ch == n and ((float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29) or float(x['data'][tr][ch][dat]) < float(-14) and float(x['data'][tr][ch][dat]) > float(-29))):
                                # if ch == 0 and (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7)):
                                #     data.write(str(ch+1) + " ")
                                #     if (float(x['data'][tr][ch][dat]) > float(8) and float(x['data'][tr][ch][dat]) < float(13)):
                                # if (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7)):
                                # if (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29)):
                                    data.write(str(x['data'][tr][ch][dat]) + " ")
                                # else:
                                #     data.write('1 ')

                                if (ch+1 == nChannel):
                                    data.write("\n")
                data.write("\n")
    data.close()

# zamiana emocji na wartości binarne
def changeEmotionsToBinaryValue(BinaryFile, labelFile):
    fout_labels_class = open(BinaryFile, 'w')
    with open(labelFile, 'r') as f:
        for val in f:
            if float(val) > 4.5:
                fout_labels_class.write(str(1) + "\n")
            else:
                fout_labels_class.write(str(0) + "\n")

# powielenie 252 wartości dla każdej emocji
def copy252TimesEachLabelValue(Binary252Values, BinaryFile):
    fout_labels_class = open(Binary252Values, 'w')
    #plik z wartościami 0-1 dla jednego filmiku [40 wierszy])
    with open(BinaryFile, 'r') as f:

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

def connectLabesWithChannels():
    with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv') as xh:
      with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\connectTwoFiles.csv') as yh:
          with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv', "w") as zh:

            xlines = xh.readlines()
            ylines = yh.readlines()
            for i in range(allrow):
                line = ylines[i].strip() + ' ' + xlines[i]
                zh.write(line)

def copyToOtherFile():
        with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\asdf.csv") as f:
            with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\connectTwoFiles.csv", "w") as f1:
                for line in f:
                    f1.write(line)
# convertData()

# for i in range(0, 32):
#     sampleFeatures(i)
#     remove01emptylines('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv')
#     connectLabesWithChannels()
#     copyToOtherFile()


sampleFeatures()
# remove01emptylines('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\RandomTree.csv')


# changeEmotionsToBinaryValue(BinaryFileForValence, labelValenceFile)
# copy252TimesEachLabelValue(Binary252ValuesValence, BinaryFileForValence)
# remove01emptylines(Binary252ValuesValence)
#
# changeEmotionsToBinaryValue(BinaryFileForArousal, labelArousalFile)
# copy252TimesEachLabelValue(Binary252ValuesArousal, BinaryFileForArousal)
# remove01emptylines(Binary252ValuesArousal)
#
# changeEmotionsToBinaryValue(BinaryFileForDominance, labelDominanceFile)
# copy252TimesEachLabelValue(Binary252ValuesDominance, BinaryFileForDominance)
# remove01emptylines(Binary252ValuesDominance)
#
# changeEmotionsToBinaryValue(BinaryFileForLiking, labelLikingFile)
# copy252TimesEachLabelValue(Binary252ValuesLiking, BinaryFileForLiking)
# remove01emptylines(Binary252ValuesLiking)



