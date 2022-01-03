import numpy as np
from scipy.io import loadmat  # this is the SciPy module that loads mat-files
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd

# mat = loadmat('C:\\datasets\\SEED_IV\\eeg_raw_data\\1\\1_20160518.mat')  # load mat-file
# print(type(mat))

# print(len(mat['cz_eeg1']))
# for keys,values in mat.items():
# # for i in range(len(mat['cz_eeg1'])):
# #     for j in range(len(mat['cz_eeg1'])):
#         # print(str(mat['cz_eeg1'][i][j]) + ", ")
#     # print("\n")
#     #     a = values[i]
#     print(keys)
#     #     print(str(i) + ': ')
#     #     print(values[i])
#     print(values)
    # break
# mdata = mat['measuredData']  # variable in mat file
# mdtype = mdata.dtype  # dtypes of structures are "unsized objects"
# * SciPy reads in structures as structured NumPy arrays of dtype object
# * The size of the array is the size of the structure array, not the number
#   elements in any particular field. The shape defaults to 2-dimensional.
# * For convenience make a dictionary of the data using the names from dtypes
# * Since the structure has only one element, but is 2-D, index it at [0, 0]
# ndata = {n: mdata[n][0, 0] for n in mdtype.names}
# Reconstruct the columns of the data table from just the time series
# Use the number of intervals to test if a field is a column or metadata
# columns = [n for n, v in ndata.iteritems() if v.size == ndata['numIntervals']]
# now make a data frame, setting the time stamps as the index
# df = pd.DataFrame(np.concatenate([ndata[c] for c in columns], axis=1),
#                   index=[datetime(*ts) for ts in ndata['timestamps']],
#                   columns=columns)

import pandas as pd
import statistics
from scipy import stats
import numpy as np
import seaborn as sns

df = pd.read_csv('C:\\Users\\aleks\\OneDrive\\Pulpit\\doktorat\\app1.csv', sep=' ')
df.columns = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

print("Correlation table: ")
print(df.corr())
corr = df.corr()
# corr.style.background_gradient(cmap='coolwarm')
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values, annot=True, fmt=".2")
# plt.matshow(df.corr())
plt.show()