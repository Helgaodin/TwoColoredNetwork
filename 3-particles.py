# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:51:44 2018

@author: Olga
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:10:06 2017
@author: Olga
"""

#(1-2 + 3-4 + 5-6 -> 2-3 + 4-5 + 6-1)
import random as rn
import networkx as nx
import numpy as np
import math
import copy

Err = 0
t = 0
N = 256
p = 0.15
c = 0.5
mu = 0.5
Tmin = 2000000000
Nb = math.floor(c*N)#number of black 250
G = nx.erdos_renyi_graph(N, p) 
MatAdj = nx.to_numpy_matrix(G)#матрица смежности 256x256
dura = np.asarray(MatAdj)
MatAdj = copy.deepcopy(dura)
fileName = 'result'+str(mu)+'.txt'
fileMatrixName = 'matrix'+str(mu)+'.txt'

def NumberBW(Adj):
    #Adj = nx.to_numpy_matrix(G)#матрица смежности
    upper_half = np.hsplit(np.vsplit(Adj, 2)[0], 2)
    upper_right_bw = upper_half[1]#Nbw
    Nbw = np.sum(upper_right_bw)
    return Nbw

def NumberOfTriple(Adj):
    #Adj = nx.to_numpy_matrix(G)#матрица смежности
    upper_half = np.hsplit(np.vsplit(Adj, 2)[0], 2)
    lower_half = np.hsplit(np.vsplit(Adj, 2)[1], 2)
    upper_left_b = upper_half[0]#black
    #upper_right = upper_half[1]
    #lower_left = lower_half[0]
    lower_right_w = lower_half[1]#white   
    BB = np.dot(upper_left_b,upper_left_b)
    WW = np.dot(lower_right_w,lower_right_w)
    db=np.diagonal(BB) #black diag elements
    dw=np.diagonal(WW)#white diag elements
    Ntripleb = (np.sum(BB) - np.sum(db))/2.0
    Ntriplew = (np.sum(WW) - np.sum(dw))/2.0
    Ntriple = Ntripleb + Ntriplew
    #print("Ntrip = ", Ntriple, "Black = ", Ntripleb, "White = ", Ntriplew)
    return Ntriple

#Граф, итерация, ошибки, правильная матрица смежности
def SwitchEdges(G, tm, Err, Adj):
    G_old = copy.deepcopy(G)
    Adj_old = copy.deepcopy(Adj)
    Nbw_old = NumberBW(Adj)
    #Adj = nx.to_numpy_matrix(G)#матрица смежности
    NtripleOld = NumberOfTriple(Adj)
    K = G.edges() 
    noe = G.number_of_edges() 
    while True:
        a1 = rn.randint(0,noe-1)       
        a2 = rn.randint(0,noe-1)#случайное ребро возьмеь верно
        a3 = rn.randint(0,noe-1)#случайное ребро возьмеь верно
        A = K[a1][0]
        B = K[a1][1]
        C = K[a2][0]
        D = K[a2][1]#это просто числа
        E = K[a3][0]
        F = K[a3][1]
        if ((B != C) and (E != D) and (F != A)):
            break
    try:
        #print(A, B, C, D)
        Adj[A][B] = Adj[A][B]-1
        Adj[B][A] = Adj[A][B]
        if(Adj[A][B] == 0):
            G.remove_edge(A,B)
        Adj[C][D] = Adj[C][D]-1
        Adj[D][C] = Adj[C][D]
        if(Adj[C][D] == 0):
            G.remove_edge(C,D)
        Adj[E][F] = Adj[E][F]-1
        Adj[F][E] = Adj[E][F]
        if(Adj[E][F] == 0):
            G.remove_edge(E,F)
        #G.remove_edge(A,B)
        #G.remove_edge(C,D) 
        Adj[B][C] = Adj[B][C]+1
        Adj[C][B] = Adj[B][C]
        if(Adj[B][C] == 1):
            G.add_edge(B,C)
        Adj[E][D] = Adj[E][D]+1
        Adj[D][E] = Adj[E][D] 
        if(Adj[E][D] == 1):
            G.add_edge(E,D)
        Adj[A][F] = Adj[A][F]+1
        Adj[F][A] = Adj[A][F] 
        if(Adj[A][F] == 1):
            G.add_edge(A,F)
        #G.add_edge(A,C)
        #G.add_edge(B,D)
        NtripleNow = NumberOfTriple(Adj)
        if (NtripleNow > NtripleOld):
            #print(NtripleNow)
            tm= tm+1
            Nbw = NumberBW(Adj)
            return G, tm, NtripleNow, Nbw, Adj
        else:
            deltaN = NtripleOld - NtripleNow
            #print("dN = ", deltaN)
            if(rn.random() < math.exp(-mu*deltaN)):#accepted
                #print(NtripleNow)
                tm= tm+1
                Nbw = NumberBW(Adj)
                return G, tm, NtripleNow, Nbw, Adj
            else:
                #print(NtripleOld)
                Nbw = Nbw_old#NumberBW(G_old)
                return G_old, tm, NtripleOld, Nbw, Adj_old 
    except (nx.NetworkXError):
        Err = Err + 1
        Nbw = NumberBW(Adj)
        return G, tm, 0, Nbw, Adj
   
#MatAdj[225][1] = MatAdj[1][255]-1
while(t<Tmin):
    #print(t, Err)
    G, t, Ntrip, Nbw, MAdj = SwitchEdges(G, t, Err, MatAdj) 
    MatAdj = copy.deepcopy(MAdj)
    if (t%2000 == 0):
        print(t)
        f = open(fileName, 'a')
        text = str(t) + '\t' + str(Ntrip) +'\t'+ str(Nbw) + '\n'
        f.write(text)
        f.close()
        f = open(fileMatrixName,'w')
        for i in range (N):
            for j in range (N):
                f.write(str(MatAdj[i][j])+'\t')
            f.write('\n')
        f.close()