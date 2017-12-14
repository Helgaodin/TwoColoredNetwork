N=256
f = open('text.txt')
Mat = np.zeros((N,N))
j=0
for line in f:#забрали матрицу
     l = line.split('\t')
     for i = 0..N:
        Mat[i][j] = l[i]
     j=j+1
