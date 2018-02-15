import pylab
import numpy as np
file = 'matrix1.txt'
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
#Связь black-white
print(upper_right_bw.max())#максимальная валентность
#будем видеть bw
bw_max = upper_right_bw.sum()#количество всех связей
 
pblack = np.zeros(int(bw_max+1)) 
for key in range(int(bw_max+1)):
    for row in upper_right_bw:#128 128
        #for elem in row:
        rowsum = row.sum()
        if( rowsum == key ):
            pblack[key]=pblack[key]+1

#pylab.plot(pblack)  

#будем видеть wb
pwhite = np.zeros(int(bw_max+1)) 
forhist =np.zeros(128)  
for key in range(int(bw_max+1)):
    for row in lower_left_wb:#128 128
        #for elem in row:
        rowsum = row.sum()
        if( rowsum == key ):
            pwhite[key]=pwhite[key]+1
