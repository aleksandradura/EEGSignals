import mne

file = 'C:\\datasets\\DEAP\\data_original\\'
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(file) if isfile(join(file, f))]
for i in range(len(onlyfiles)):
    raw = mne.io.read_raw_bdf(file+onlyfiles[i], preload = False)
    data, times = raw[: 32,:]
    for row in range(len(times) - 1, len(times)):
        # for col in range(len(data)):
        print(str(row) + str(': ') + str(times[row]))
# print(str(len(times)))

# mne.io.save(raw, 'C:\\datasets\\DEAP\\data_original\\user1.csv')
# print(times.shape)
# for row in range(len(times)):
#     print(times[row])