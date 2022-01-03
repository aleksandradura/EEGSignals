import os
import numpy as np  # linear algebra
import pandas as pd  # data processing
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal

from scipy.signal import welch

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# /kaggle/input/eeg-sample/samplingPD.csv


col_list = ["channel1"]
df_ch1 = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\samplingPD.csv", usecols=col_list)
df_ch1.insert(loc=0, column='No', value=np.arange(1, len(df_ch1) + 1))
# col_list = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8", "ch9", "ch10", "ch11", "ch12", "ch13", "ch14", "ch15", "ch16", "ch17", "ch18", "ch19", "ch20",
#             "ch21", "ch22", "ch23", "ch24", "ch25", "ch26", "ch27", "ch28", "ch29", "ch30", "ch31", "ch32"]
# df_ch1 = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", sep= " ", names=col_list)
# df_ch1.insert(loc=0, column='No', value=np.arange(1, len(df_ch1) + 1))

# print(df_ch1)

# Show the plot for time-domain
# sns.lineplot(x = "No", y = "channel1", data=df_ch1)
# plt.show()

# transform to frequency-domain
# fs = 512                                # Sampling rate (512 Hz)
fs = 128


def get_psd_values(y_values, f_s):
    f_values, psd_values = welch(y_values, fs=fs)
    return f_values, psd_values

f_values, psd_values = get_psd_values(np.abs(df_ch1["channel1"]), fs)
print(psd_values, f_values)


# # Get real amplitudes of FFT (only in postive frequencies)
fft_vals = np.absolute(np.fft.rfft(df_ch1["channel1"]))
print(fft_vals)

# Get frequencies for amplitudes in Hz
fft_freq = np.fft.rfftfreq(len(df_ch1["channel1"]), 1.0 / fs)
print(fft_freq)
# Define EEG bands
eeg_bands = {'Delta': (0, 4),
             'Theta': (4, 8),
             'Alpha': (8, 12),
             'Beta': (12, 30),
             'Gamma': (30, 45)}

df_subbands_one_ch = pd.DataFrame(columns=["Delta", "Theta", "Alpha", "Beta", "Gamma"])

# Take the mean of the fft amplitude for each EEG band. Enter subbands into dataframe
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((fft_freq >= eeg_bands[band][0]) &
                       (fft_freq <= eeg_bands[band][1]))[0]
    print(band)
    print("freq_ix= " + str(freq_ix) + " fft_vals[freq_ix]= " + str(fft_vals[freq_ix]))
    # df_subbands_one_ch[band]=fft_vals[freq_ix]
    df_subbands_one_ch[band] = pd.Series(fft_vals[freq_ix])
    eeg_band_fft[band] = np.mean(fft_vals[freq_ix])

# Plot the data (using pandas here cause it's easy)
print(df_subbands_one_ch)

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")



print("done")


import os
import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import welch
from scipy.fft import fft, ifft
from scipy import fftpack

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# /kaggle/input/eeg-sample/samplingPD.csv


col_list = ["channel1"]
df_ch1 = pd.read_csv("/kaggle/input/eeg-sample4/samplingPD-2.csv", usecols=col_list)

print(df_ch1)
print("DONE1")


#transform to frequency-domain
#fs = 512                                # Sampling rate (512 Hz)
fs = 128

#print("f_s= " + str(f_s))

# The FFT of the signal
sig_fft = fftpack.fft(df_ch1)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(df_ch1.size+1, d=1./fs)
print(power)
print("razem= " + str(np.count_nonzero(power)))


# Define EEG bands
eeg_bands = {'Delta': (0, 4),
             'Theta': (4, 8),
             'Alpha': (8, 12),
             'Beta': (12, 30),
             'Gamma': (30, 45)}


df_subbands = pd.DataFrame(columns = ["Delta", "Theta", "Alpha", "Beta", "Gamma"])

# Take the mean of the fft amplitude for each EEG band. Enter subbands into dataframe
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((abs(power) >= eeg_bands[band][0]) &
                       (abs(power) <= eeg_bands[band][1]))[0]
    print(band)
    print("freq_ix= " + str(freq_ix) + " fft_vals[freq_ix]= " + str(power[freq_ix]))

    print("razem= " + str(np.count_nonzero(sample_freq[freq_ix])))


#40 filmików 32 uczestników
print("done")



