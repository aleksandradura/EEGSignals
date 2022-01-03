import gzip
import pickle
import time
import sys
import psutil
import csv
# import mne as mne
import tracemalloc

tracemalloc.start()

# filename = "C:\\datasets\\MAHNOB\\Sessions\\2\\Part_1_S_Trial1_emotion.raw.fif"
# with open(filename, 'rb') as f:
#     print(mne.io.read_raw_fif(f))


fname = 'C:\\datasets\\data_preprocessed_python\\arffFiles\\allChannels.csv'
chList = []
row_count = 0
print('memory % used:', psutil.virtual_memory()[2])
def withGenerator(fname, ch, row_count):
    start = time.time()
    with open(fname, 'r') as f:
        for i in f:
            ch.append(i)
            row_count += 1
            # pass
    end = time.time()
    elapsed = end - start
    # print(elapsed, row_count)
    return ch
def forloop(fname, ch, row_count):
    start = time.time()
    f = open(fname, 'r')
    for i in f:
        ch.append(i)
        row_count += 1
        # pass
    f.close()
    end = time.time()
    elapsed = end - start
    # print("TIME: ", elapsed, row_count)
    return ch

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

def gen(c, ch, row_count):
    start = time.time()
    for row in c:
        ch.append(row)
        row_count += 1
        #pass
    end = time.time()
    elapsed = end - start
    print("TIME: ", elapsed)
    return ch




#ith construction
print(sys.getsizeof(withGenerator(fname, chList, row_count)))

#for loop
# print(sys.getsizeof(forloop(fname, chList, row_count)))

#take all file by one
# print(sys.getsizeof(gen(csv_reader(fname), chList, row_count)))
# csvs = csv_reader(fname)


# print(sys.getsizeof(gen(csvg)))
# print(sys.getsizeof(gen(csvs)))



print('memory % used:', psutil.virtual_memory()[2])


current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
