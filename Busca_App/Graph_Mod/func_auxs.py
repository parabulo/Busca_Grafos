import numpy as np
import random as rd

# Rotina sucessores para Grade de Ocupação
def sucessores(atual,mapa,dim_x,dim_y):
    f = []
    x = atual[0]
    y = atual[1]
    
    if y+1!=dim_y:
        if mapa[x][y+1]==0:
            linha = []
            linha.append(x)
            linha.append(y+1)
            f.append(linha)
            
    if x+1!=dim_x:
        if mapa[x+1][y]==0:
            linha = []
            linha.append(x+1)
            linha.append(y)
            f.append(linha)
    
    if x-1>=0:
        if mapa[x-1][y]==0:
            linha = []
            linha.append(x-1)
            linha.append(y)
            f.append(linha)
    
    if y-1>=0:
        if mapa[x][y-1]==0:
            linha = []
            linha.append(x)
            linha.append(y-1)
            f.append(linha)
    return f

# Carrega Grafo para Lista de Adjacência e Lista de Nós
def Gera_Problema_Grafo(arquivo):
    f = open(arquivo,"r")
    
    i=0
    nos = []
    grafo = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i==0:
            nos = str1
        else:
            grafo.append(str1)
        i += 1       
    
    return nos, grafo

def Gera_Problema_Grade(arquivo):
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        mapa.append(str1)
    
    return mapa


def Gera_Problema_Grade1(n,m,qt_ob):
    
    mapa = np.zeros((n,m),int)
    
    k = 0
    while k<qt_ob:
        i = rd.randrange(0,n)
        j = rd.randrange(0,m)
        if mapa[i][j]!=2:
            mapa[i][j] = 2
            k += 1
    
    return mapa