#!/usr/bin/python
# coding: utf-8 -*-

#area or stack plot are similar to line plots. Are used to track changes over the groups over period of time

from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd

df = pd.read_csv('test.csv')

colname = list(df.columns.values)

Ylabel = colname[0]
del colname[0]

days = []
sleeping = []
eating = []
working = []
playing = []

for element in df.values:
    if element[0] : days.append(element[0])
    if element[1] : sleeping.append(element[1])
    if element[2]: eating.append(element[1])
    if element[3]: working.append(element[1])
    if element[4]: playing.append(element[1])

plt.plot([],[],color='b',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='Eating',linewidth=5)
plt.plot([],[],color='r',label='Working',linewidth=5)
plt.plot([],[],color='w',label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,color=['b','c','r','w'])

plt.xlabel('X')
plt.ylabel(Ylabel)
plt.title('Area Plot')
plt.legend()

plt.show()



