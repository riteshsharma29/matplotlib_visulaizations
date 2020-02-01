#!/usr/bin/python
# coding: utf-8 -*-

#http://www.chartblocks.com/en/support/faqs/faq/when-to-use-a-bar-chart

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("budget.csv")

y = df['Values'].values

df.plot(kind='bar',color='c',grid=True)

plt.ylabel('Values')

plt.xlabel('Activity')

# range(Number of categories)

plt.xticks(range(6),df['Activity'])

plt.title('2014 Budget: Variance')

for i, v in enumerate(y):
    plt.text(v,i ,str(v), color='blue', fontweight='bold')

plt.show()
