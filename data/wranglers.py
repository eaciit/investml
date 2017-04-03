import numpy as np
import datetime
import os
import glob
import csv
import pandas as pd
from sklearn.preprocessing import normalize

path = "ALL_TIME"
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
    coff = 0
    for ed in d:
        if j == 0:
            j += 1
            continue

        d1 = datetime.datetime.strptime(dates[k][j][0], "%Y-%m-%d")
        d2 = datetime.datetime.strptime(composite_dates[j-coff][0], "%Y-%m-%d")
        if d2 > d1:
            j += 1
            coff -= 1
            continue
        elif d1 > d2:
            j += 1
            coff += 1
            continue

        data[i, 0:6] = ed
        data[i, 6:12] = composite[j-coff]
        data[i, 12] = d[j-1][5]
        j += 1
        i += 1

    k += 1

data = data[:i]
print data.shape

data_s = data[:, :-1]
data_s = normalize(data_s, axis=0)
data = np.concatenate((data_s, data[:, -1:]), axis=1)

np.savetxt("generated/" + path + ".csv", data, delimiter=",")
np.save("generated/" + path + ".npy", data)
