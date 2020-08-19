forOneValue, total, allrow = 252, 0, 10112
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 32, 40, 8064
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
    for i in range(22):
        if (i % 1 == 0):
            if i < 10:
                name = '%0*d' % (2, i + 1)
            else:
                name = i + 1
        #pobranie wszystkich plików (32 pliki - 1 plik dla każdego uczestnika) z folderu
        fname = "C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\s\\s" + str(name) + ".dat"
        f = open(fname, 'rb')
        x = pickle.load(f, encoding='latin1')
        for tr in range(22):
            if (tr % 1 == 0):
                for dat in range(8064):
                    if (dat % 32 == 0):
                        for ch in range(40):
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

    for i in range(22):
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
                        if(dat%32 == 0 ):
                            for ch in range(32): #ilość kanałów
                                # if (ch == 4 or ch == 16 or ch == 31):# or ch == 33 or ch == 34 or ch == 35 or ch == 36  or ch == 37 or ch == 38 or ch == 39 ): #ReliefAttribute10
                                # if (ch == 4 or ch == 7 or ch == 16 or ch == 19  or ch == 21 or ch == 24 or ch == 31): #or ch == 33 or ch == 34 or ch == 35 or ch == 36 or ch == 37 or ch == 38 or ch == 39): #Relief5
                                #if (ch == 32 or ch == 33 or ch == 34 or ch == 35 or ch == 36 or ch == 37 or ch == 38 or ch == 39 ):  # 33-40
                                # if (ch == 12 or ch == 29 or ch == 31): # or ch == 33 or ch == 34 or ch == 35 or ch == 36 or ch == 37 or ch == 38 or ch == 39):  # Naive-bayes
                                # if (ch == 12 or ch == 30 or ch == 31):  # Pz 13, Fz 31, Cz 32
                                # if (ch == 8 or ch == 15 or ch == 24 or ch == 31):  # valence, beta, CP1 9, Oz 16, FC6 25, Cz 32
                                # if (ch == 6 or ch == 20 or ch == 21 or ch == 22 or ch==23 or ch==24 or ch==27 or ch==31):  # valence, gamma, T7 7, CP6 21, CP2 22, C4 23, T8 24, FC6 25, F8 28
                                if ((ch == 7 and (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29))) or (ch == 16 and (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29))) or (ch == 23 and (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29)))):  # arousal, theta CP6 21, alpha Cz 32, beta FC2 26
                                # if ((ch == 20 and (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7))) or (ch == 25 and (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29))) or (ch == 31 and (float(x['data'][tr][ch][dat]) > float(8) and float(x['data'][tr][ch][dat]) < float(13)))):  # arousal, theta CP6 21, alpha Cz 32, beta FC2 26
                                # if ((ch == 26 and (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7))) or (ch == 31 and (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29))) or (ch == 22 and (float(x['data'][tr][ch][dat]) > float(8) and float(x['data'][tr][ch][dat]) < float(13)))):  #Geneva: arousal, theta CP6 21, alpha Cz 32, beta FC2 26
                                #if (ch != 5 and ch != 8 and ch != 19):  # RandomTree
                                #if (ch!=14 and ch!=9 and ch!=31): #k10 dla valence
                                # if (ch != 14 and ch != 6 and ch != 13):  # k5 dla valence
                                # if (ch != 31 and ch != 14):  # k10 dla arousal
                                # if (ch != 14 and ch != 31 and ch != 6 and ch !=13):  # k5 dla arousal
                                #if (ch != 14 and ch != 31 and ch != 9 and ch !=23):  # k10 dla dominance
                                # if (ch!=6 and ch != 14 and ch != 9 and ch != 13 and ch !=31):  # k5 dla dominance
                                # if (ch != 14 and ch != 31 and ch != 9):  # k10 dla liking
                                #if (ch != 13 and ch != 9 and ch != 6 and ch !=14):  # k5 dla liking
                                #     data.write(str(ch+1) + " ")
                                #     if (float(x['data'][tr][ch][dat]) > float(8) and float(x['data'][tr][ch][dat]) < float(13)):
                                    # if (float(x['data'][tr][ch][dat]) > float(3) and float(x['data'][tr][ch][dat]) < float(7)):
                                    # if (float(x['data'][tr][ch][dat]) > float(14) and float(x['data'][tr][ch][dat]) < float(29)):
                                    data.write(str(x['data'][tr][ch][dat]) + " ")
                                if (ch+1 == 32):
                                    data.write("\n")
                data.write("\n")
    data.close()

# zamiana emocji na wartości binarne
def changeEmotionsToBinaryValue():
    fout_labels_class = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_3.dat", 'w')
    with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_3.dat', 'r') as f:
        for val in f:
            if float(val) > 4.5:
                fout_labels_class.write(str(1) + "\n")
            else:
                fout_labels_class.write(str(0) + "\n")

# powielenie 252 wartości dla każdej emocji
def copy252TimesEachLabelValue():
    fout_labels_class = open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\labels_252_3_01.dat", 'w')
    #plik z wartościami 0-1 dla jednego filmiku [40 wierszy])
    with open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\label_class_3.dat', 'r') as f:

        for val in f:
            for forOne in range(forOneValue):
                fout_labels_class.write(str(val))
            fout_labels_class.write("\n")
        fout_labels_class.write("\n")

# convertData()
sampleFeatures()
# changeEmotionsToBinaryValue()
# copy252TimesEachLabelValue()




