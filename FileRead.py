# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:21:23 2017

@author: дмитрий
"""
import pylab
file = 'result.txt'
x =[]
y =[]
k=0
for line in open(file):
    k=k+1
    line = line.split('\t')
    x.append(float(line[0]))
    y.append(float(line[1]))
k
pylab.plot(x, y)
pylab.show()
