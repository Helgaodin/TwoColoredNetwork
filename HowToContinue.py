Nb = math.floor(c*N)#number of black 5

fileMatrixName = 'my3matrix'+str(mu)+'.txt'
fileName = 'my3result'+str(mu)+'.txt'
MatAdj = np.zeros((N,N))
Contk=0
for line in open(fileMatrixName):
    line = line.split('\t')
    for i in range(N):
        MatAdj[Contk][i] = float(line[i])
    Contk=Contk+1
             
    
last_line = None

for line in open(fileName, "r"):
    last_line = line
pop = last_line.split('\t')
t = float(pop[0])
#G = nx.erdos_renyi_graph(N, p) 
G = nx.Graph(MatAdj)
