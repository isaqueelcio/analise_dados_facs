# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np


df = pd.read_excel('dados//Atividade01//atividade_01_experimento_02_tratado02_tese01.xlsx', sheet_name='Planilha1')


X = df.iloc[:,[1,10]].values
X = df.iloc[:, 1:11].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

dbscan = DBSCAN(eps = 0.8, min_samples = 10)
previsoes = dbscan.fit_predict(X)
unicos, quantidade = np.unique(previsoes, return_counts = True)

plt.scatter(X[previsoes == -1, 0], X[previsoes == -1, 1], s = 100, c = 'brown', label = 'Cluster -1')
plt.scatter(X[previsoes == 0, 0], X[previsoes == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[previsoes == 1, 0], X[previsoes == 1, 1], s = 100, c = 'orange', label = 'Cluster 2')
plt.scatter(X[previsoes == 2, 0], X[previsoes == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[previsoes == 3, 0], X[previsoes == 3, 1], s = 100, c = 'green', label = 'Cluster 4')
plt.scatter(X[previsoes == 4, 0], X[previsoes == 4, 1], s = 100, c = 'green', label = 'Cluster 5')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()