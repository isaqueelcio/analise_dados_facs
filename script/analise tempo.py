# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



#carregando dados

df = pd.read_excel('dados//ANALISE_DADOS_EMOCAO_tempo01.xlsx', sheet_name='Planilha1')
df1 = df


tempo = df1[(df1.ID_ATIVIDADE == 3) & (df1.ID_EXPERIMENTO == 3)]

a = tempo[(tempo.inicial > 0)]

tempo_adapta = a.iloc[:, 3:4].values

tempo_adapta.mean()

plt.figure(1,figsize=(6, 4))
plt.boxplot(tempo_adapta)


#agrupar tempo de cada experimento


tempogrupo = pd.DataFrame()

tempo_adapta.drop([0, 1])


tempo_adapta.columns = ['1-3']


tempogrupo['1-3'] = tempo_adapta['1-3']








