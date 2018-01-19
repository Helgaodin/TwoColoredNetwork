# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:03:35 2018

@author: Olga
"""


import pylab
import numpy as np
file = 'matrix0.5.txt'
Mat = np.zeros((256,256))
k=0
for line in open(file):
    line = line.split('\t')
    for i in range(256):
        Mat[k][i] = float(line[i])
    k=k+1
print(k)
upper_half = np.hsplit(np.vsplit(Mat, 2)[0], 2)
lower_half = np.hsplit(np.vsplit(Mat, 2)[1], 2)
upper_left_bb = upper_half[0]#black-black
upper_right_bw = upper_half[1]#black-white
lower_left_wb = lower_half[0]#white-black
lower_right_ww = lower_half[1]#white-white

#########################################################

#Распределение bw по вершинам
#black-white
print(upper_right_bw.max())
bw_max = upper_right_bw.sum() 
pblack = np.zeros(int(bw_max+1)) 
for key in range(int(bw_max+1)):
    for row in upper_right_bw:#128 128
        #for elem in row:
        rowsum = row.sum()
        if( rowsum == key ):
            pblack[key]=pblack[key]+1

#pylab.plot(pblack)  
pwhite = np.zeros(int(bw_max+1)) 
forhist =np.zeros(128)  
for key in range(int(bw_max+1)):
    for row in lower_left_wb:#128 128
        #for elem in row:
        rowsum = row.sum()
        if( rowsum == key ):
            pwhite[key]=pwhite[key]+1

#ip=0                 
#for row in lower_left_wb:#128 128
#    #for elem in row:
#    rowsum = row.sum()
#    forhist[ip] = rowsum
#    ip = ip + 1
#pylab.plot(pwhite)
#pylab.hist(forhist)      
###############################################################

#Распределение общей валентности у вершин куда приходит bw
#Рассматриваем только связанные с bw вершины и смотрим их валентность

#black#  0-127    
i=0
massivblack=[]#пустой список
for row in upper_right_bw:
    if (row.sum()!=0):
        massivblack.append(i)
    i=i+1
black = []
for key in massivblack:
    bl = upper_right_bw[key].sum() + upper_left_bb[key].sum()
    black.append(bl)    
#white#  128-255 
i=128
massivwhite=[]#пустой список
for row in lower_left_wb:
    if (row.sum()!=0):
        massivwhite.append(i)
    i=i+1  
white = []
for key in massivwhite:
    wh = lower_right_ww[key-128].sum() + lower_left_wb[key-128].sum()
    white.append(wh)
                      