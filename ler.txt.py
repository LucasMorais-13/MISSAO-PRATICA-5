texto = open('loremipsum.txt','r')
print(texto.read(),"\n")
texto.seek(0)
print(f"Os três primeiros caracteres são: {texto.readline(3)}","\n")
texto.close()
with open('loremipsum.txt','r') as arquivo:
    dados = arquivo.read()
    print(dados,"\n")
arquivo.close()