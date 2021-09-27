def calculo_media():
    notas = [6, 7, 5, 8, 9]
    soma = 0
    x = 0
    while x < 5:
        soma = soma + notas[x]
        x = x + 1
    print(f'Média: {soma / x:5.2f}')


def media():
    notas = [0]*7
    soma = 0
    x = 0
    while x < 5:
        notas[x] = float(input(f'Nota {x}: '))
        soma += notas[x]
        x += 1
    x = 0
    while x < 5:
        print(f'Nota {x}: {notas[x]:6.2f}')
        x += 1
    print(f'Média: {soma / x:5.2f}')


def apresentacao_numero():
    numero = [0]*5
    x = 0
    while x < 5:
        numero[x] = int(input(f'Numero {x + 1}: '))
        x += 1
    while True:
        escolhido = int(input('Qual a posição você quer imprimir (0 para sair): '))
        if escolhido == 0:
            break
        print(f'Você escolheu o número: {numero[escolhido - 1]}')


def listas():
    l = [1, 2, 3, 4]
    m = [4, 3, 7, 8]
    v = l + m
    print(v)
    lista = []
    i = 0
    for i in range(len(l)):
        if l[i] not in lista:
            lista.append(l[i])
        if m[i] not in lista:
            lista.append(m[i])
    print(lista)


def fila_banco():
    ultimo = 10
    fila = list(range(1, ultimo + 1))
    while True:
        print(f'\nExistem {len(fila)} clientes na fila')
        print(f'Fila atual: {fila}')
        print('Digite F para adicionar um cliente ao fim da fila,')
        print('ou A para realizar o atendimento. S para sair')
        operacao = input('Operação (F, A ou S) ')
        if operacao == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} antendido')
            else:
                print('Fila vazia! Ninguém para atender.')
        elif operacao == 'F':
            ultimo += 1  # incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao == 'S':
            break
        else:
            print('Operação invalida! Digite F, A ou S!')


def fila_banco1():
    ultimo = 10
    ultimo2 = 10
    fila1 = list(range(1, ultimo + 1))
    fila2 = list(range(1, ultimo2 + 1))
    while True:
        print(f'\nExistem {len(fila1)} clientes na fila 1')
        print(f'Fila atual: {fila1}')
        print(f'\nExistem {len(fila2)} clientes na fila 2')
        print(f'Fila atual: {fila2}')
        print('\nDigite A para o atendimento na fila 1\n'
              'Digite F para adicionar um cliente ao fim da fila,')
        print('ou A para realizar o atendimento.')
        print('Digite B para o atendimento na fila 2\n'
              'Digite G para adicionar um cliente ao fim da fila,')
        print('ou A para realizar o atendimento. S para sair')

        operacao = input('Operação (A, B, F, G, A ou S) ')
        operacao.split()
        fila1_contagem = operacao.count('A')
        fila2_contagem = operacao.count('B')
        contagem = operacao.count('F')
        contagem_fila2 = operacao.count('G')
        contagem2 = operacao.count('A')
        contagem3 = operacao.count('S')
        print(contagem3, contagem, contagem2)
        if fila1_contagem != 0:
            while contagem > 0:
                if len(fila1) > 0:
                    atendido = fila1.pop(0)
                    print(f'Cliente {atendido} antendido')
                else:
                    print('Fila vazia! Ninguém para atender.')
                contagem = contagem - 1
            while contagem2 > 0:
                ultimo += 1  # incrementa o ticket do novo cliente
                fila1.append(ultimo)
                contagem2 = contagem2 - 1
            if contagem3 != 0:
                break
            elif contagem == 0 and contagem2 == 0 and contagem3 == 0:
                print('Operação invalida! Digite F, A ou S!')
        if fila2_contagem != 0:
            while contagem_fila2 > 0:
                if len(fila1) > 0:
                    atendido = fila1.pop(0)
                    print(f'Cliente {atendido} antendido')
                else:
                    print('Fila vazia! Ninguém para atender.')
                contagem_fila2 = contagem_fila2 - 1
            while contagem2 > 0:
                ultimo += 1  # incrementa o ticket do novo cliente
                fila1.append(ultimo)
                contagem2 = contagem2 - 1
            if contagem3 != 0:
                break
            elif contagem == 0 and contagem2 == 0 and contagem3 == 0:
                print('Operação invalida! Digite F, A ou S!')


def pilha_de_pratos():
    prato = 5
    pilha = list(range(1, prato + 1))
    while True:
        print(f'\nExistem {len(pilha)} pratos na pilha')
        print(f'Pilha atual: {pilha}')
        print('Digite E para empulhar um novo prato,')
        print(f'ou D para desempilhar. S para sair')
        operacao = input(f'Operação(E, D ou S)')
        if operacao == 'D':
            if len(pilha) > 0:
                lavado = pilha.pop(-1)
                print(f'Prato {lavado} lavado')
            else: print('Pilha vazia')
        elif operacao == 'E':
            prato += 1  # Novo prato
            pilha.append(prato)
        elif operacao == 'S': break
        else: print('Operação invalida! Digite apenas E, D ou S!')
        



def main():
    pilha_de_pratos()


if __name__ == '__main__':
    main()
