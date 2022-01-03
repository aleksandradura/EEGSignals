# import pandas as pd
# def add01ValueForLabel(p, lab):
#     # power, sample_freq = fastFourierTransform()
#     countAll = []
#     count = 0
#     countingRows = {}
#     for i in range(len(p)):
#         if p[i] == 0:
#             count += 1
#             countingRows[i] = p[i - 1]
#             countAll.append(i)
#             # countingRows.append(i + 1)
#     # print("razem= " + str(np.count_nonzero(power)))
#     # print("0 counter= " + str(count))
#     # for x, y in countingRows.items():
#         # print(str(x) + ' ' + str(y))
#     k, a = 0, 0
#     with open(label1, 'w') as fi:
#         for z in range(len(lab)):
#             a = countAll[k]
#             for h in range(a):
#                 fi.write(lab[z])
#                 fi.write("\n")
#             k += 1
#
# first get all lines from file
# with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", 'r') as f:
#     lines = f.readlines()
#
# # remove spaces
# lines = [line.replace(' \n', '\n') for line in lines]
#
# # finally, write lines in the file
# with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", 'w') as f:
#     f.writelines(lines)

# with open("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", 'r+') as f:
#     txt = f.read().replace(' \n', '\n')
#     f.seek(0)
#     f.write(txt)
#     f.truncate()

import matplotlib.pyplot as plt
# Import seaborn
import seaborn as sns
import pandas as pd
# Apply the default theme
df = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv", sep=' ')
df.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32', 'ch33']

X, Y, Z, H, M, Q = [], [], [], [], [], []
summ = 0
for i in range(60):
    for j in range(128):
        Y.append(i+1)
for line in open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv', 'r'):
  values = [float(s) for s in line.split()]
  X.append(abs(values[8]))
# for i in range(60):
#     Y.append(i+1)

for line in open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv', 'r'):
  values = [float(s) for s in line.split()]
  M.append(abs(values[9]))
for line in open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv', 'r'):
  values = [float(s) for s in line.split()]
  H.append(abs(values[3]))
for line in open('C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\arffFiles\\allChannels.csv', 'r'):
  values = [float(s) for s in line.split()]
  Z.append(abs(values[28]))


max = 0
for j in range(len(X)):
    if max < X[j]:
        max = X[j]
    if j % 128 == 0:
        Q.append(max)
        max = 0
# for i in range(len(Q)):
#     print(str(i) + ': '+ str(Q[i]))
# print(len(Q))



# for i in range(60):
#     Y.append(i+1)
#     k = 0
# for i in range(60):
#     for j in range(128):
#         summ += abs(X[k])
#         k+=1
#     print(summ)
#     Z.append(summ/(j+1))
#     summ = 0
# for l in range(len(Z)):
#     print(Z[l])


a = sns.lineplot(x = Y,  y = X, color = 'purple')
plt.ylim(0, 50)
a.set(xlabel="time [s]", ylabel = "frequency [Hz]")
plt.legend(labels = ["mean", "std"])
plt.show()
# #
a = sns.lineplot(x = Y,  y = M, color = 'seagreen')
plt.ylim(0, 50)
a.set(xlabel="time [s]", ylabel = "frequency [Hz]")
plt.legend(labels = ["mean", "std"])
plt.show()
a = sns.lineplot(x = Y,  y = H, color = 'firebrick')
plt.ylim(0, 50)
a.set(xlabel="time [s]", ylabel = "frequency [Hz]")
plt.legend(labels = ["mean", "std"])
plt.show()
a = sns.lineplot(x = Y,  y = Z, color = 'darkorange')
plt.ylim(0, 50)
a.set(xlabel="time [s]", ylabel = "frequency [Hz]")
plt.legend(labels = ["mean", "std"])
plt.show()
# import numpy as np
# w = np.array(Q)
# z = np.array(Y)
# print(w)
# print(z)
import matplotlib.pyplot as plt
# plt.plot(z, w)
# plt.show()
# a = sns.lineplot(x = z,  y =w, color = 'firebrick')
# plt.ylim(0, 50)
# a.set(xlabel="time", ylabel = "frequency")
# plt.show()


# import pandas as pd
# ix_rows = ['1608', '2863', '11187', '12791', '13463', '68437', '105703', '115066', '125605', '176359', '209875', '327764', '342723', '410299', '416891', '458693', '493696', '529017', '538146', '575199', '630322', '631696', '633419', '637435', '637436', '653495', '667731', '671216', '685746', '698346', '702169', '702711', '703417', '706207', '708320', '712921', '718161', '721764', '729980', '730106', '730728', '731632', '741772', '743174', '747310', '747908', '750856', '752073', '754272', '755332', '758573', '768288', '769947', '771262', '773736', '774169', '774547', '775740', '775743', '780189', '785892', '786596', '786680', '792516', '792752', '793529', '794428', '796664', '801305', '802035', '803088', '805409', '805824', '806352', '808270', '808359', '811753', '813702', '821437', '822600', '828776', '830463', '830721', '832934', '842471', '847027', '848380', '851769', '853717', '857492', '860156', '864474', '864742', '869258', '875455', '878464', '880187', '898613', '903165', '908303', '910117', '910258', '910857', '912284', '914645', '924845', '953514', '955046', '995763', '996360', '997840', '1015181', '1030321', '1057793', '1083027', '1088069', '1102378', '1117747', '1150939', '1165223', '1165290', '1263852', '1536466', '1546789', '1549334', '1549573', '1557187', '1561180', '1581828']
#
# df = pd.read_csv("C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\bbb.csv", sep=' ')
# # df_ch1.columns = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14', 'ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31', 'ch32', 'ch33']
# df.columns = ['1', '2', '3', '4', '5']
# index = df.index
# numb_of_rows = len(index)
# # print(numb_of_rows)
# df.insert(0, 'row_num', range(0,len(df)))
# print(df)
# # for col in range(len(list(df.columns.values)) - 1):
#
# def takeR(n):
#     ro = []
#     # u = df.columns.values
#     # for col in range(len(list(df.columns.values)) - 1):
#     #     n = '2'
#     for i in range(len(ix_rows)):
#         # print(ix_rows[i])
#         # if df.columns.values[n] == '2':
#             k = df.loc[df[n] == int(ix_rows[i])]
#             print(k.row_num)
#         # ro.append(int(k.row_num))
#
#     # k = df['1'].where(df['1'] == 1630)
#     # print(k)
#
#     # for j in range(len(ro)):
#     #     print(ro[j])
#     # return ro
# takeR('1')