arquivo = open('texto.txt')
LARGURA = 76
LINHA = 60
GUARDANDO = ''
saida = open('saida_paginada.txt', 'w')
for index ,linha in enumerate(arquivo.readlines()):
    texto = ''
    if GUARDANDO == '':
        texto = linha
    else:
        texto = GUARDANDO + ' ' + linha

    texto = texto.replace('\n', '')

    if len(texto) > LARGURA:
        GUARDANDO = texto[77::]
        texto = texto[:76]
    else:
        GUARDANDO = ''

    if (index + 1) % 60 == 0:
        espacamento = f'\n{arquivo.name} --- pagina {(index + 1) // 60}\n' \
                      f'\n'
        saida.write(espacamento)
    saida.write(texto + '\n')
if GUARDANDO != '':
    saida.write(GUARDANDO)
saida.close()




