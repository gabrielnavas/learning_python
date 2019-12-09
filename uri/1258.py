ll = [[] for _ in range(6)]


#ll[0] = branco p 
#ll[1] = //     m
#ll[2] = //     g
#ll[3] = vermelho p
#ll[4] = vermelho m
#ll[5] = vermelho g


n = int(input())
while n != 0:

    # filter
    while 2*n > 0:
        nome = input()
        cor, tamanho = input().rsplit(' ')

        if cor == 'branco':
            if tamanho == 'P':
                ll[0].append(nome)
            elif tamanho == 'M':
                ll[1].append(nome)
            else:
                ll[2].append(nome)
        else:
            if tamanho == 'P':
                ll[3].append(nome)
            elif tamanho == 'M':
                ll[4].append(nome)
            else:
                ll[5].append(nome)
        n -= 1

    # sort all
    for l in ll:
        l.sort()

    # show result set
    for nome in ll[0]:
        print('branco P {}'.format(nome))
                
    for nome in ll[1]:
        print('branco M {}'.format(nome))

    for nome in ll[2]:
        print('branco G {}'.format(nome))


    for nome in ll[3]:
        print('vermelho P {}'.format(nome))

    for nome in ll[4]:
        print('vermelho M {}'.format(nome))

    for nome in ll[5]:
        print('vermelho G {}'.format(nome))

    n = int(input())

    if n > 0:
        print()
            
    for l in ll:
        l.clear()
    

