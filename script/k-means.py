# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('dados//Atividade01//atividade_01_experimento_02_tratado02_tese01.xlsx', sheet_name='Planilha1')


X = df.iloc[:,[1,10]].values
X = df.iloc[:, 1:10].values

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')

kmeans = KMeans(n_clusters = 8, random_state = 0)
previsoes = kmeans.fit_predict(X)

plt.scatter(X[previsoes == -1, 0], X[previsoes == -1, 1], s = 100, c = 'brown', label = 'Cluster -1')
plt.scatter(X[previsoes == 0, 0], X[previsoes == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[previsoes == 1, 0], X[previsoes == 1, 1], s = 100, c = 'orange', label = 'Cluster 2')
plt.scatter(X[previsoes == 2, 0], X[previsoes == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[previsoes == 3, 0], X[previsoes == 3, 1], s = 100, c = 'green', label = 'Cluster 4')
plt.scatter(X[previsoes == 4, 0], X[previsoes == 4, 1], s = 100, c = 'green', label = 'Cluster 5')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()




lista_clientes = np.column_stack((base, previsoes))
lista_clientes = lista_clientes[lista_clientes[:,26].argsort()]
