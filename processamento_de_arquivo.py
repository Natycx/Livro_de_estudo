Largura = 79
with open('entrada.txt') as entrada:
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(Largura))
        elif linha[0] == '=':
            print('=' * 40)
        elif linha[0] == '*':
            print(linha[1:].center(Largura))
        elif linha[0] == '.':
            input('Digite algo para continuar: ')
            print()
        else:
            print(linha)