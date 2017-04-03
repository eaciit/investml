import numpy as np
import os
import glob
import csv
import pandas as pd

path = "1Y"
csv_path = glob.glob(path + "/*.csv")

ds = []
dates = []
i = 0
count = 0
for cp in csv_path:
    if os.path.basename(cp).startswith('JKSE'):
        continue

    d = np.loadtxt(cp, delimiter=',', skiprows=1, usecols=range(1,7))
    f = open(cp, 'rb')
    reader = csv.reader(f)
    dates.append(list(reader))

    count += len(d)-1
    ds.append(d)
    i += 1

composite = np.loadtxt(path + "/JKSE.csv", delimiter=',', skiprows=1, usecols=range(1,7))
f = open(path + "/JKSE.csv", 'rb')
reader = csv.reader(f)
composite_dates = list(reader)

# Hard guessing the legth of data
data = np.zeros((count, 6*2+1))
i, k = 0, 0
for d in ds:
    j = 0
    offset = 0
    for ed in d:
        if j == 0:
            j += 1
            continue

        if dates[k][j][0] != composite_dates[j-offset][0]:
            j += 1
            offset += 1
            continue

        data[i, 0:6] = ed
        data[i, 6:12] = composite[j-offset]
        data[i, 12] = d[j-1][5]
        j += 1
        i += 1

    k += 1

data = data[:i]
print data.shape

np.savetxt(path + "/Data.csv", data, delimiter=",")
np.save(path + "/Data.npy", data)
