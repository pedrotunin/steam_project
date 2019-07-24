import os
import numpy as np

files = os.listdir("/home/tunin/projeto_cr/Extração de Dados/api_responses(appids_new)/")
graph = np.zeros((8300, 8300), dtype=int)
dicionario = []

cont = 0
indicex = 0
indicey = 0

arq = open("/home/tunin/projeto_cr/Extração de Dados/graph.txt", "w+")
arq_relaciona = open("/home/tunin/projeto_cr/Extração de Dados/relationships.txt", "w+")

for i in range(500):
    read_arq = open("/home/tunin/projeto_cr/Extração de Dados/api_responses(appids_new)/" + files[cont], "r+")
    read = []
    read = read_arq.readlines()
    
    for x in range(0, len(read) - 1):
        readx = read[x][:-1]
        
        if readx in dicionario:
            indicex = dicionario.index(readx)
        else:
            dicionario.append(readx)
            indicex = dicionario.index(readx)
        
        for y in range(x + 1, len(read)):
            ready = read[y][:-1]
            
            if ready in dicionario:
                indicey = dicionario.index(ready)
            else:
                dicionario.append(ready)
                indicey = dicionario.index(ready)
            
            graph[indicex][indicey] = graph[indicex][indicey] + 1

    read_arq.close()
    cont = cont + 1

for i in range(8300):
    for j in range(8300):
        arq.write(str(graph[i][j]) + " ")
    arq.write("\n")

arq.close()

arq_relaciona.write(str(dicionario))
arq_relaciona.close()
        
