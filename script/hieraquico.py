# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


#carregando dados

df = pd.read_excel('dados//Atividade01//atividade_01_experimento_02_tratado02_tese01.xlsx', sheet_name='Planilha1')


X = df.iloc[:,[1,10]].values
X = df.iloc[:, 1:11].values


scaler = StandardScaler()
X = scaler.fit_transform(X)

dendrograma = dendrogram(linkage(X, method = 'ward'))

hc = AgglomerativeClustering(n_clusters = 4, affinity = 'euclidean', linkage = 'ward')
previsoes = hc.fit_predict(X)


plt.scatter(X[previsoes == 0, 0], X[previsoes == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[previsoes == 1, 0], X[previsoes == 1, 1], s = 100, c = 'orange', label = 'Cluster 2')
plt.scatter(X[previsoes == 2, 0], X[previsoes == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.xlabel('x')
plt.ylabel('Y')
plt.legend()