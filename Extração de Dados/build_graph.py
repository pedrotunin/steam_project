import os
import numpy as np

files = os.listdir("/home/ufabc/steam_project/Extração de Dados/api_responses(appids_new)/")
graph = np.zeros((10000, 10000), dtype=int)
dicionario = []

contador = 0
cont = 0
indicex = 0
indicey = 0

arq = open("/home/ufabc/steam_project/Extração de Dados/graph.txt", "w+")
arq_relaciona = open("/home/ufabc/steam_project/Extração de Dados/relationships.txt", "w+")

for i in range(500):
    read_arq = open("/home/ufabc/steam_project/Extração de Dados/api_responses(appids_new)/" + files[cont], "r+")
    read = []
    read = read_arq.readlines()
    
    for x in range(0, len(read) - 1):
        readx = read[x][:-1]
        
        if readx in dicionario:
            indicex = dicionario.index(readx)
        else:
            contador = contador + 1
            dicionario.append(readx)
            indicex = dicionario.index(readx)
        
        for y in range(x + 1, len(read)):
            ready = read[y][:-1]
            
            if ready in dicionario:
                indicey = dicionario.index(ready)
            else:
                contador = contador + 1
                dicionario.append(ready)
                indicey = dicionario.index(ready)
            
            graph[indicex][indicey] = graph[indicex][indicey] + 1

    read_arq.close()
    print(str(cont) + " = " + str(contador))
    cont = cont + 1

cont = 0
for i in dicionario:
    arq.write(str(dicionario[cont] + " "))
    cont = cont + 1

arq.write("\n")

for i in range(len(dicionario)):
    arq.write(str(dicionario[i]) + " ")	    
    for j in range(len(dicionario)):
        arq.write(str(graph[i][j]) + " ")
    arq.write("\n")

arq.close()

arq_relaciona.write(str(dicionario))
arq_relaciona.close()     
