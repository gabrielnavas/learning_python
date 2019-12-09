def bolha(lista: []):
    tl = len(lista) - 1

    while tl > 0:
        for i in range(tl):
            if len(lista[i+1]) > len(lista[i]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
        tl -= 1

n = int(input())
while n > 0:
    words = input().rsplit(' ')

    bolha(words)

    tl = len(words)
    for i in range(tl-1):
        print(words[i], end=' ')

    print(words[-1])

    n -= 1
