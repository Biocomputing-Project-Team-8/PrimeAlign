#algorithm based on https://www.biostars.org/p/231391/
import numpy as np
from string import *


def diagonal(num1,num2,match,sub):
    if num1 == num2:
        return match
    else:
        return sub


def align(a ,b , mat):
    lista = " "
    listb = " "
    x = len(b)
    y = len(a)
    while x != 0 or y != 0:
        d = mat[x - 1][y - 1]
        h = mat[x - 1][y]
        v = mat[x][y - 1]
        if d >= h and d >= v:

            x -= 1
            y -= 1
            lista = a[y] + lista
            listb = b[x] + listb
        elif h > d and h > v:

            x -= 1
            lista = a[y] + lista
            listb = '_' + listb
        elif v > d and v > h:

            y -= 1
            lista = '_' + lista
            listb = b[x] + listb
    print(lista)
    print(listb)


def nw(a, b, match, sub, indel):
    y = len(a) + 1
    x = len(b) + 1
    almat = np.zeros((x,y),dtype = int)
   # pmat = np.zeros((x,y),dtype = str)
    for i in range(0,x):
        almat[i][0] = indel * i
    #    pmat[i][0] = 'V'
    for j in range(0,y):
        almat[0][j] = indel * j
    for i in range(1,x):
        for j in range(1,y):
            d = almat[i-1][j-1] + diagonal(a[j-1],b[i-1], match, sub)
            h = almat[i-1][j] + indel
            v = almat[i][j-1] + indel
            almat[i][j]=max(d,h,v)
    print (np.matrix(almat))
    return almat


seq1 = "ACGGTA"
seq2 = "AAGTA"
mat = nw(seq1, seq2, 3, -2, -2)
align(seq1, seq2, mat)