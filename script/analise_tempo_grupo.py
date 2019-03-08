# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



#carregando dados

df = pd.read_excel('dados//dados_agupados_tempo.xlsx', sheet_name='Planilha1')
df1 = df.values




boxplot = df.boxplot(column=['a', 'b', 'c','d','e','f'])
boxplot = df.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))


a = df.iloc[:, 0:1]
boxplot = a.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))

b = df.iloc[:, 1:2]
boxplot = b.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))

c = df.iloc[:, 2:3]
boxplot = c.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))

d = df.iloc[:, 3:4]
boxplot = d.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))

e = df.iloc[:, 4:5]
boxplot = e.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))

f = df.iloc[:, 4:5]
boxplot = f.boxplot(grid=True, rot=45, fontsize=12, figsize =(9,6))