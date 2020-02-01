#!/usr/bin/python
# coding: utf-8 -*-

#http://www.chartblocks.com/en/support/faqs/faq/when-to-use-a-bar-chart

'''
If you have comparative data that you would like to represent through a chart then a bar chart would be the best option. This type of chart is one of the more familiar options as it is easy to interpret. These charts are useful for displaying data that is classified into nominal or odinal categories. A good example of a bar chart can be seen below.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

y = df['Time (mins)'].values

df.plot(kind='barh',color='g')

plt.xlabel('Time in (ms)')

plt.ylabel('Activity')

# range(Number of categories)

plt.yticks(range(10),df['Activity'])

plt.title('Average time spent on smartphones daily')

for i, v in enumerate(y):
    plt.text(v,i ,str(v), color='blue', fontweight='bold')

plt.show()
