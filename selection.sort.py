vetor = [0,5,3,10,1,14,13,6,4,23,15,9,24,7,16]
print(f'Criando antes do método',vetor) #criado antes da ordenação

for i in range(len(vetor)):
    temp = i
    for j in range(i+1,len(vetor)):
        if vetor[temp] > vetor[j]:
            temp = j
    vetor[i],vetor[temp] = vetor[temp],vetor[i]
    #print(vetor)
print(f'Criado depois de passar pelo método',vetor)