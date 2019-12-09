branco_p = []
branco_m = []
branco_g = []
vermelho_p = []
vermelho_m = []
vermelho_g = []

n = int(input())

while n != 0:

    while 2*n > 0:
        nome = input()
        cor, tamanho = input().rsplit(' ')

        if cor == 'branco':
            if tamanho == 'P':
                branco_p.append(nome)
            elif tamanho == 'M':
                branco_m.append(nome)
            else:
                branco_g.append(nome)
        else:
            if tamanho == 'P':
                vermelho_p.append(nome)
            elif tamanho == 'M':
                vermelho_m.append(nome)
            else:
                vermelho_g.append(nome)
        n -= 1

    branco_p.sort()
    branco_m.sort()
    branco_g.sort()
    vermelho_p.sort()
    vermelho_m.sort()
    vermelho_g.sort()

    for nome in branco_p:
        print('branco P {}'.format(nome))

    for nome in branco_m:
        print('branco M {}'.format(nome))

    for nome in branco_g:
        print('branco G {}'.format(nome))


    for nome in vermelho_p:
        print('vermelho P {}'.format(nome))

    for nome in vermelho_m:
        print('vermelho M {}'.format(nome))

    for nome in vermelho_g:
        print('ermelho G {}'.format(nome))

    n = int(input())
    print()
    branco_p.clear()
    branco_m.clear()
    branco_g.clear()
    vermelho_p.clear()
    vermelho_m.clear()
    vermelho_g.clear()


