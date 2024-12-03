import csv
import numpy as np
import pandas as pd

#with open('input') as f:
#    reader = csv.reader(f, delimiter="\s+")
#    data = list(reader)

df = pd.read_csv('input', delimiter=r'\s+', header=None)
print(df.head())

df = df.transform(np.sort)

print(df.head())
print(df.tail())

sum = 0
for i in range(len(df)):
    sum += abs(df[0][i] - df[1][i])

print(sum)

sim_score = 0
for i in range(len(df)):
    count = 0
    for j in range(len(df)):
        if df[0][i] == df[1][j]:
            count += 1
    sim_score += df[0][i] * count

print(sim_score)