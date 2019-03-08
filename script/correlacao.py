# -*- coding: utf-8 -*-

#importes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#carregando dados

df = pd.read_excel('dados//Atividade01//atividade_01_experimento_02_tratado03_tese4.xlsx', sheet_name='Planilha1')

df = pd.read_excel('dados//Atividade01//atividade_01_experimento_02.xlsx', sheet_name='Planilha1')


df1 = df


df2 = df1.iloc[:, 2:11].values
teste = df1.iloc[:, 1:2].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_previsores = LabelEncoder()

df2 [:, 1] = labelencoder_previsores.fit_transform(df2 [:, 1])
df2 [:, 2] = labelencoder_previsores.fit_transform(df2 [:, 2])
df2 [:, 3] = labelencoder_previsores.fit_transform(df2 [:, 3])
df2 [:, 4] = labelencoder_previsores.fit_transform(df2 [:, 4])
df2 [:, 5] = labelencoder_previsores.fit_transform(df2 [:, 5])
df2 [:, 6] = labelencoder_previsores.fit_transform(df2 [:, 6])
df2 [:, 7] = labelencoder_previsores.fit_transform(df2 [:, 7])
df2 [:, 8] = labelencoder_previsores.fit_transform(df2 [:, 8])
df2 [:, 9] = labelencoder_previsores.fit_transform(df2 [:, 9])
teste[1] = labelencoder_previsores.fit_transform(teste[1])


onehotencoder = OneHotEncoder(categorical_features = [0])
teste = onehotencoder.fit_transform(teste).toarray()


df3 = df2 [:, 1]
print(df3)

df2['Lendo'] = e_dataframe1

e_dataframe = pd.DataFrame(teste)  
e_dataframe1 = e_dataframe.iloc[:, 5:6]

e_dataframe1.columns = ['Lendo']


cov = (df4.cov())
corr = (df2.corr())


df2.to_excel("dados//Atividade01//atividade_01_experimento_02_tratado02_correlacao.xlsx")

corr.to_excel("dados//Atividade01//atividade_01_experimento_02_tratado02_cov01.xlsx")


df2.corr().style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)
plt.show()