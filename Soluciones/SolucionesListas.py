# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:33:37 2016

@author: roberto
"""

def moverElemento(matriz,xOri,yOri,xFin,yFin):
    
    aux=matriz[xFin][yFin]
    matriz[xFin][yFin]=matriz[xOri][yOri]
    matriz[xOri][yOri]=aux
    
    return matriz
    
def moverFila(matriz,filaOri,filaDest):
    aux=matriz[filaDest]
    matriz[filaDest]=matriz[filaOri]
    matriz[filaOri]=aux
    
    return matriz


def moverColumna(matriz,colOri,colDest):
    
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    
    aux=0

    for i in range(nFilas):
            aux=matriz[i][colDest]
            matriz[i][colDest]=matriz[i][colOri]
            matriz[i][colOri]=aux
            
    return matriz

def transponer(matriz):
    
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    
    aux=0
    

    for i in range(nFilas):
        for j in range(nColumnas):
            if(i>j):
                aux1=matriz[i][j]
                matriz[i][j]=matriz[j][i]
                matriz[j][i]=aux
    
    return matriz
    
def sumarMatrices(matriz1,matriz2):

    if(len(matriz1) != len(matriz2) and len(matriz1[0]) != len(matriz2[0])):
        print "No se pueden sumar matrices que no tienen la misma dimension"
        return 
        
    
    for i in range(len(matriz1)):
        for j in range(len(matriz[0])):
            matriz1[i][j]+=matriz2[i][j]
    return matriz1
    
#Funcion Boss
def multiplicarMatrices(matriz1,matriz2):
    matrizFinal=[]
    filaAuxiliar=[]
    
    
    for x in range(len(matriz1)):
     
        for i in range(len(matriz1)):
               aux=0
               for j in range(len(matriz1[0])):
                aux+=matriz1[x][j]*matriz2[j][i]
               filaAuxiliar.append(aux)
   
        matrizFinal.append(filaAuxiliar)
        filaAuxiliar=[]
                
    return matrizFinal
    

matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
matriz2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]
        
#print moverElemento(matriz,0,0,1,1)
#print moverElemento(matriz2,0,0,1,1)
#print moverFila(matriz,1,2)
#print moverFila(matriz2,1,2)
#print moverColumna(matriz,1,2)
#print moverColumna(matriz2,1,2)
#print transponer(matriz)
#print transponer(matriz2)
#print sumarMatrices(matriz,matriz)
#print multiplicarMatrices(matriz,matriz)
        

        
        