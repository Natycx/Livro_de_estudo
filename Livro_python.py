import random
import sys
import types
import math


def calculo_media():
    notas = [6, 7, 5, 8, 9]
    soma = 0
    x = 0
    while x < 5:
        soma += notas[x]
        x = x + 1
    print(f'Média: {soma / x:5.2f}')


def media():
    notas = [0] * 7
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
    numero = [0] * 5
    x = 0
    while x < 5:
        numero[x] = int(input(f'Numero {x + 1}: '))
        x += 1
    while True:
        escolhido = int(input('Qual a posição você quer imprimir (0 para sair): '))
        if escolhido == 0:
            break
        print(f'Você escolheu o número: {numero[escolhido - 1]}')


def adicao_de_elementos():
    l = []
    while True:  # Não pode ser transformado em for pois n sabemos o numero de elementos a ser inserido no l
        n = int(input("Digite um numero (0 sai): "))
        if n == 0:
            break
        l.append(n)
    for i in l:
        print(i)


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
            else:
                print('Pilha vazia')
        elif operacao == 'E':
            prato += 1  # Novo prato
            pilha.append(prato)
        elif operacao == 'S':
            break
        else:
            print('Operação invalida! Digite apenas E, D ou S!')


def pesquisa_sequencial():
    L = [15, 7, 27, 39]
    p = int(input('Digite o valor a procurar: '))
    v = int(input('Digite o valor a procurar: '))
    x = 0
    y = 0
    while x < len(L):
        if L[x] == p:
            break
        x += 1
    while y < len(L):
        if L[y] == v:
            break
        y += 1
    if x <= len(L) and y <= len(L):
        print(f'{p} foi achado na posição {x} e {v} foi achado na posição {y}')

    else:
        print(f'Não achou {p}')


def usando_for():
    L = [7, 9, 10, 12]
    p = int(input('Digite um numero a pesquisar: '))
    for e in L:
        if e == p:
            print('Elemento encontrado!')
            break
    else:
        print('Elemento não encontrado!')


def listas_range():
    for v in range(0, 10, 2):
        print(v)
    for t in range(3, 33, 3):
        print(t, end=" ")
    print()
    l = list(range(100, 1100, 50))
    print(l)


def listas_enumerate():
    l = [5, 9, 13]
    for z in enumerate(l):
        x, e = z
        print(z)
        print(f'[{x}] {e}')


def maior_menor():
    l = [1, 7, 2, 4]
    minimo = l[0]
    for e in l:
        if e < minimo:
            maximo = e
    print(minimo)


def temperatura():
    T = [-10, -8, 0, 1, 2, 5, -2, -4]
    minimo = T[0]
    maximo = T[0]
    media = 0
    for e in T:
        if e < minimo:
            minimo = e
        if e > maximo:
            maximo = e
        media += e
    resultado = media / len(T)
    print(f'A temperatura minima foi: {minimo}\n'
          f'A temperatura maxima foi: {maximo}\n'
          f'A temperatura media foi {resultado}')


def copia_de_elementos():
    v = [9, 8, 7, 12, 0, 13, 21]
    p = []
    i = []
    for e in v:
        if e % 2 == 0:
            p.append(e)
        else:
            i.append(e)
    print('Pares: ', p)
    print('Impares: ', i)


def controle_sala_de_cinema():
    lugares_vagos = [10, 2, 1, 3, 0]
    while True:
        sala = int(input('Sala (0 sai): '))
        if sala == 0:
            print('Fim')
            break
        if sala > len(lugares_vagos) or sala < 1:
            print('Sala invalida')
        elif lugares_vagos[sala - 1] == 0:
            print('Desculpe, sala lotada!')
        else:
            lugares = int(input(f'Quantos lugares você deseja ({lugares_vagos[sala - 1]}) vagos: '))
            if lugares > lugares_vagos[sala - 1]:
                print('Esse número de lugares não está disponível')
            elif lugares < 0:
                print('Numero invalido')
            else:
                lugares_vagos[sala - 1] -= lugares
                print(f'{lugares} lugares vendidos ')
        print('Utilização das salas')
        for x, l in enumerate(lugares_vagos):
            print(f'Sala {x + 1} - {l} lugar(es) vazio(s)')


def lista_de_compras():
    compras = []
    while True:
        produto = input('Produto: ')
        if produto == 'fim':
            break
        compras.append(produto)
    for p in compras:
        print(p)


def string():
    S = ['Maçã', 'peras', 'kiwis']
    print(S[2][1])


def lista_de_string():
    L = ['maçãs', 'peras', 'kiwis']
    for s in L:
        for letras in (s):
            print(letras)


def lista_de_lista():
    produto1 = ['maçã', 10, 0.30]
    produto2 = ['pera', 5, 0.75]
    produto3 = ['kiwi', 4, 0.98]
    compras = [produto1, produto2, produto3]
    for e in compras:
        print(f'Produto: {e[0]}')
        print(f'Quantidade: {e[1]}')
        print(f'Preço: {e[2]:5.2f}')


def criacao_lista_de_compras():
    compras = []
    while True:
        produto = input('Produto: ')
        if produto == 'fim':
            break
        quantidade = int(input('Digite a quantidade: '))
        preco = float(input('Digite o preço: '))
        compras.append([produto, quantidade, preco])
    soma = 0
    for e in compras:
        print(f'{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}')
        soma += e[1] * e[2]
        print(f'Total: {soma:7.2f}')


def bublle_sorte():
    L = [1, 2, 3, 4, 5]
    fim = 5
    while fim > 1:
        trocou = False
        x = 0
        while x < (fim - 1):
            if L[x] < L[x + 1]:
                trocou = True
                temp = L[x]
                L[x] = L[x + 1]
                L[x + 1] = temp
            x += 1
        if not trocou:
            break
        fim -= 1
    for e in L:
        print(e)


def dicionario():
    tabela = {'alface': 0.45,
              'Batata': 1.20,
              'Tomate': 2.30,
              'Feijão': 1.50}
    print(tabela['alface'])
    print(tabela)
    tabela['Tomate'] = 2.5
    print(tabela['Tomate'])
    tabela['cebola'] = 1.20
    print(tabela)
    print('Manga' in tabela)
    print('Batata' in tabela)
    print(tabela.keys())
    print(tabela.values())


def obtencao_de_valor_dicionario():
    tabela = {'alface': 0.45,
              'Batata': 1.20,
              'Tomate': 2.30,
              'Feijão': 1.50}
    while True:
        produto = input('Digite o nome do produto, fim para terminar: ')
        if produto == 'fim':
            break
        if produto in tabela:
            print(f'Preço {tabela[produto]:5.2f}')
        else:
            print('Produto não encontrado')


def dicionario_com_estoque():
    estoque = {'Alface': [500, 0.45],
               'Batata': [2001, 1.20],
               'Tomate': [1000, 2.30],
               'Feijão': [100, 1.50]}
    total = 0
    print('Vendas: \n')
    while True:
        produto = input('Digite o nome do produto, fim para terminar: ')
        quantidade = int(input('Digite a quantidade desejada: '))
        if produto == 'fim' or quantidade == 0:
            break
        if produto in estoque:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f'{produto:12s} : {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print('Produto não encontrado')

    print(f'Custo total: {total:21.2f}\n')
    print('Estoque: \n')
    for chave, dados in estoque.items():
        print('Descrição: ', chave)
        print('Quantidade: ', dados[0])
        print(f'Preço: {dados[1]:6.2f}\n')


def dicionario_de_frases():
    frase = {}
    letras = input('Digite a palavra: ')
    for letra in letras:
        if letra in frase:
            frase[letra] = frase[letra] + 1
        else:
            frase[letra] = 1
    print(frase)


def dicionario_sem_padrao():
    d = {}
    for letra in "abacadabra":
        if letra in d:
            d[letra] = d[letra] + 1
        else:
            d[letra] = 1
    print(d)


def dicionario_usando_get():
    d = {}
    for letra in "abacadabra":
        d[letra] = d.get(letra, 0) + 1
    print(d)


def comparacao_conjuntos():
    a = {0, 2, 3, 1, 5}
    b = {0, 1, 8, 7, 9}
    print(a & b)
    print(a - b)
    print(b - a)
    print((a - b) | (b - a))


def listas_conjunto():
    a = {0, 2, 3, 1, 5}
    b = {0, 1, 5, 2, 8, 7, 9}
    print(f'Novos elementos: {b - a}')
    print(f'Elementos que não mudaram {a & b}')
    print(f'Elementos removidos: {a - b}')


def pesquisa_string():
    s = 'um tigre, dois tigres, três tigres'
    p = 0
    while p > -1:
        p = s.find('tigre', p)
        if p >= 0:
            print(f'Posição: {p}')
            p += 1


def comparacao_string():
    a = 'AABBEFAATT'
    b = 'BE'
    p = 0
    while p > -1:
        p = a.find(b, p)
        if p >= 0:
            print(f'{b} encontrado na posição: {p} de {a}')
            p += 1


def geracao_de_string():
    a = 'AAACTBF'
    b = 'CBT'
    b = list(b)
    a = list(a)
    resultado = ''
    for i in range(3):
        if b[i] in a:
            resultado += b[i]
    print(resultado)


def unica_string():
    a = 'CTA'
    b = 'ABC'
    b = list(b)
    a = list(a)
    print(b)
    resultado = ''
    for i in range(3):
        if b[i] not in a:
            resultado += b[i]
        if a[i] not in b:
            resultado += a[i]
    print(resultado)


def leitura_string():
    letra = 'TTAAC'
    print(f'T: {letra.count("T")}')
    print(f'A: {letra.count("A")}')
    print(f'C: {letra.count("C")}')


def tratamento_string():
    a = 'AATTGGAA'
    b = 'TG'
    c = ''
    for letra in a:
        if letra not in b:
            c += letra
    print(c)


def substituicao_string():
    a = input("Digite a primeira string: ")
    b = input("Digite a segunda string: ")
    c = input("Digite a terceira string: ")

    if len(b) == len(c):
        resultado = ""
        for letra in a:
            posicao = b.find(letra)
            if posicao != -1:
                resultado += c[posicao]
            else:
                resultado += letra

        if resultado == "":
            print("Todos os caracteres foram removidos.")
        else:
            print(f"Os caracteres {b} foram substituidos por "
                  f"{c} em {a}, gerando: {resultado}")
    else:
        print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")


def jogo_da_forca():
    lista_de_palavras = ['amor', 'fato', 'viés', 'mito', 'caos', 'esmo',
                         'brio', 'como', 'vide', 'você', 'ação', 'após',
                         'sede', 'auge', 'pois', 'ermo', 'vida', 'ônus',
                         'saga', 'mote', 'suma', 'tolo', 'apto', 'idem',
                         'medo', 'crer', 'além', 'urge', 'veio', 'área',
                         'vovó', 'casa', 'sina', 'pude', 'zelo', 'cota',
                         'ruim', 'coxo', 'soar', 'ente', 'ater', 'rude',
                         'fase', 'pela', 'rima', 'voga', 'auto', 'mais',
                         'para', 'será', 'cedo', 'onde', 'cujo', 'tudo',
                         'sela', 'meio', 'trás', 'logo', 'teor', 'jugo',
                         'ante', 'cela', 'nojo', 'face', 'amar', 'pose']

    numero = int(input('Digite um numero'))
    indice = (numero * 776) % len(lista_de_palavras)
    palavra = lista_de_palavras[indice].lower().strip()
    for x in range(100):
        print()
    digitadas = []
    acertos = []
    erros = 0
    while True:
        senha = ''
        for letra in palavra:
            senha += letra if letra in acertos else '.'
        print(senha)
        if senha == palavra:
            print('Voê acertou!')
            break
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já tentou esta letra!')
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')
            print('X==:==\nX  :  ')
            print('X  0  ' if erros >= 1 else 'X')
            linha2 = ''
            if erros == 2:
                linha2 = '  |  '
            elif erros == 3:
                linha2 = ' \|  '
            elif erros >= 4:
                linha2 = '  \|/  '
            print(f'X{linha2}')
            linha3 = ''
            if erros == 5:
                linha3 += '  /    '
            elif erros >= 6:
                linha3 += '  / \   '
            print(f'X{linha3}')
            print('X\n===========')
            if erros == 6:
                print('Enforcado!')
                print(f'A palavra era {palavra}')
                break


def desenho_jogo(posicoes):
    print(f'{posicoes[0][0]}  |  {posicoes[0][1]}  |  {posicoes[0][2]}')
    print('---+---+---')
    print(f'{posicoes[1][0]}  |  {posicoes[1][1]}  |  {posicoes[1][2]}')
    print('---+---+---')
    print(f'{posicoes[2][0]}  |  {posicoes[2][1]}  |  {posicoes[2][2]}')


def valida_vencedor(matriz):
    venceu = False
    condicao_vitoria = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (1, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 1)]
    ]

    for x in condicao_vitoria:
        posicao1 = matriz[x[0][0]][x[0][1]]
        posicao2 = matriz[x[1][0]][x[1][1]]
        posicao3 = matriz[x[2][0]][x[2][1]]
        if '_' not in [posicao1, posicao2, posicao3]:
            if posicao1 == posicao2 == posicao3:
                venceu = True
                break

    return venceu


def troca_jogador(jogador):
    if jogador == 'x':
        jogador = 'o'
    else:
        jogador = 'x'
    return jogador


def jogo_da_velha():
    posicoes = [['', '', ''], ['', '', ''], ['', '', '']]
    print(desenho_jogo(posicoes))
    jogador = ''
    fim_de_jogo = False

    while True:
        if jogador != 'x' and jogador != 'o':
            jogador = input('Digite x ou o: ')
        else:
            break
    while True:
        print(f'Agora é a vez do {jogador}')
        for i in range(0, 3):
            entrada = ''
            for j in range(0, 3):
                if posicoes[i][j] not in ['x', 'o']:
                    entrada = input('Digite a posição para jogar: ')
                    if entrada == 1:
                        posicoes[0][0] = jogador
                        break
                    elif entrada == '2':
                        posicoes[0][1] = jogador
                        break
                    elif entrada == '3':
                        posicoes[0][2] = jogador
                        break
                    elif entrada == '4':
                        posicoes[1][0] = jogador
                        break
                    elif entrada == '5':
                        posicoes[1][1] = jogador
                        break
                    elif entrada == '6':
                        posicoes[1][2] = jogador
                        break
                    elif entrada == '7':
                        posicoes[2][0] = jogador
                        break
                    elif entrada == '8':
                        posicoes[2][1] = jogador
                        break
                    elif entrada == '9':
                        posicoes[2][2] = jogador
                        break
            if entrada != '':
                break
        desenho_jogo(posicoes)

        if valida_vencedor(posicoes):
            print(f'{jogador} Ganhou!')
            break

        jogador = troca_jogador(jogador)


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def epar(x):
    try:
        return x % 2 == 0
    finally:
        print('Executado antes de retornar')


def impar(x):
    return not epar(x)


def par_ou_impar(x):
    if epar(x):
        return 'par'
    else:
        return 'impar'


def maximo(a, b):
    if a > b:
        return a
    else:
        return b


def multipos(a, b):
    if a % b == 0:
        return True
    else:
        return False


def area(lado):
    A = lado * lado
    return A


def area_triangulo(base, altura):
    A = (base * altura) / 2
    return A


def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None


def soma2(l):
    total = 0
    for x in range(5):
        total += l[x]
    return total


def fatorial1(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat


def como_nao_escrever_uma_funcao():
    l = [1, 7, 2, 9, 15]
    print(soma2(l))


def teste():
    a = 7
    print(f'A dentro da função: {a}')


def pesquisa_lista():
    L = [10, 20, 25, 30]
    print(pesquise(L, 25))
    print(pesquise(L, 27))


def fatorial(n):
    print(f'Calculando o fatorial de {n}')
    if n == 0 or n == 1:
        print(f'Fatorial de {n} == 1')
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f'Fatorial de {n} = {fat}')
    return fat


def maior_divisor_comum(a, b):
    if b == 0:
        return a
    else:
        return maior_divisor_comum(b, a % b)


def menor_divisor_comum(a, b):
    resultado = (abs(a * b)) / maior_divisor_comum(a, b)
    return resultado


def fibonacci_sem_recursao():
    n = int(input('Digite um numero: '))
    v1 = 1
    v2 = 1
    soma = 0
    if n <= 2:
        return 1
    while n > soma:
        v3 = v1 + v2
        v1 = v2
        v2 = v3
        print(v3)
        soma += 1


def validacao_sem_recursao():
    while True:
        v = int(input('Digite um valor entre 0 e 5: '))
        if v < 0 or v > 5:
            print('Valor invalido.')
        else:
            break


def faixa_int(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f'Valor invalido. Digite um valor entre {minimo} e {maximo}')
        else:
            return v


def validacao_string(palavra, minimo, maximo):
    while True:
        v = input(palavra)
        if len(v) < minimo or len(v) > maximo:
            print(f'Valor invalido. Digite uma palavras com caracter entre {minimo} e {maximo}')
        else:
            return v


def lista_de_palavras():
    lista_de_palavras = ['amor', 'fato', 'viés', 'mito', 'caos', 'esmo',
                         'brio', 'como', 'vide', 'você', 'ação', 'após',
                         'sede', 'auge', 'pois', 'ermo', 'vida', 'ônus',
                         'saga', 'mote', 'suma', 'tolo', 'apto', 'idem',
                         'medo', 'crer', 'além', 'urge', 'veio', 'área',
                         'vovó', 'casa', 'sina', 'pude', 'zelo', 'cota',
                         'ruim', 'coxo', 'soar', 'ente', 'ater', 'rude',
                         'fase', 'pela', 'rima', 'voga', 'auto', 'mais',
                         'para', 'será', 'cedo', 'onde', 'cujo', 'tudo',
                         'sela', 'meio', 'trás', 'logo', 'teor', 'jugo',
                         'ante', 'cela', 'nojo', 'face', 'amar', 'pose']
    return lista_de_palavras


def validacao_string_lista(palavra, lista):
    while True:
        v = input(palavra)
        for v in lista:
            return True
        else:
            return False


def valida_entrada(mensagem, opcoes):
    opcoes1 = opcoes.lower()
    while True:
        escolha = input(mensagem)
        if escolha.lower() in opcoes1:
            break
        print("Erro: opção inválida. Redigite.\n")
    return escolha


def barra(n=10, caracter='*'):
    print(caracter * n)


def soma_parametros(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s


def funcao_retangulo(largura, altura, caracter='*'):
    linha = caracter * largura
    for i in range(altura):
        print(linha)


def imprime(a, b, foper):
    print(foper(a, b))


def funcoes_como_parametro():
    imprime(5, 4, soma)
    imprime(10, 1, subtracao)


def imprime_lista(l, fimpressao, fcondicao):
    for e in l:
        if fcondicao(e):
            fimpressao(e)


def imprime_elemento(e):
    print(f'Valor: {e}')


def configuracao_de_funcao_com_funcao():
    l = [1, 7, 9, 2, 11, 0]
    imprime_lista(l, imprime_elemento, epar)
    imprime_lista(l, imprime_elemento, impar)


def soma3(a, b):
    print(a + b)


def empacotamento_e_desempacotamento_de_parametros():
    l = [2, 3]
    soma3(*l)
    n = [[5, '-'], [10, '-'], [5], [6, '-']]
    for e in n:
        barra(*e)


def soma_com_indeterminados_parametros(*args):
    s = 0
    for x in args:
        s += x
    return s


def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)


def desempacotamento_de_parametros():
    print(soma_com_indeterminados_parametros(1, 2))
    print(soma_com_indeterminados_parametros(2))
    print(soma_com_indeterminados_parametros(5, 6, 7, 8))
    print(soma_com_indeterminados_parametros(9, 10, 20, 30, 40))
    print(imprime_maior('Maior:', 5, 4, 3, 1))
    print(imprime_maior('Max:', *[1, 7, 9]))


def funcao_lambda():
    a = lambda x: x * 2
    print(a(3))
    aumento = lambda b, c: (b * c / 100)
    print(aumento(100, 5))
    l = ['A', 'b', 'C', 'd', 'E']
    l.sort()
    print(l)
    l.sort(key=lambda k: k.lower())
    print(l)


def excecoes():
    nomes = ['Ana', 'Carlos', 'Maria']
    for tentativas in range(3):
        try:
            i = int(input('Digite o indice que vc quer imprimir: '))
            print(nomes[i])
        except ValueError:
            print('Digite um numero!')
        except IndexError:
            print('Valor valido entre -3 e 3')


def excecoes_das_excecoes():
    nomes = ['Ana', 'Carlos', 'Maria']
    for tentativas in range(3):
        try:
            i = int(input('Digite o indice que vc quer imprimir: '))
            print(nomes[i])
        except Exception as e:
            print(f'Algo de errado aconteceu: {e}')


def excecoes_finally():
    nomes = ['Ana', 'Carlos', 'Maria']
    for tentativas in range(3):
        try:
            i = int(input('Digite o indice que vc quer imprimir: '))
            print(nomes[i])
        except ValueError as e:
            print('Digite um numero!')
        finally:
            print(f'Tentativas {tentativas + 1}')


def excecoes_raise():
    nomes = ['Ana', 'Carlos', 'Maria']
    for tentativas in range(3):
        try:
            i = int(input('Digite o indice que vc quer imprimir: '))
            print(nomes[i])
        except ValueError as e:
            print('Digite um numero!')
            raise
        finally:
            print('Finally sempre executado')


def excecoes_funcao():
    try:
        print(2, epar(2))
        print('a', epar('a'))
    except Exception:
        print('Algo deu errado')


def excecoes_try_else_if():
    while True:
        try:
            v = int(input('Digite um numero inteiro (0 sai): '))
            if v == 0:
                break
        except Exception:
            print("Valor invalido")
        else:
            print('Parabens nenhuma exceção')
        finally:
            print('Executado sempre, mesmo com break')


def funcao_raint():
    for x in range(10):
        print(random.randint(1, 100))


def adivinhe_o_numero():
    n = random.randint(1, 10)

    tentativa = 3
    while tentativa > 0:
        x = int(input('Escolha um numero de 1 a 10: '))
        if x == n:
            print('Você acertou!')
            break
        else:
            print('Você errou')
            tentativa -= 1
            print(f'Você tem {tentativa}')
            if tentativa == 0:
                print('Acabou o numero de tentativas')


def funcao_random():
    for x in range(10):
        print(random.random())
        print(random.uniform(15, 25))
        print(random.sample(range(1, 101), 6))
    a = list(range(1, 11))
    random.shuffle(a)
    print(a)


def diz_o_tipo(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, list):
        return 'Lista'
    elif isinstance(a, dict):
        return 'Dicionario'
    elif isinstance(a, int):
        return 'Numero inteiro'
    elif isinstance(a, float):
        return 'Numero decimal'
    elif isinstance(a, types.FunctionType):
        return 'Função'
    elif isinstance(a, types.BuiltinFunctionType):
        return 'Função inteira'
    else:
        return str(type(a))


def diz_o_tipo_exemplos():
    print(diz_o_tipo(10))
    print(diz_o_tipo(10.5))
    print(diz_o_tipo('Alô'))
    print(diz_o_tipo([1, 2, 3]))
    print(diz_o_tipo({'a': 1, 'B': 50}))
    print(diz_o_tipo(print()))
    print(diz_o_tipo(None))
    L = [2, 'Alô', ["!"], {"a": 1, 'b': 2}]
    for e in L:
        print(type(e))


def navegando_listas_apartir_dos_elementos():
    l = ['a', ['b', 'c', 'd'], 'e']
    for x in l:
        if type(x) is str:
            print(x)
        else:
            print('Lista: ', end='')
            for z in x:
                print(f'{z}', end='')
                print()


def variaveis():
    espaco_por_nivel = 4
    return espaco_por_nivel


def imprime_elementos(l, nivel=0):
    espaco = '' * variaveis() * nivel
    if type(l) == list:
        print(espaco, '[')
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espaco, ']')
    else:
        print(espaco, l)


def comprehensions():
    l = [x for x in range(10)]
    k = [x * 2 for x in [0, 1, 2, 3]]
    y = [(x, x * 2) for x in [1, 2, 3]]
    z = [s.upper() for s in "abcdef"]
    p = [x for x in range(10) if x % 2 == 0]
    d = [(y, x) for x, y in [(4, 3), (2, 1), (8, 9)]]
    g = [(x, y) for *x, y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
    j = [(x, y) for x, *y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
    i = [math.sqrt(z) for z in range(0, 10)]
    h = [z for z in range(0, 10) if math.sqrt(z) % 1 == 0]
    print(l)
    print(k)
    print(y)
    print(z)
    print(p)
    print(d)
    print(g)
    print(j)
    print(i)
    print(h)


def gerador_de_numeros():
    i = 0
    while True:
        yield i
        i += 1


def geradores():
    g = gerador_de_numeros()
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    for x in gerador_de_numeros():
        print(x)


def gerador_fibonacci():
    p = 0
    s = 1
    while s < 10:
        yield s
        p, s = s, s + p


def resultado_gerador_de_fibonacci():
    l = [x for x in gerador_fibonacci()]
    print(l)


def gerador_numeros_primos():
    for y in (n for n in range(100) if n % 2 != 0 and n % 3 != 0 and n % 5 != 0):
        print(y)


def generator_fibonacci():
    def fibonacci(n):
        p = 0
        s = 1
        while n > 0:
            yield p
            p, s = s, s + p
            n -= 1

    for f in fibonacci(10):
        print(f)


def arquivos():
    arquivo = open('números.txt', 'w')
    for linha in range(1, 101):
        arquivo.write(f'{linha}\n')
    arquivo.close()


def abrindo_lendo_e_fechando_arquivos():
    arquivo = open('números.txt', 'r')
    for linha in arquivo.readline():
        print(linha)
    arquivo.close()


def uso_do_with():
    with open('números.txt', 'r') as arquivo:
        for linha in arquivo.readline():
            print(linha)


def parametros_da_linha_de_comando():
    print(f'Numero de parametros: {len(sys.argv)}')
    for n, p in enumerate(sys.argv):
        print(f'Parametro {n} = {p}')

# Usar no python console utilizar python ./nome do arquivo.txt parametros depois


def gravacao_de_numeros_pares_e_impares():
    with open('impares.txt', 'w') as impares, open('pares.txt', 'w') as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f'{n}\n')
            else:
                impares.write(f'{n}\n')


def multiplos_de_4():
    with open("multiplos de 4.txt", "w") as multiplos4:
        with open("pares.txt") as pares:
            for l in pares.readlines():
                if int(l) % 4 == 0:
                    multiplos4.write(l)


def le_numero(arquivo):
    while True:
        numero = arquivo.readline()
        if numero == '':
            return None
        if numero.strip() != '':
            return int(numero)


def escreve_numero(arquivo, n):
    arquivo.write(f'{n}\n')


def pareseimpares():
    pares = open('pares.txt')
    impares = open('impares.txt')
    pares_e_impares = open('pareseimpares.txt', 'w')
    npar = le_numero(pares)
    nimpar = le_numero(impares)
    while True:
        if npar is None and nimpar is None:
            break
        if npar is not None and (nimpar is None or npar <= nimpar):
            escreve_numero(pares_e_impares, npar)
            npar = le_numero(pares)
        if nimpar is not None and (npar is None or nimpar <= npar):
            escreve_numero(pares_e_impares, nimpar)
            nimpar = le_numero(impares)
    pares.close()
    impares.close()
    pares_e_impares.close()


def linhas_invertidas():
    pares = open('pares.txt', 'r')
    lista_invertida = open('lista_invertida.txt', 'w')
    l = pares.readlines()
    l.reverse()
    for x in l:
        lista_invertida.write(x)
    pares.close()
    lista_invertida.close()


def processamento_de_um_arquivo():
    largura = 79
    with open('arquivo.txt')  as entrada:
        for linha in entrada.readlines():
            if linha[0] == ';':
                continue
            elif linha[0] == '=':
                print('=' * 40)
            elif linha[0] == '.':
                input('Digite algo para continuar: ')
                print()
            elif linha[0] == '>':
                print(linha[:1].rjust(largura))
            elif linha[0] == '*':
                print(linha[1:].center(largura))
            else:
                print(linha)


def arquivo_paginado():
    print()


def main():
    processamento_de_um_arquivo()


if __name__ == '__main__':
    main()
