# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 08:25:25 2017

@author: Olga
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:21:23 2017
@author: дмитрий
"""
import pylab
file = 'result0.3.txt'
x =[]
y1 =[]
y2 = []
k=0
for line in open(file):
    k=k+1
    line = line.split('\t')
    x.append(float(line[0]))
    y1.append(float(line[1]))#Тройка
    y2.append(float(line[2]))#Nbw
k
pylab.plot(x[1550:], y1[1550:])#triple
#pylab.plot(x, y2)#Nbw
print (y2[k-1])
print(y1[k-1])
pylab.show()