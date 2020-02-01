#!/usr/bin/python
# coding: utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd

#Histograms have quantiative variables

df = pd.read_csv('test.csv')
colm = list(df.columns.values)

#df.fillna(0, inplace=True)

population_ages = []
bins = []

for element in df.values:
    if element[0] : population_ages.append(element[0])
    if element[0]: bins.append(element[1])

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.show()

