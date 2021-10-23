import sys
if len(sys.argv) != 4:
    print("\nUso: e09-04.py primeiro segundo saída\n\n")
else:
    primeiro = open(sys.argv[1], 'r')
    segundo = open(sys.argv[2], 'r')
    saida = open(sys.argv[3], 'w')

    for l1 in primeiro:
        saida.write(l1)
    for l2 in segundo:
        saida.write(l2)

    primeiro.close()
    segundo.close()
    saida.close()