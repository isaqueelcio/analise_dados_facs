# -*- coding: utf-8 -*-

#importes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('dados//Atividade01//atividade_01_experimento_02_tratado02_tese005.xlsx', sheet_name='Planilha1')


df2 = df.iloc[:, 0:14]


cov = (df.cov())


corr = (df.corr('kendall'))

cov.to_excel("dados//Atividade01//atividade_01_experimento_02_tratado02_cov_teste.xlsx")


