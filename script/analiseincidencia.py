# -*- coding: utf-8 -*-

#importes
import pandas as pd
import numpy as np


#carregando dados

df = pd.read_excel('dados//Atividade01//atividade_01_experimento_01_tratados.xlsx', sheet_name='Planilha1')



a = df[(df.Categoria == "Procurando") & (df.engajamento == "engajamentoalto")]

a = df[(df.Categoria == "Lendo") & (df.desprezo == "desprezo") & (df.raiva== "raiva") &  (df.engajamento == "engajamentoalto") & 
       (df.valencia == "VN") & (df.tristeza == "tristeza")]