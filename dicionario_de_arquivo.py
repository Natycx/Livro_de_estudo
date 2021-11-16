dicionario = {}
with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras = linha.split(' ')
        for i in palavras:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
print(dicionario)