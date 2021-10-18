import entrada
l = []
for x in range(10):
    l.append(entrada.valida_inteiro('Digite um numero: ', 0, 20))
print(f'Soma: {sum(l)}')