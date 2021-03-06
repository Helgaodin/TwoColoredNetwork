# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:10:06 2017

@author: Olga
"""
import random as rn
import networkx as nx
import math
import copy

N = 500
p = 0.15
c = 0.5
mu = 0.5

Nb = math.floor(c*N)#number of black
G = nx.erdos_renyi_graph(N, p) 

def NumberOfTriple(G):
    Ntripleb = 0
    for i in range(Nb):#0..Nb-1
        for j in range(i+1,Nb) :
            if(G.number_of_edges(i,j) != 0):
                for k in range(j+1,Nb):
                    if((G.number_of_edges(i,k)!=0) and (G.number_of_edges(j,k)!=0)):
                        Ntripleb = Ntripleb+1
    Ntriplew = 0         
    for i in range(Nb,N):
        for j in range(i+1,N) :
            if(G.number_of_edges(i,j) != 0):
                for k in range(j+1,N):
                    if(G.number_of_edges(i,k)!=0) and (G.number_of_edges(j,k)!=0):
                        Ntriplew = Ntriplew+1  
    Ntriple = Ntripleb + Ntriplew 
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
