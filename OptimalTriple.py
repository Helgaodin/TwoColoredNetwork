# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:40:47 2017

@author: дмитрий
"""

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

N = 500
p = 0.15
c = 0.5
mu = 0.5

Nb = math.floor(c*N)#number of black 250
G = nx.erdos_renyi_graph(N, p) 


def NumberOfTriple(G):
    Adj = nx.to_numpy_matrix(G)#матрица смежности
    upper_half = np.hsplit(np.vsplit(Adj, 2)[0], 2)
    lower_half = np.hsplit(np.vsplit(Adj, 2)[1], 2)
    upper_left_b = upper_half[0]#black
    #upper_right = upper_half[1]
    #lower_left = lower_half[0]
    lower_right_w = lower_half[1]#white
    
    BB = np.dot(upper_left_b,upper_left_b)
    WW = np.dot(lower_right_w,lower_right_w)
    
    db=np.diagonal(BB) #black
    dw=np.diagonal(WW)#white
    Ntripleb = (np.sum(BB) - np.sum(db))/2.0
    Ntriplew = (np.sum(WW) - np.sum(dw))/2.0
    Ntriple = Ntripleb + Ntriplew
    print("Ntrip = ", Ntriple, "Black = ", Ntripleb, "White = ", Ntriplew)
    return Ntriple

def SwitchEdges(G):
    G_old = copy.deepcopy(G)
    NtripleOld = NumberOfTriple(G)
    K = G.edges() 
    noe = G.number_of_edges() 
    a1 = rn.randint(0,noe)       
    a2 = rn.randint(0,noe)
    A = K[a1][0]
    B = K[a1][1]
    C = K[a2][0]
    D = K[a2][1]
    G.remove_edge(A,B)
    G.remove_edge(C,D) 
    G.add_edge(A,C)
    G.add_edge(B,D)
    NtripleNow = NumberOfTriple(G)
    if (NtripleNow > NtripleOld):
        print(NtripleNow)
        return G
    else:
        deltaN = NtripleOld - NtripleNow
        print("dN = ", deltaN)
        if(rn.random() < math.exp(-mu*deltaN)):#accepted
            print(NtripleNow)
            return G
        else:
            print(NtripleOld)
            return G_old
    
for i in range(5000):
    print(i)
    G = SwitchEdges(G) 

nx.draw_networkx(G, with_labels=True)   
