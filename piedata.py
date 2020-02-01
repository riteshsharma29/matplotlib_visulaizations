#!/usr/bin/python
# coding: utf-8 -*-

#pie plots are similar to stack plot only they certain point in time. Use to show percentage in share

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("piedata.csv")

for lst in df.values:
    mylist = lst

activities = list(df.columns.values)

cols = ['r','b','m','c','k','g','w','navy','khaki','pink']

slices = mylist

plt.pie(slices,
    labels=activities,
    colors=cols,
    startangle=90,
    shadow=True,
    explode=(0,0,0.1,0), #0.1 is used to explote the slice-share use 0.0 instead if this feature is not required.
    autopct='%1.1f%%'
)

plt.title('Pie Plot')

plt.show()

