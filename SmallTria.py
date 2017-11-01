#вспомогательный файл для подсчета триплетов оптимальным способом на маленьком графе
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:18:07 2017

@author: дмитрий
"""

import networkx as nx
import numpy as np

e = [(1,2), (1,4), (1,5), (2,3), (2,4), (3,5), (4,5)]  # list of edges
G = nx.Graph(e)
N=6
Adj = nx.to_numpy_matrix(G)
B = np.linalg.matrix_power(Adj, 2)
C=np.dot(Adj,Adj)
d=np.diagonal(C)
bubl1 = np.sum(B) - np.sum(d)

nx.triangles(C)

#wtf = np.vsplit(Adj, 5)
#hsplit Split an array into multiple sub-arrays horizontally (column-wise).
#vsplit Split an array into multiple sub-arrays vertically (row-wise).
#upper_half = np.hsplit(np.vsplit(Adj, 2)[0], 2)


#print("Nt =", Nt, "Ntrip =", Ntriple/3.0)

#upper_half = np.hsplit(np.vsplit(my_matrix, 2)[0], 2)
#lower_half = np.hsplit(np.vsplit(my_matrix, 2)[1], 2)
#
#upper_left = upper_half[0]
#upper_right = upper_half[1]
#lower_left = lower_half[0]
#lower_right = lower_half[1]
