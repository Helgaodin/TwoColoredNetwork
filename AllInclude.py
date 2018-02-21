# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:10:06 2017
@author: Olga
"""
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
Tmin = 10000000
Nb = math.floor(c*N)#number of black 128
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
        aRan1 = rn.random()
        aRan2 = rn.random()
        if (aRan1 < 0.5):
            A = K[a1][0]
            B = K[a1][1]
        else:
            A = K[a1][1]
            B = K[a1][0]
        if (aRan2 < 0.5):
            C = K[a2][0]
            D = K[a2][1]#это просто числа
        else:
            C = K[a2][1]
            D = K[a2][0]#это просто числа
        if ((A != C) and (B != D)) and ((G.has_edge(A,C)==False) and (G.has_edge(B,D)==False)):
            break
    try:
        #print(A, B, C, D)
        Adj[A][B] = Adj[A][B]-1
        Adj[B][A] = Adj[A][B]
        G.remove_edge(A,B)
        Adj[C][D] = Adj[C][D]-1
        Adj[D][C] = Adj[C][D]
        G.remove_edge(C,D)
        #G.remove_edge(A,B)
        #G.remove_edge(C,D) 
        Adj[A][C] = Adj[A][C]+1
        Adj[C][A] = Adj[A][C]
        G.add_edge(A,C)
        Adj[B][D] = Adj[B][D]+1
        Adj[D][B] = Adj[B][D] 
        G.add_edge(B,D)
        #G.add_edge(A,C)
        #G.add_edge(B,D)
        NtripleNow = NumberOfTriple(Adj)
        tm= tm+1
        if (NtripleNow > NtripleOld):
            #print(NtripleNow)
            Nbw = NumberBW(Adj)
            return G, tm, NtripleNow, Nbw, Adj
        else:
            deltaN = NtripleOld - NtripleNow
            #print("dN = ", deltaN)
            if(rn.random() < math.exp(-mu*deltaN)):#accepted
                #print(NtripleNow)
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
        if(t%1000000):
            fileMil = '2mu'+str(mu)+'step'+str(t)+'.txt'
            f = open(fileMil,'w')
            for i in range (N):
                for j in range (N):
                    f.write(str(MatAdj[i][j])+'\t')
                f.write('\n')
            f.close()
