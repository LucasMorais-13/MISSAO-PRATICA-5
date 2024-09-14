texto_novo = open('texto.txt','a')

texto = list()
texto.append("Os projetos me auxiliam a aprender saindo da minha zona de conforto.\n")
texto.append("A vida tem dessas coisas, tipo fazer trabalho durante a madrugada.\n")
texto.append("Existe duas vida, uma antes do software e outra depois.")

texto_novo.writelines(texto)

texto_novo.close()