# -*- coding: utf-8 -*-

#importes
import pandas as pd
import numpy as np


#carregando dados

df = pd.read_excel('dados//Atividade02//atividade_02_experimento_01_tratados.xlsx', sheet_name='Planilha1')
df1 = df

df1 = df.loc[df['Alegria'] == 0]

df['Alegria']

df1 = df.loc[df['Alegria'] == 0 , "Alegria" ] =  2

df.loc[df['Alegria'] == 0]

df1.loc[df1['Alegria'] > 0, "Alegria"] = 'Alegria'
df1.loc[df1['tristeza'] > 0, "tristeza"] = 'tristeza'
df1.loc[df1['desgosto'] > 0, "desgosto"] = 'desgosto'
df1.loc[df1['desprezo'] > 0, "desprezo"] = 'desprezo'
df1.loc[df1['raiva'] > 0, "raiva"] = 'raiva'
df1.loc[df1['medo'] > 0, "medo"] = 'medo'
df1.loc[df1['surpresa'] > 0, "surpresa"] = 'surpresa'


df1.loc[df1['valencia'] < 0, "valencia"] = -100
df1.loc[df1['valencia'] > 0, "valencia"] = 200

df1.loc[df1['valencia'] == -100, "valencia"] = "VN"
df1.loc[df1['valencia'] == 200, "valencia"] = "VP"

df1.loc[df1['engajamento'] <= 30, "engajamento"] = -25
df1.loc[df1['engajamento'] > 30, "engajamento"] = 50


df1.loc[df1['engajamento'] == -25, "engajamento"] = "engajamentobaixo"
df1.loc[df1['engajamento'] == 50, "engajamento"] = "engajamentoalto"

'''



df1.loc[df1['engajamento'] > 0, "engajamento"] = 'engajamento'

df1.loc[df1['engajamento'] <= 30, "engajamento"] = 25
df1.loc[df1['engajamento'] > 30, "engajamento"] = 50

'''

#******************
'''

df1.loc[df1['valencia'] == 'NaN', "valencia"] = 50



df.loc[(df["B"] > 50) & (df["C"] == 900), "A"] *= 1000


df1[(df1.valencia > 0)], 'valencia' = 100


df1['valencia'] = np.where(df1['valencia'] >=0 , 'yes', 'no')


df['valencia'] = ['VN' if x == 200 elif x == 100 'VP' for x in df['valencia']]

'''

#Não usado
'''
for x in df['valencia']:
x = 0   
for i in range(0 , 3522): 
   x = df['valencia'][1]         
   if(x > 0):
       print("Maior que zero", x)
       print("valor i", i)
       df['valencia'][6] = "VN"
   else:
       print("Menor que zero", x)
       df['valencia'][i] = "VP"
       print("valor i", i)


'''






a = df1[(df1.Categoria == "busca") & (df1.desgosto == "desgosto")]

################## Categoria
df1.loc[df1['Categoria'] == 1, "Categoria"] = "busca"
df1.loc[df1['Categoria'] == 2, "Categoria"] = "Carregando"
df1.loc[df1['Categoria'] == 3, "Categoria"] = "Procurando"
df1.loc[df1['Categoria'] == 4, "Categoria"] = "Encontrou"
df1.loc[df1['Categoria'] == 5, "Categoria"] = "Lendo"
df1.loc[df1['Categoria'] == 6, "Categoria"] = "Login"
df1.loc[df1['Categoria'] == 7, "Categoria"] = "Escrevendo"
df1.loc[df1['Categoria'] == 8, "Categoria"] = "Buscaproduto"
df1.loc[df1['Categoria'] == 9, "Categoria"] = "Escolhendoproduto"



#seprarção dados emoções
emocoes = df1.iloc[:, 1:8]
emocoes = df1.iloc[:, 1:7].values

#separação dados Dominios 
dominios = df1.iloc[:, 8:10]
dominios = df1.iloc[:, 1:7].values

#Dominios e emoções
dominiosemocaoes = df1.iloc[:, 0:11]


# Exportando dados
'''
df1.to_excel("dados//Atividade01//atividade_01_experimento_02_tratado.xlsx")
df1.to_csv("dados//Atividade01//atividade_01_experimento_02_tratado.csv")

emocoes.to_csv("dados//Atividade01//atividade_01_experimento_02_emocoes.csv")
dominios.to_csv("dados//Atividade01//atividade_01_experimento_02_dominios.csv")


dominiosemocaoes.to_csv("dados//Atividade01//atividade_01_experimento_02_dominiosemocaoes.csv")

'''
''' 
df1.loc[((df1["valencia"] > 0) or (df1["valencia"] < 0)), "valencia"] = "valencia"
df1.loc[((df1["valencia"] > 0) or (df1["valencia"] < 0)), "valencia"] = "valencia"

''' 
dominiosemocaoes.to_excel("dados//Atividade03//atividade_03_experimento_03_tratados.xlsx")
#****  converter em lista ***
transacoes = []
for i in range(0, len(dominiosemocaoes)):
    transacoes.append([str(dominiosemocaoes.values[i,j]) for j in range(0, 10)])
    
#transacoes = list(map(int, transacoes))
# Valencia positiva e negativa
'''    
for i in range(0, 3522):
         j = 8
         
         if(transacoes[i][j] > 0):
             print("Positiva #####", transacoes[i][j])
             print("i", i)
             print("j",j)
             #del transacoes[i][j]
             
         
         else:
             print("Negativa ****", transacoes[i][j])
             print("i", i)
             print("j",j)
    
    '''

# ***** deletar elementos vazio

for i in range(0, len(transacoes)):
    for j in reversed (range(0, 10)):
         
         if(transacoes[i][j] == 'nan'):
             print("dados #####", transacoes[i][j])
             print("i", i)
             print("j",j)
             del transacoes[i][j]
             
         
         else:
             print("dados ****", transacoes[i][j])
             print("i", i)
             print("j",j)
    
# **** Deletar listas vazias **
vazio = 0
registros = 0
for i in reversed(range(0, len(transacoes))):
    if len(transacoes[i]) == 0 :
        print("Vazio", transacoes[i])
        vazio = vazio + 1
        del transacoes[i]
    else:
        print("Emoção", transacoes[i])
        registros = registros + 1
        
        
##Eliminar atividade sem emoção
atividade = 0
registros = 0
for i in reversed(range(0, len(transacoes))):
    for j in range(0, len(transacoes[i])):
    
        if ((len(transacoes[i]) == 1) and ((transacoes[i][j] == 'busca') or
             (transacoes[i][j] == 'Carregando') or 
             (transacoes[i][j] == 'Procurando') or
             (transacoes[i][j] == 'Encontrou') or
             (transacoes[i][j] == 'Lendo') or
             (transacoes[i][j] == 'Login') or
             (transacoes[i][j] == 'Escrevendo') or
             (transacoes[i][j] == 'Buscaproduto') or
             (transacoes[i][j] == 'Escolhendoproduto'))):
            print("Len 1", transacoes[i])
            atividade = atividade + 1
            del transacoes[i]
        else:
            print("Emoção", transacoes[i])
            registros = registros + 1


 
        
 '''            
del transacoes[0][0]
len(transacoes[1])
transacoes.remove("engajamento") 

for a in reversed (range(0, 9)):
        print("teste", a)
transacoes.append([str(pd.isnull(dominiosemocaoes.values[i,j]) for j in range(0, 9)])
 
A= []
del(A[0])
'''    
        

from apyori import apriori

regras = apriori(transacoes, min_support = 0.06 , min_confidence = 0.06, min_lift = 1, min_length = 5)

resultados = list(regras)
resultados

Results2 = [list(x) for x in resultados]

Res = []
for j in range(0, len(resultados)):

   Res.append([list(x) for x in Results2[j][2]])
    
Res

for j in range(0, len(resultados)):
    print("Regra --", j)
    print(Res[j])
    
    
    
 
    
#Busca nas regras
busca = []
Carregando = []
Procurando = []
Encontrou = []
Lendo = []
Login = []
Escrevendo = []
Buscaproduto = []
Escolhendoproduto = []

for j in range(0, len(resultados)):
    regra = str(Res[j])
    
    if('busca' in regra):
        print("busca --Regra -", j)
        busca.append(j)
       
        #busca = busca + 1
        
    elif('Carregando' in regra):
        print("Carregando --Regra -", j)
        Carregando.append(j)
        #Carregando = Carregando + 1
        
    elif('Procurando' in regra):
        print("Procurando --Regra -", j)
        Procurando.append(j)
        #Procurando = Procurando + 1
        
    elif('Encontrou' in regra):
        print("Encontrou --Regra -", j)
        Encontrou.append(j)
        Encontrou = Encontrou + 1
        
    elif('Lendo' in regra):
        print("Lendo --Regra -", j)
        Lendo.append(j)
        Lendo.append(j)
        #Lendo = Lendo + 1
        
    elif('Login' in regra):
        print("Login --Regra -", j)
        Login.append(j)
        #Login = Login + 1
        
    elif('Escrevendo' in regra):
        print("Escrevendo --Regra -", j)
        Escrevendo.append(j)
        #Escrevendo = Escrevendo + 1
        
    elif('Buscaproduto' in regra):
        print("Buscaproduto --Regra -", j)
        Buscaproduto.append(j)
        #Buscaproduto = Buscaproduto + 1
        
    elif('Escolhendoproduto' in regra):
        print("Escolhendoproduto --Regra -", j)
        Escolhendoproduto.append(j)
        #Escolhendoproduto = Escolhendoproduto + 1
    else:
        print("Não encontrou Regra -", j)
        
print("Regras --busca ", busca)
print("Regras --Carregando ", Carregando)
print("Regras -- Procurando", Procurando)
print("Regras -- Encontrou", Encontrou) 
print("Regras --Lendo ", Lendo)
print("Regras --Login ", Login)
print("Regras --Escrevendo", Escrevendo)
print("Regras --Escolhendoproduto", Escolhendoproduto)
   
#####
busca = []
Carregando = []
Procurando = []
Encontrou = []
Lendo = []
Login = []
Escrevendo = []
Buscaproduto = []
Escolhendoproduto = []

for j in range(0, len(resultados)):
    regra = str(Res[j])
    
    if('busca' in regra):
        print("busca --Regra -", j)
        busca.append(j)
        print(Res[j])
        #busca = busca + 1
        
    elif('Carregando' in regra):
        print("Carregando --Regra -", j)
        Carregando.append(j)
        print(Res[j])
        #Carregando = Carregando + 1
        
    elif('Procurando' in regra):
        print("Procurando --Regra -", j)
        Procurando.append(j)
        print(Res[j])
        #Procurando = Procurando + 1
        
    elif('Encontrou' in regra):
        print("Encontrou --Regra -", j)
        Encontrou.append(j)
        #Encontrou = Encontrou + 1
        print(Res[j])
        
    elif('Lendo' in regra):
        print("Lendo --Regra -", j)
        Lendo.append(j)
        print(Res[j])
        #Lendo = Lendo + 1
        
    elif('Login' in regra):
        print("Login --Regra -", j)
        Login.append(j)
        #Login = Login + 1
        print(Res[j])
        
    elif('Escrevendo' in regra):
        print("Escrevendo --Regra -", j)
        Escrevendo.append(j)
        print(Res[j])
        #Escrevendo = Escrevendo + 1
        
    elif('Buscaproduto' in regra):
        print("Buscaproduto --Regra -", j)
        Buscaproduto.append(j)
        print(Res[j])
        #Buscaproduto = Buscaproduto + 1
        
    elif('Escolhendoproduto' in regra):
        print("Escolhendoproduto --Regra -", j)
        Escolhendoproduto.append(j)
        print(Res[j])
        #Escolhendoproduto = Escolhendoproduto + 1
    else:
        print("Não encontrou Regra -", j)
   
   
        
        
Res[0][0][1] == "desprezo"  
len(Res[58][5])       


Res[58][0] 
        
        aqui
        
nome = str( Res[58])
Nome = "[[frozenset(), frozenset({'Lendo'}), 0.45920889987639063, 1.0]]"


if('desprezo' in nome):
    print("Encontrou ")
else:
    print("não encontrou")


        
        
   
        if(Res == "Lendo"):
            print("Regra --", j)
            print(Res[j])
        else:
            print("nada")
    
Res[11][1][3] == "desprezo"  
len(Res[58][5]) 
    
lista = ["teste", "outro", "mais", "um", "teste"]
print len([x for x in lista if x=="teste"]))
    
print("fdg", len(lista))




###############################
len(transacoes[i])
    
cont = 0    
for i in range(0, 1618):
    for j in range(0, len(transacoes[i])):
         
         if(transacoes[i][j] == "engajamento"):
             print("dados #####", transacoes[i][j])
             print("i", i)
             print("j",j)
             cont = cont + 1
             
         
         else:
             print("dados ****", transacoes[i][j])
             print("i", i)
             print("j",j)
             
print("Cont", cont)

#############################

engajamento = df1.loc[(df1["engajamento"] >= 50)]
len(engajamento)

valencia = df1.loc[(df1["valencia"] > 50)]
len(valencia)

######################

a = df1[(df1.Categoria == "busca") & (df1.desgosto == "desgosto")]






