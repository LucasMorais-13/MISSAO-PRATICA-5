import time
import timeit

lista = list()

with open('documentos.txt','r',encoding='UTF-8') as arquivo:
    dados = arquivo.read()

linhas = dados.split()
for palavra in linhas:
    lista.append(palavra)

inicio_2 = timeit.default_timer()

vetor = lista
for i in range(len(vetor)):
    temp = i
    for j in range(i+1,len(vetor)):
        if vetor[temp] > vetor[j]:
            temp = j
    vetor[i],vetor[temp] = vetor[temp],vetor[i]
    #print(vetor)
print(f'Criado depois de passar pelo método \n ',vetor)

fim_2 = timeit.default_timer()
tempo_total_2 = fim_2 - inicio_2
print(f"Tempo de execução modo selection.sort: {tempo_total_2} segundos \n")

texto_novo = open('texto_novo.txt','a')

palavras_criad = list()
palavras_criad.extend(vetor)
texto_novo.writelines(palavras_criad)

texto_novo.close()

