def bubbleSort(vetor):
    for i in range(len(vetor)):
                for j in range(0, len(vetor)- i- 1):
                        
                    if vetor[j] > vetor[j+1]:  
                        temp = vetor[j]
                        vetor[j] = vetor[j+1]
                        vetor[j+1] = temp

exemplo = [0,5,3,10,1,14,13,6,4,23,15,9,24,7,16]

print(f'Criando antes do método',exemplo) #criado antes da ordenação

bubbleSort(exemplo)
print(f'Criado depois de passar pelo método',exemplo)