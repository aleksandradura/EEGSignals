from DEAP import name_files as nf, prepareFile as pf

minUser = 0

label_dict = {
    'valence': nf.binaryFileForValence,
    'arousal': nf.binaryFileForArousal
}
def count_number_of_2class():
    counter = 0
    for i in range(len(label_dict)):
        file = open(list(label_dict.values())[i])
        for line in file:
            if int(line) == 1:
                counter += 1
        print(str(list(label_dict.keys())[i]) + ' - 1: ' + str(counter) + ', 0: ' + str(40 - counter))
        counter = 0

def create_array_from_file_line(file):
    array = []
    for line in file:
        array.append(int(line))
    return array

def count_number_of_4class():
    valence = create_array_from_file_line(open(list(label_dict.values())[0]))
    arousal = create_array_from_file_line(open(list(label_dict.values())[1]))
    counter1, counter2, counter3, counter4 = 0, 0, 0, 0
    label4class = []
    for i in range(len(valence)):
        if valence[i] == 0 and arousal [i] == 0:
            label4class.append(1)
            counter1 += 1
        if valence[i] == 0 and arousal[i] == 1:
            label4class.append(2)
            counter2 += 1
        if valence[i] == 1 and arousal[i] == 0:
            label4class.append(3)
            counter3 += 1
        if valence[i] == 1 and arousal[i] == 1:
            label4class.append(4)
            counter4 += 1
    print('1 - ' + str(counter1))
    print('2 - ' + str(counter2))
    print('3 - ' + str(counter3))
    print('4 - ' + str(counter4))
    # print(label4class)
    return label4class

def run_counter():
    for n in range(15, 16):
        pf.convertData(n, n+1)
        pf.prepareLabelsFile()
        print('User:' + str(n + 1))
        count_number_of_2class()
        # count_number_of_4class()

# run_counter()

# data_path = sample.data_path()
# fname_fwd = data_path + '/MEG/sample/sample_audvis-meg-oct-6-fwd.fif'
# raw_fname = "C:\\Users\\aleks\\PycharmProjects\\FeatureSelection\\EEGSignals\\sample_audvis_trunc-meg-eeg-oct-6-fwd.fif"
# raw_fname = "C:\\Users\\aleks\\PycharmProjects\\FeatureSelection\\EEGSignals\\sample_audvis_trunc_raw.fif"


# raw = mne.io.read_raw_fif(raw_fname, preload=True)
# print(raw)
# fwd = mne.read_forward_solution(raw_fname)
# fwd = mne.convert_forward_solution(fwd, surf_ori=True)
# print(raw[0][0])

pf.cleanFile(nf.label4class)
label = count_number_of_4class()
for i in range(len(label)):
    with open(nf.label4class, 'a+') as file:
        for k in range(7680):
            file.write(str(label[i]) + '\n')
        # print(label[i])


