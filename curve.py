#!/usr/bin/python
# coding: utf-8 -*-

#http://pandas.pydata.org/pandas-docs/stable/visualization.html

import pandas as pd
from pandas.tools.plotting import andrews_curves
import matplotlib.pyplot as plt

data = pd.read_csv('iris.csv')
andrews_curves(data, 'Name')

plt.show()