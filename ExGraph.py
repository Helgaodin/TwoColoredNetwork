import networkx as nx
e = [(1, 2), (1,4), (1,5), (2, 3), (2,4), (3, 5), (4,5)]  # list of edges
G = nx.Graph(e)

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:18:07 2017

@author: дмитрий
"""

import networkx as nx


e = [(1,2), (1,4), (1,5), (2,3), (2,4), (3,5), (4,5)]  # list of edges
G = nx.Graph(e)
N=6
Ntripleb = 0
for i in range(1,N):#0..Nb-1
    for j in range(i+1,N):
            if(G.number_of_edges(i,j) != 0):
                for k in range(j+1,N):
                    if((G.number_of_edges(i,k)!=0) and (G.number_of_edges(j,k)!=0)):
                        Ntripleb = Ntripleb+1
print("numOfEdgTri = ", Ntripleb)

Ntriple = 0
Nt = 0
for i in range(1,N):#0..Nb-1
    for j in range(i+1,N):
            if(G.number_of_edges(i,j) != 0):
                for k in range(1,N):
                    if((k!=i) and (k!=j)):
                        if((G.number_of_edges(i,k)!=0) and (G.number_of_edges(j,k)!=0)):
                            Ntriple = Ntriple+1#закрытый
                        else:
                            if((G.number_of_edges(i,k)!=0) or (G.number_of_edges(j,k)!=0)):
                                Nt = Nt+1#открытые
                                print("i = ", i, "j = ", j, "k = ",k)
print("Nt =", Nt/2.0, "Ntrip =", Ntriple/3.0)
